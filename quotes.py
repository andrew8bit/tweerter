import requests
from random import seed
from random import choice

url = "https://type.fit/api/quotes"
r = requests.get(url = url)
response = r.json()

def quote_picker():
    quote = choice(response)
    return f"{quote['text']} - {quote['author']}"

new = quote_picker()
