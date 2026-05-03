from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_timeline():
    response = client.get("/api/timeline")
    assert response.status_code == 200
    data = response.json()
    assert "phases" in data
    assert len(data["phases"]) == 8

def test_quiz_get():
    response = client.get("/api/quiz")
    assert response.status_code == 200
    data = response.json()
    assert "questions" in data
    assert len(data["questions"]) == 7
    # Ensure correct index is NOT leaked
    assert "correct_index" not in data["questions"][0]

def test_quiz_submit_invalid():
    # Should 400 on mismatch answer count
    response = client.post("/api/quiz/submit", json={"answers": [1, 2]})
    assert response.status_code == 400

def test_quiz_submit_valid():
    # Submit 7 answers
    response = client.post("/api/quiz/submit", json={"answers": [1, 2, 0, 1, 0, 1, 0]})
    assert response.status_code == 200
    data = response.json()
    assert data["score"] == 7
    assert data["badge"] == "Champion"

def test_eligibility_underage():
    response = client.post("/api/eligibility/check", json={
        "is_citizen": True,
        "age": 16,
        "has_address_proof": True,
        "is_sound_mind": True,
        "not_disqualified": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["eligible"] == False
    assert len(data["reasons"]) > 0

def test_booth_invalid_pincode():
    response = client.get("/api/booth?pincode=123")
    assert response.status_code == 400

def test_booth_valid_pincode():
    response = client.get("/api/booth?pincode=110001")
    assert response.status_code == 200
    data = response.json()
    assert "embed_url" in data
    assert "110001" in data["embed_url"]
