import json
from pathlib import Path
from fastapi import FastAPI, HTTPException

from app import engine, manager
from app.services import load_session, save_session
from app import models as dt



app = FastAPI(title="Dizzy API")

@app.post("/sessions/create", response_model=dt.Session)
def create_game(user_id: str):
    try:
        session = manager.manage_session(user_id)
        return session
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/sessions/{user_id}/{session_id}/matchup")
def get_current_matchup(user_id: str, session_id: str):
    try:
        session = manager.locate_session(user_id=user_id, session_id=session_id)
        print("HEHEHEHEH")
        # winner_id = winner_obj_.id
        # return winner_id
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/sessions/{session_id}/choose")
def submit_vote(session_id: str, winner_id: str):
    try:
        engine.submit_choice(session_id, winner_id=winner_id)
        save_session(session=session_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get('/sessions/{session_id}/ranking')
def get_ranking(session_id: str):
    try:
    # print("🏆 Tournament Complete!")
        ranking = engine.get_ranking(session_id)
        return ranking 
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
