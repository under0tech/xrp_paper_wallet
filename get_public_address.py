from xrpl.wallet import Wallet

secret_key = ''
with open("secret_key.txt", "r") as secret_key_file:
    secret_key = secret_key_file.read().strip()

if secret_key:
    wallet = Wallet.from_secret(seed=secret_key)
    public_address = wallet.classic_address
    print("Public XRP address:", public_address)

