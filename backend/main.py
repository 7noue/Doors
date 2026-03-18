import json
from pathlib import Path
from fastapi import FastAPI, HTTPException

from app import engine
from app.services import load_session, save_session
from app import models as dt


current_dir = Path(__file__).parent
json_path = current_dir / "tests" / "fixtures" / "mock_tracks.json"


with open(json_path, 'r') as f:
    raw_data = json.load(f)
    f.close()

song_pool = [
    engine.dt.Song (
        id = item['id'],
        title = item['name'],
        artist = item['artists'][0]['name']
    )
    for item in raw_data['tracks']
]


app = FastAPI(title="Dizzy API")
@app.post("/sessions/create", response_model=dt.Session)
def create_game(user_id: str, songs: dt.Song):
    try:
        session = engine.create_session(user_id=user_id, songs=song_pool)
        save_session(session=session, filepath=f"{session.id}-session_state.json")
        return 
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))

@app.get("/sessions/{session_id}/matchup")
def get_current_matchup(session_id: str):
    try:
        session_id = load_session(f"{session_id}-session_state.json")
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))

@app.post("/sessions/{session_id}/choose")
def submit_vote(session_id: str, winner_id: str):
    ...

@app.get('/sessions/{session.id}/ranking')
def get_ranking():
    ...
















































# try:

#     if Path("session_state.json").exists():
#         session = load_session("session_state.json")
#         print(f"Resuming Session: {session.id}")
#     else: 
#         session = engine.create_session(user_id="user_dev123", songs=song_pool)
#         print(f"✅ Engine started! Session ID: {session.id}")
#         engine.advance_round(session)

#     while session.is_active:
#         if session.current_matchup_index >= len(session.matchups):
#             engine.advance_round(session)
#             print(f'Current Round: {session.current_round}')
#             if not session.is_active: break

#         m = session.matchups[session.current_matchup_index]
#         winner_obj, _ = engine.get_matchup_result((m.song_a, m.song_b))

#         #Submit choice and Save
#         engine.submit_choice(session, winner_id=winner_obj.id)
#         save_session(session=session)

#     print("🏆 Tournament Complete!")
#     engine.get_ranking(session)

# except ValueError as e:
#     print(f"❌ {e}")
