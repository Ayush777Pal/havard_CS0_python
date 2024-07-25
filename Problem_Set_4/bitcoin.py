import requests
import sys

if len(sys.argv)==2:
    try:
        value=float(sys.argv[1])
        pass
    except:
       print("Missing command line argument")
       sys.exit(1)
else:
    print("Missing command line argument")
    sys.exit(1)

try:
    r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response=r.json()
    x=response["bpi"]["USD"]["rate_float"]
    y=x*value
    print(f"${y:,.4f}")
except requests.RequestException:
    print("Request Exception")
    sys.exit(1)