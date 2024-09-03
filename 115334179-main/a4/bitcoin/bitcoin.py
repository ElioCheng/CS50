import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Error! Incorrect number of command line arguements :(")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Error! Incorrect type of command line argument :(")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Unknown Error")
price = response.json()
price_usd = price["bpi"]["USD"]["rate_float"]
price_usd *= n
print(f"${price_usd:,.4f}")
