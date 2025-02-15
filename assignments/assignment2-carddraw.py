# Suffles a deck of cards and gets 5 cards from it via API
# author: atacan buyuktalas

import requests
import json

# Shuffle Deck API URL
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

# Get the deck id
response = requests.get(url)
#print(response.json())
deck_id = response.json()['deck_id']

# Get 5 cards from the deck
url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(url)
#print(response.json())
cards = response.json()['cards']

# Print the cards
for card in cards:
    print(f"{card['value']} of {card['suit']}")
