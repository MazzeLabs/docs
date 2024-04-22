# Temporary Limitations

As we launch the Mazze Testnet, it's important to understand some of the current limitations and why they exist. This will help set expectations for developers and testers, ensuring everyone understands the temporary constraints and the path forward for the testnet.

## Throttled Mode Operation

The Mazze Testnet is presently operating in a throttled mode, which is a necessary measure to maintain network stability and efficiency during the initial phases of our testing environment. This limitation has specific impacts on how transactions and blocks are processed:

* **Single Internal Miner Controlled Block Production.** Currently, the Mazze Testnet is managed by a single internal miner. This setup is intended to stabilize the early test phases and control the block production rate closely.
* **Block Finality Time Increased Block Time.** To prevent network overload and ensure smooth operation, the block time has been set to approximately 3 seconds. This is longer than the anticipated final block time but is necessary under the current configuration to accommodate thorough testing without risking performance degradation.

## Implications for Developers

Given the current configuration, developers and testers may notice the following:&#x20;

* **Slower Transaction Confirmation.** With a block time of 3 seconds, you might experience slower transaction confirmations compared to a fully operational network. This is expected, given the throttled mode.&#x20;
* **Limited Throughput.** The current setup may result in limited throughput, meaning fewer transactions processed per second compared to a fully decentralized network. Testing Focus: This throttled mode is ideal for testing individual smart contracts, deployment strategies, and transaction workflows without overloading the system.

## Future Plans and Adjustments

* **Opening to External Miners.** Soon, we plan to open the testnet to external miners. This transition will mark a significant scaling up of network operations and is expected to help us move towards more realistic operational conditions.
* **Reduced Block Time.** Once the network is sufficiently robust and external miners begin participating, we aim to reduce the block finality time to approximately 1 second. This will bring the network closer to our target specifications for speed and efficiency.

## Developer Guidance

During this phase, we encourage developers to:

* **Monitor Network Updates.** Stay updated with the latest changes and enhancements to the testnet. Adjustments to the mining process and block time will be communicated through official channels. Test Accordingly: Plan your testing activities with the current limitations in mind. This involves preparing for higher block times and being adaptable to changes in network conditions.&#x20;
* **Provide Feedback.** Your feedback is invaluable. Please share your experiences and any issues encountered while using the testnet. This information will be crucial for us as we continue to refine and enhance the network.

{% hint style="success" %}
We appreciate your participation and patience as we work through these early stages of the testnet. These limitations are temporary and are in place to ensure that the Mazze Testnet can evolve into a stable and efficient platform. We are committed to making continual improvements and look forward to achieving the full potential of the Mazze blockchain with your help.
{% endhint %}
