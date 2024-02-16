import requests
from enums import Region
import json
from API import headers
import Player
from MatchInfo import MatchInfo

class MatchHistory:
    def __init__(self, player: Player, count: int):
        self.puuid: str = player.puuid
        self.region: Region = player.region
        self.match_ids: list[str] = self._get_match_history(count)

        self.matches: list[MatchInfo] = []

        for match_id in self.match_ids:
            self.matches += [self.get_match(match_id)]

    def get_match(self, match_id: str) -> MatchInfo:
        url = f"https://{self.region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error getting match IDs: {response.status_code}, {response.reason}")
        
        return MatchInfo.initialize_from_json(response.json())
            

    def _get_match_history(self, count: int=20) -> list[str]:
        """
        Fetch the match history for a given summoner name.

        :param summoner_name: The summoner's name in the game.
        :param count: Number of matches to retrieve.
        :return: A list of match IDs or None if an error occurs.
        """
        url = f"https://{self.region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{self.puuid}/ids?start=0&count={count}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error getting match history: {response.status_code}, {response.reason}")

