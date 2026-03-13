import data_structure as dt
from typing import List
import random

K = 32


# if song_list:
#         paired = generate_round_1_pairs(song_list)
#         paired = matchups(paired)

def create_session(user_id: str , songs: List[dt.Song]) -> dt.Session:
    if not songs or len(songs) < 2:
        raise ValueError("⛽ Engine Error: You need at least 2 songs to start a matchup!")

    if not user_id:
        raise ValueError("👤 Driver Error: No user_id provided.")
    
    return dt.Session(
        user_id=user_id,
        songs=songs,
        status=False
    )

def generate_round_1_pairs(songs):
    # 1. Shuffle
    shuffled = random.sample(songs, len(songs))
    
    # 2. Use zip for all the perfect pairs
    # This automatically ignores the last song if the length is odd
    paired = list(zip(shuffled[0::2], shuffled[1::2]))
    
    # 3. Handle the remainder
    if len(shuffled) % 2 != 0:
        last_song = shuffled[-1]
        # Pick anyone from the already paired songs as the opponent
        random_opponent = random.choice(shuffled[:-1])
        paired.append((last_song, random_opponent))
    
        
    return paired

def generate_round_2_pairs(songs):
    ...


def generate_round_3_pairs(songs):
    ...

def get_matchup_result(pair):
    print('CURRENT ROUND')
    """Handles exactly one matchup and returns the outcome."""
    print(f"\nSong [1]: {pair[0].title}")
    print(f"Song [2]: {pair[1].title}")

    choice = get_user_choice(2)

    if choice == 1:
        return pair[0], pair[1]
    else:
        return pair[1], pair[0]


# FOR MULTIPLE CHOICE
def get_user_choice(num_options):
    while True:
        try:
            # 1. Try to get and convert the input
            choice = int(input(f"Pick a song (1-{num_options}): "))
            
            # 2. Check if the number is actually in range
            if 1 <= choice <= num_options:
                return choice
            else:
                print(f"❌ Please enter a number between 1 and {num_options}.")
        except ValueError:
            # 3. This runs if int() fails (e.g., user typed "abc")
            print("⚠️ That's not a number! Try again.")
    

def update_elo(winner, loser):
    expected_winner = 1 / (1 + 10 ** ((loser.rating - winner.rating) / 400))
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
    #  mark complete, return final ranking
    #  save playlist
    session.is_active = False
    ...