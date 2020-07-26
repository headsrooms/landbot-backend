def test_get_questions(client, random_questions):
    response = client.get("/questions/")
    assert response.status_code == 200
    questions_response = response.json()["questions"]
    assert len(questions_response)

    questions_response_user_ids = [
        question["user_id"] for question in questions_response
    ]
    random_questions_user_ids = [
        str(question["user_id"]) for question in random_questions
    ]
    assert not len(set(questions_response_user_ids) - set(random_questions_user_ids))


def test_get_question_after_posting(client, post_question):
    payload, question = post_question
    response = client.get(f"/questions/{question['id']}")
    assert response.status_code == 200
    response = response.json()
    assert payload["question"] == response["text"]
