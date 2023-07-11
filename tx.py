import requests
import base64

def get_transactions(block_number):
    url = f"https://akash.mintscan.io/api/blocks/{block_number}"
    
    response = requests.get(url)
    data = response.json()

    transactions = data["result"]["data"]["txs"]
    
    if transactions:
        for transaction in transactions:
            encoded_data = transaction["tx"]["value"]["msg"][0]["value"]["data"]
            decoded_data = base64.b64decode(encoded_data).decode()
            print(decoded_data)
    else:
        print("No transactions found in the block.")
