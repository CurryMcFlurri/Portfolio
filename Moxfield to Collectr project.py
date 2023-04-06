import requests

# authenticate with Moxfield API
moxfield_api_key = "your-moxfield-api-key"
moxfield_headers = {
    "Authorization": f"Bearer {moxfield_api_key}"
}

# authenticate with Collectr API
collectr_api_key = "your-collectr-api-key"
collectr_headers = {
    "Authorization": f"Bearer {collectr_api_key}"
}

# prompt user to enter the name of the deck to upload cards from
deck_name = input("Enter the name of the deck to upload cards from: ")

# retrieve deck from Moxfield
response = requests.get("https://api.moxfield.com/api/v1/decks", headers=moxfield_headers)
decks = response.json()

deck_id = None
for deck in decks:
    if deck['name'] == deck_name:
        deck_id = deck['id']
        break

if deck_id is None:
    print(f"No deck found with name {deck_name}")
    exit()

# retrieve cards from the specified deck with value over $5
response = requests.get(f"https://api.moxfield.com/api/v1/decks/{deck_id}/cards", headers=moxfield_headers)
cards = response.json()

cards_to_upload = []
for card in cards:
    if card['value'] > 5:
        cards_to_upload.append(card)

# upload cards to Collectr
for card in cards_to_upload:
    response = requests.post("https://api.collectr.com/cards", headers=collectr_headers, json=card)
    if response.status_code == 200:
        print(f"Card {card['name']} uploaded successfully!")
    else:
        print(f"Error uploading card {card['name']}")
