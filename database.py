import sqlite3
import MatchMetadata


class data:
    def __init__(self):
        self.conn = sqlite3.connect("./data/LoLData.db")
        self.cursor = self.conn.cursor()
        self.__create()

    def run_query(self, query: str) -> None:
        self.cursor.execute(query)

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def __create(self):
        # Create the MatchMetadata table
        self.run_query(
            """
            CREATE TABLE IF NOT EXISTS MatchMetadata (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DataVersion INTEGER,
                MatchID INTEGER,
                Participant TEXT
            )
        """
        )

        # Create the PlayerStats table
        self.run_query(
            """
            CREATE TABLE IF NOT EXISTS PlayerStats (
                ParticipantID INTEGER,
                ChampionName TEXT,
                Kills INTEGER,
                Deaths INTEGER,
                Assists INTEGER,
                TotalDamageDealtToChampions INTEGER,
                GoldEarned INTEGER,
                MatchID INTEGER,
                FOREIGN KEY (MatchID) REFERENCES MatchMetadata(MatchID)
            )
        """
        )

    def insert_match_metadata(self, metadata: MatchMetadata) -> None:
        for participant in metadata.participants:
            query = """INSERT INTO MatchMetadata (DataVersion, MatchID, Participant) 
                VALUES (?, ?, ?)"""
            self.cursor.execute(
                query, (metadata.data_version, metadata.match_id, participant)
            )
