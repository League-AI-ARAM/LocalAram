import enums
from Player import Player

PLATFORM = enums.Platform.NA1
NAME = "BeastMachine#1338"

beast = Player(NAME, PLATFORM)

history = beast.match_history
print(history.matches[0].game_id)
