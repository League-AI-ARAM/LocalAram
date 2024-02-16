import enums
from Player import Player
from MatchMetadata import MatchMetadata
from MatchInfo import MatchInfo
from database import data

PLATFORM = enums.Platform.NA1
NAME = "BeastMachine#1338"

beast = Player(NAME, PLATFORM)

history = beast.match_history
print(history.matches[0].game_id)
