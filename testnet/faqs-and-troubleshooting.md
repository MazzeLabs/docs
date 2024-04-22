# FAQs and Troubleshooting

This page addresses some of the frequently asked questions and common issues that developers encounter when working with the Mazze Testnet. Below, you’ll find solutions and tips to help you resolve these issues quickly.

## FAQs

#### Q1: How do I add the Mazze Testnet to my Metamask?

**A:** To add the Mazze Testnet to Metamask, you need to access the network settings in Metamask and enter the following details:

* Network Name: Mazze Testnet
* New RPC URL: `https://testnet-rpc.mazze.io`
* Chain ID: `199991`
* Currency Symbol: MAZZE

For a detailed guide, see our page on [How to Add the Mazze Testnet to Metamask](how-to-add-the-mazze-testnet-to-metamask.md).

#### Q2: Where can I get test MAZZE tokens for the testnet?

**A:** Test MAZZE tokens can be obtained from our testnet faucet. Visit the [Mazze Testnet Faucet page](https://faucet.mazze.io), enter your wallet address and click on "Request Tokens."

#### Q3: What tools can I use to develop and test smart contracts on the Mazze Testnet?

**A:** Since Mazze is EVM-compatible, you can use all the popular Ethereum development tools like Remix, Truffle, Hardhat and others for developing and testing your smart contracts.

## Troubleshooting

#### Issue 1: I cannot connect to the Mazze Testnet via Metamask.

**Solution:** Ensure that you have the correct RPC URL (`https://testnet-rpc.mazze.io`) and Chain ID (`199991`). If the problem persists, try clearing your browser cache or restarting Metamask.

#### Issue 2: I haven’t received any test MAZZE tokens from the faucet.

**Solution:**

* Check your internet connection and ensure that there is no network outage.
* Verify that you have entered the correct wallet address.
* If there’s still a delay, it might be due to network congestion. Please wait a few minutes and check your wallet again.

#### Issue 3: My smart contract transactions keep failing.

**Solution:**

* Double-check the gas limit and gas price settings in your transaction.
* Ensure you have enough test MAZZE tokens in your account to cover transaction fees.
* Review your smart contract code for any errors that might cause the transaction to fail.
* If using Remix or other tools, ensure they are configured correctly to connect to the Mazze Testnet.

#### Issue 4: How do I report a bug or issue with the testnet?

**Solution:** If you encounter a bug or an issue not covered in this FAQ, please report it to our support team. Provide detailed information including the error messages received, screenshots and steps to reproduce the issue. You can contact us via Discord in our dedicated channel  `#testnet-feedback`.
