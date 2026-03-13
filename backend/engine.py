import uuid
import json
import data_structure as dt
from typing import List

K = 32

def create_session(user_id: str , songs: List[dt.Song] = None) -> dt.Session:
    song_list = songs if songs else []
    return dt.Session(user_id=user_id, songs=song_list)

def generate_round_1_pairs(songs):
    ...


def generate_round_2_pairs(songs):
    ...


def generate_round_3_pairs(songs):
    ...


def update_elo(winner, loser):
    expected_winner = 1 / (1 + 10^((loser.rating - winner.rating) / 400))
    expected_loser = 1 - expected_winner

    winner.rating = winner.rating + K * (1 - expected_winner)
    loser.rating = loser.rating + K * (0 - expected_loser)

    return winner, loser


def submit_choice(session, matchup_id, winner_id):
    ...


def advance_round(session):
    ...


def get_ranking(session):
    ...


def end_session(session):
    ...


if __name__ == "__main__":
    with open('mock_tracks.json', 'r') as f:
        raw_data = json.load(f)
        f.close()

    song_pool = [
        dt.Song (
            id = item['id'],
            title = item['name'],
            artist = item['artists'][0]['name']
        )
        for item in raw_data['tracks']
    ]
        

    test = create_session(user_id=12312312, songs=song_pool)
    print(f'Session ID: {test.id}')
    titles = [s.title for s in test.songs]
    print(f'Song pool: {titles}')
