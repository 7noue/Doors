import {API_BASE} from '$lib/constants';

export async function createSession(userId: String) {
    const response = await fetch(`${API_BASE}/sessions/create?user_id=${userId}`, {
        method: "POST"
    });

    if (!response.ok){
        const errorDetail = await response.json();
        throw new Error(typeof errorDetail.detail === 'string' 
            ? errorDetail.detail 
            : JSON.stringify(errorDetail.detail));
    }

    return response.json();
}

export async function getRankings(sessionId:string) {
    const response = await fetch(`${API_BASE}/sessions/${sessionId}/ranking`);
    if (!response.ok) {
        throw new Error ("Could not fetch rankings");
    }
}
export async function submitChoice(userId: string, sessionId: string, winnerId: string) {
    // Matches: @app.post("/sessions/{user_id}/{session_id}/choose")
    // Note: winner_id is a query parameter in your FastAPI code
    const response = await fetch(`${API_BASE}/sessions/${userId}/${sessionId}/choose?winner_id=${winnerId}`, {
        method: 'POST'
    });
    if (!response.ok) throw new Error("Vote failed");
    return await response.json();
}

export async function getInitialMatchup(userId: string, sessionId: string) {
    // Matches: @app.get("/sessions/{user_id}/{session_id}/matchup")
    const response = await fetch(`${API_BASE}/sessions/${userId}/${sessionId}/matchup`);
    if (!response.ok) throw new Error("Matchup not found");
    return await response.json();
}

export async function getSession(userId: string, sessionId: string) {
    const response = await fetch(`${API_BASE}/sessions/${userId}/${sessionId}`);
    
    if (!response.ok) throw new Error("Session not found");
    return await response.json();
}