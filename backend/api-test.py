import requests as req

BASE_URL = "http://127.0.0.1:8000"
USER_ID = "test_user_1"

resp = req.post(f"{BASE_URL}/sessions/create?user_id={USER_ID}")

if resp.status_code != 200:
    print(f"Error {resp.status_code}: {resp.text}")
    exit()

session = resp.json()

s_id = session['id']
print(f"Created session: {s_id}")


round_num = 0
match_index = 0
# 2. Play 3 Rounds
# for i in range(3):
#     # Get Matchup
#     match = req.get(f"{BASE_URL}/sessions/{USER_ID}/{s_id}/matchup").json()

#     song_a = match['song_a']['id']
#     song_b = match['song_b']['id']

#     print(f"Round {round_num}: {match['song_a']['title']} vs {match['song_b']['title']}")
#     # Vote for Song A every time just to test
#     vote = req.post(f"{BASE_URL}/sessions/{USER_ID}/{s_id}/choose?winner_id={song_a}")
#     if vote.status_code == 200:
#         track = vote.json()
#         print(f"New Match Index: {track['current_matchup_index']}")
#         print(f"Current Round: {track['current_round']}")
#     else:
#         print(f"Error: {vote.text}")

# # 3. Check Ranking
# ranking = req.get(f"{BASE_URL}/sessions/{USER_ID}/{s_id}/ranking")
# print("Final Rankings:", ranking.json())

check_ranking = req.get(f'{BASE_URL}/sessions/{USER_ID}/{s_id}/ranking')
if check_ranking.status_code == 200:
    ranking = check_ranking.json()
    print(ranking)
else:
    print(check_ranking.text)