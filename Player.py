import requests
from API import headers
from enums import Region, Platform
from MatchHistory import MatchHistory


class Player:
    def __init__(self, summoner_name: str, platform: Platform):
        self.summoner_name: str = summoner_name
        self.platform: Platform = platform
        self.region: Region = Region.get_region(platform)
        self.puuid: str = self._get_puuid()
        self.match_history: MatchHistory = self._get_matches()

    def _get_matches(self, count: int = 1) -> MatchHistory:
        return MatchHistory(self, count)

    def _get_puuid(self) -> str:
        url = f"https://{self.platform}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner_name}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("puuid")
        else:
            raise Exception(
                f"Error getting PUUID: {response.status_code}, {response.reason}"
            )
