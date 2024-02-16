import json

class MatchMetadata:
    def __init__(self, data_version: int, match_id: str, participants: list[str]):
        self.match_id = match_id
        self.data_version = data_version
        self.participants = participants

    @staticmethod
    def initialize_from_json(data):
        try:
            match_metadata = MatchMetadata(
                data_version=data['dataVersion'],
                match_id=data['matchId'],
                participants=data['participants']
            )
            return match_metadata

        except KeyError as e:
            raise Exception(f"Missing key in JSON data: {e}")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON data")
