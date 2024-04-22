# Deploying Smart Contracts on Mazze Testnet

This guide will walk you through deploying, testing, and interacting with your smart contracts on the Mazze Testnet. Since Mazze is EVM-compatible, you can use familiar Ethereum tools like Truffle, Hardhat, or Remix for your development process.

### Prerequisites

* Ensure your Metamask is configured for the Mazze Testnet. See our guide on How to Add the Mazze Testnet to Metamask.
* Have some test MAZZE tokens in your account to pay for gas fees. You can obtain these from our Testnet Faucet.

### Step 1: Setting Up Your Development Environment

#### Using Truffle

1.  **Install Truffle**\
    Install Truffle globally on your machine if you haven't already:

    ```bash
    npm install -g truffle
    ```
2.  **Initialize a New Truffle Project**

    ```bash
    mkdir MyDapp && cd MyDapp
    truffle init
    ```
3.  **Configure Truffle to Use Mazze Testnet**\
    Edit `truffle-config.js` to add the Mazze Testnet configuration:

    ```javascript
    module.exports = {
      networks: {
        mazze-testnet: {
          provider: () => new HDWalletProvider(process.env.MNEMONIC, "https://testnet-rpc.mazze.io"),
          network_id: 199991,
          gas: 5500000,        // Gas limit used for deploys
          confirmations: 2,    // # of confs to wait between deployments
          timeoutBlocks: 200,  // # of blocks before a deployment times out
          skipDryRun: true     // Skip dry run before migrations? (default: false for public nets)
        },
      },
      // Other configurations...
    };
    ```

#### Using Hardhat

1.  **Install Hardhat**\
    Set up a new Hardhat project if you haven't already:

    ```bash
    npm init -y
    npm install --save-dev hardhat
    ```
2.  **Create a Hardhat Project**

    ```bash
    npx hardhat
    ```
3.  **Configure Hardhat to Connect to Mazze Testnet**\
    Modify `hardhat.config.js`:

    ```javascript
    require('@nomiclabs/hardhat-ethers');

    module.exports = {
      defaultNetwork: "mazze-testnet",
      networks: {
        mazze-testnet: {
          url: "https://testnet-rpc.mazze.io",
          accounts: [process.env.PRIVATE_KEY]
        }
      },
      solidity: "0.8.4",
    };
    ```

### Step 2: Writing Your Smart Contract

Create a simple smart contract. Here's an example of a simple storage contract in Solidity:

```solidity
// contracts/SimpleStorage.sol
pragma solidity ^0.8.4;

contract SimpleStorage {
    uint public storedData;

    constructor(uint initialValue) {
        storedData = initialValue;
    }

    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
```

### Step 3: Deploying Your Smart Contract

Deploy your contract using Truffle or Hardhat:

#### Using Truffle

Create a migration file and deploy your contract:

```javascript
// migrations/2_deploy_contracts.js
const SimpleStorage = artifacts.require("SimpleStorage");

module.exports = function(deployer) {
  deployer.deploy(SimpleStorage, 100);
};
```

Run the migration:

```bash
truffle migrate --network mazze-testnet
```

#### Using Hardhat

Deploy your contract with a script:

```javascript
// scripts/deploy.js
async function main() {
  const [deployer] = await ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);

  const SimpleStorage = await ethers.getContractFactory("SimpleStorage");
  const simpleStorage = await SimpleStorage.deploy(100);

  console.log("SimpleStorage deployed to:", simpleStorage.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

Run the deployment script:

```bash
npx hardhat run scripts/deploy.js --network mazze-testnet
```

### Step 4: Interacting with Your Deployed Contract

After deploying, you can interact with your contract through scripts or frontend applications.
