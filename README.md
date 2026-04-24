# ⚡ DIZZY
> **A Song Ranking Engine.**

DIZZY uses a Python-powered Elo rating algorithm to help users rank their music library or music category through a series of head-to-head matchups. Built with a "Double-Locked" session architecture for persistent, shareable game states.

---

## 🏗 System Architecture

The project is split into a **Reactive Frontend** and a **Stateful Backend**. They communicate via a REST API.



### 1. The Frontend (SvelteKit)
- **Framework:** SvelteKit (TypeScript)
- **Styling:** Tailwind CSS (Neobrutalist aesthetic: high contrast, 4px borders, hard shadows)
- **Routing:** Dynamic nested routes `[userId]/[sessionId]` to ensure page refreshes don't lose state.

### 2. The Backend (FastAPI)
- **Logic Engine:** Python + Pydantic (Strict data modeling)
- **Storage:** Local JSON File System (`stored_sessions/{user_id}/{session_id}.json`) 
- **Ranking:** Custom Elo Implementation (K-Factor: 32)

---

## 🚦 The Data Flow (Elo Logic)

1. **Initialize:** User enters a `userId`. Backend creates a `Session` object.
2. **Pairing:** Backend shuffles songs and generates Round 1 matchups.
3. **The Choice:** User picks Song A or Song B.
4. **The Update:** Backend calculates the new Elo ratings and increments the matchup index.



---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | SvelteKit | UI & Routing |
| **Backend** | FastAPI | API Endpoints |
| **Models** | Pydantic | Data Validation |
| **Logic** | Python | Elo Calculations |
| **Styles** | Tailwind | Neobrutalist UI |

---

## 📡 API Endpoints (The Handshake)

### Sessions
- `POST /sessions/create?user_id={id}`: Initializes a new session.
- `GET /sessions/{user_id}/{session_id}`: Retrieves the full session state.
- `GET /sessions/{user_id}/{session_id}/matchup`: Gets the current pair to be voted on.

### Gameplay
- `POST /sessions/{user_id}/{session_id}/choose?winner_id={id}`: Submits a vote and updates Elo.
- `GET /sessions/{user_id}/{session_id}/ranking`: Returns final leaderboard (Only available when `is_active: false`).

---

## 📂 Project Structure

```text
.
├── backend/                # Python FastAPI Logic
│   ├── app/
│   │   ├── engine.py       # Elo & Pairing logic
│   │   ├── manager.py      # Session persistence
│   │   └── models.py       # Pydantic Schemas (dt.Session, dt.Song)
│   ├── main.py             # API Entry point
│   └── stored_sessions/    # JSON Storage (Git ignored) TO PUT IN DATABASE
│
└── frontend/               # SvelteKit Application
    ├── src/
    │   ├── lib/
    │   │   ├── api.ts      # Fetch wrappers
    │   │   ├── types.ts    # TypeScript Interfaces (Matches Pydantic)
    │   │   └── components/ # UI (Matchup, SongRanking, etc.)
    │   └── routes/
    │       └── game/[userId]/[sessionId]/ # Dynamic Game Logic