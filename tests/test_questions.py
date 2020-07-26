def test_get_questions(client):
    response = client.get("/questions/")
    assert response.status_code == 200
    questions = response.json()["questions"]
    assert len(questions)
