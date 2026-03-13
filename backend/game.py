import json
import engine

with open('mock_tracks.json', 'r') as f:
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
    
try:
    session = engine.create_session(user_id=123, songs=song_pool)
    print(f"✅ Engine started! Session ID: {session.id}")
    while session.is_active:
        initialize_round = engine.generate_round_1_pairs(session.songs)
except ValueError as e:
    print(f"❌ {e}")
