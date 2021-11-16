
# my matchups
# 

import requests


response2 = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/uAl0d3Ipq86eAflYFHLH4z_H9kTqOnDODFDTtnRgfdNEQfw5E3iJTfDWtGnFesz_SFa9dGDJkEWqLg/ids", headers={'X-Riot-Token':'RGAPI-1da60881-013a-4d2e-a088-46c8ac2d25a9'})
games_id = response2.text.rsplit(',')
print(games_id)
response = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/"+response2.text[0], headers={'X-Riot-Token':'RGAPI-1da60881-013a-4d2e-a088-46c8ac2d25a9'})
print(response.text)
print("hello")