from pathlib import Path

user_id = "user_dev1"
session_id = "090909.json"
nested_dir_path = Path(f'stored_sessions/{user_id}')
nested_dir_path.mkdir(parents=True, exist_ok=True)

if nested_dir_path.exists():
    with open(f'{nested_dir_path}/{session_id}', "w") as f:
        f.write('Test')