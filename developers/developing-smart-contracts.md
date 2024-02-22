---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Developing Smart Contracts

To begin working with Mazze blockchain, which is compatible with the Ethereum Virtual Machine (EVM), you'll first need to install Hardhat in your project directory.

Execute the following command to install Hardhat:

```bash
npm install --save-dev hardhat
```

After installation, initiate Hardhat by running `npx hardhat`. This action will generate a Hardhat configuration file (`hardhat.config.js`) in your project directory:

```bash
npx hardhat
```

You'll be greeted by the Hardhat interface:

```
npx hardhat

Welcome to Hardhat v2.2.1

✔ What do you want to do? · Create an empty hardhat.config.js
Config file created
```

The next step is to create your first smart contract. In the `contracts` directory, store your Solidity source files (.sol). Let's start with a basic contract named `Box`, which allows storing and retrieving a value.

Create the contract in the file `contracts/Box.sol`:

```solidity
// contracts/Box.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Box {
    uint256 private _value;

    // Emitted when the stored value changes
    event ValueChanged(uint256 value);

    // Stores a new value in the contract
    function store(uint256 value) public {
        _value = value;
        emit ValueChanged(value);
    }

    // Reads the last stored value
    function retrieve() public view returns (uint256) {
        return _value;
    }
}
```

For compiling Solidity code to EVM bytecode, configure Hardhat to use a suitable Solidity compiler version, matching your contract's requirements. In `hardhat.config.js`, specify Solidity 0.8 for our `Box.sol` contract:

```solidity
// hardhat.config.js

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
 module.exports = {
  solidity: "0.8.4",
};
```

To compile, run:

```bash
npx hardhat compile
```

Hardhat will compile all contracts in the `contracts` directory. The compiled artifacts (bytecode and metadata) will be stored in the `artifacts` directory.

As your project expands, you might create more contracts. For instance, let's add an access control system to our `Box` contract. We'll create an `Auth` contract that stores an administrator address. This contract will be placed in a subdirectory, like `contracts/access-control/Auth.sol`.

```solidity
// contracts/access-control/Auth.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Auth {
    address private _administrator;

    constructor(address deployer) {
        // Make the deployer of the contract the administrator
        _administrator = deployer;
    }

    function isAdministrator(address user) public view returns (bool) {
        return user == _administrator;
    }
}
```

To integrate `Auth` with `Box`, use an import statement in `Box.sol`:

```solidity
// contracts/Box.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import Auth from the access-control subdirectory
import "./access-control/Auth.sol";

contract Box {
    uint256 private _value;
    Auth private _auth;

    event ValueChanged(uint256 value);

    constructor() {
        _auth = new Auth(msg.sender);
    }

    function store(uint256 value) public {
        // Require that the caller is registered as an administrator in Auth
        require(_auth.isAdministrator(msg.sender), "Unauthorized");

        _value = value;
        emit ValueChanged(value);
    }

    function retrieve() public view returns (uint256) {
        return _value;
    }
}
```

For advanced modularization, consider using inheritance in Solidity. A great resource for reusable modules and libraries is the OpenZeppelin Contracts library. It's thoroughly audited for security and correctness.

To use OpenZeppelin Contracts, install the library:

```bash
npm install @openzeppelin/contracts
```

Then, import the necessary contracts from OpenZeppelin. For example, to add access control to `Box`, replace the `Auth` contract with `Ownable` from OpenZeppelin:

```solidity
// contracts/Box.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import Ownable from the OpenZeppelin Contracts library
import "@openzeppelin/contracts/access/Ownable.sol";

// Make Box inherit from the Ownable contract
contract Box is Ownable {
    uint256 private _value;

    event ValueChanged(uint256 value);

    constuctor() Ownable(msg.sender) {}

    // The onlyOwner modifier restricts who can call the store function
    function store(uint256 value) public onlyOwner {
        _value = value;
        emit ValueChanged(value);
    }

    function retrieve() public view returns (uint256) {
        return _value;
    }
}
```

For more information on developing secure smart contract systems, refer to the [<mark style="color:orange;">OpenZeppelin</mark> <mark style="color:orange;">Contracts documentation</mark>](https://docs.openzeppelin.com/contracts/5.x/), including their [<mark style="color:orange;">Access Control guide</mark>](https://docs.openzeppelin.com/contracts/5.x/access-control).
