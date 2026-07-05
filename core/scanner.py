import requests


def get_coinbase_products():
    """
    Returns all Coinbase Exchange USD trading pairs.
    """

    url = "https://api.exchange.coinbase.com/products"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    products = response.json()

    usd_pairs = []

    for product in products:

        product_id = product["id"]

        if product_id.endswith("-USD"):
            usd_pairs.append(product_id)

    return sorted(usd_pairs)


if __name__ == "__main__":

    coins = get_coinbase_products()

    print(f"\nFound {len(coins)} USD trading pairs:\n")

    for coin in coins:
        print(coin)