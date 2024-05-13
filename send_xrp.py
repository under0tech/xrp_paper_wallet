from xrpl import transaction, utils
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.transactions import Payment

# https://xrpl.org/docs/tutorials/public-servers/
client = JsonRpcClient("https://s1.ripple.com:51234/") # Mainnet

# https://xrpscan.com/account/rK1LBHKR5KcjDnQ5ejj9whBNSma7uPXvRD
# sender_address = "rK1LBHKR5KcjDnQ5ejj9whBNSma7uPXvRD"

sender_secret = "sEdVnMBXUjya7bwdMLuedckJsntbsCN" # Secret key from your file
destination_address = "rNxp4h8apvRis6mJf9Sh8C6iRxfrDWN7AV" # Deposit address on Binance
destination_tag = 316143501 # Tag on Binance
amount = utils.xrp_to_drops(19.80)  # The amount of XRP to send

wallet = Wallet.from_secret(seed=sender_secret)

payment_transaction = Payment(
    account=wallet.classic_address,
    amount=amount,
    destination=destination_address,
    destination_tag=destination_tag,
)

signed_tx = transaction.autofill_and_sign(
        payment_transaction, client, wallet)

try:
    tx_response = transaction.submit_and_wait(signed_tx, client)
    print(tx_response)
except transaction.XRPLReliableSubmissionException as e:
    exit(f"Submit failed: {e}")
