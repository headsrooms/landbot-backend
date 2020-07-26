def test_get_users(client, random_users):
    users_db, users = random_users
    response = client.get("/users/")
    assert response.status_code == 200
    users_response = response.json()["users"]
    assert len(users)

    users_response_emails = [user["email"] for user in users_response]
    random_users_emails = [user["email"] for user in users]
    assert not len(set(users_response_emails) - set(random_users_emails))


def test_get_user_after_posting_question(client, post_question):
    payload, question = post_question
    response = client.get(f"/users/{question['user_id']}")
    assert response.status_code == 200
    response = response.json()
    assert payload["email"] == response["email"]
    assert payload["phone"] == response["phone"]
