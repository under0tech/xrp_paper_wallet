# XRP Paper wallet and beyond
Native XRP code for creating XRP paper wallet, getting the public address and sending XRP to Binance with Tag in transaction

### Install the dependencies
```bash
pip3 install -r requirements.txt
```

### Run the create_wallet.py 
**to generate new wallet** and save secret key to file `secret_key.txt`
```bash
python3 create_wallet.py
```

### Run the get_public_address.py 
**to read public XRP address** to give it to the people who will send XRP to you
```bash
python3 get_public_address.py
```

### Run the send_xrp.py 
**to send XRP to Binance** or any other XRP address with no destination Tag included
```bash
python3 send_xrp.py
```

## Learn more on official XRP Ledger web-page
Learn how to prepare the transaction, sign, submit to the network, validate and check the current status on the official XRP Ledger resource.

[Interactive guide on sending XRP](https://xrpl.org/docs/tutorials/how-tos/send-xrp/#interactive-submit)