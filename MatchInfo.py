import json

class Objective:
    def __init__(self, first: bool, kills: int):
        self.first = first
        self.kills = kills

class Team:
    def __init__(self, team_id: int, win: bool, bans, objectives: dict[Objective]):
        self.team_id = team_id
        self.win = win
        self.bans = bans
        self.objectives = objectives

class MatchInfo:
    """Represents detailed information about a match."""

    def __init__(self, end_of_game_result: str, game_creation: int, game_duration: int, game_end_timestamp: int, game_id: int, game_mode: str, game_name: str, game_start_timestamp: int, game_type: str, game_version: str, map_id: int, participants: list[str], platform_id: str, queue_id: int, teams: list[Team]) -> None:
        self.end_of_game_result = end_of_game_result
        self.game_creation = game_creation
        self.game_duration = game_duration
        self.game_end_timestamp = game_end_timestamp
        self.game_id = game_id
        self.game_mode = game_mode
        self.game_name = game_name
        self.game_start_timestamp = game_start_timestamp
        self.game_type = game_type
        self.game_version = game_version
        self.map_id = map_id
        self.participants = participants
        self.platform_id = platform_id
        self.queue_id = queue_id
        self.teams = teams
        
    @staticmethod
    def initialize_from_json(data):
        data = data["info"]

        # Parse teams
        teams = []
        for team_data in data.get('teams', []):
            objectives = {}
            for key, obj in team_data.get('objectives', {}).items():
                objectives[key] = Objective(first=obj.get('first', False), kills=obj.get('kills', 0))
            
            team = Team(
                team_id=team_data.get('teamId'),
                win=team_data.get('win'),
                bans=team_data.get('bans', []),
                objectives=objectives
            )
            teams.append(team)

        # Create MatchInfo instance
        return MatchInfo(
            end_of_game_result=data.get('endOfGameResult'),
            game_creation=data.get('gameCreation'),
            game_duration=data.get('gameDuration'),
            game_end_timestamp=data.get('gameEndTimestamp'),
            game_id=data.get('gameId'),
            game_mode=data.get('gameMode'),
            game_name=data.get('gameName'),
            game_start_timestamp=data.get('gameStartTimestamp'),
            game_type=data.get('gameType'),
            game_version=data.get('gameVersion'),
            map_id=data.get('mapId'),
            participants=data.get('participants', []),
            platform_id=data.get('platformId'),
            queue_id=data.get('queueId'),
            teams=teams
        )