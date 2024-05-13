from xrpl.wallet import Wallet

wallet = Wallet.create()
with open("secret_key.txt", "w") as secret_key_file:
    secret_key_file.write(wallet.seed)

print("Paper wallet created and secret key saved.")



