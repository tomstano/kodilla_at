# import json
# import pytest
#
# from unittest.mock import patch
# from kodilla.module_2_quiz_app_backend.backend.flaskr.models import Category, Question
#
#
# def test_question_list(setup_app, setup_test_api):
#     """Test that hitting the question list GET endpoint returns a list of question(s), as well as categories"""
#
#     science, geography, _, _ = setup_test_api
#     client = setup_app
#
#     third_question = Question("Why is science?", "Only Bill Nye knows", science.id, 5)
#     third_question.insert()
#     # Test list with pagination only returns 2 result
#     resp = client.get("/api/questions")
#     assert resp.status_code == 200
#     data = json.loads(resp.data)
#     assert "categories" in data
#     assert "questions" in data
#     assert "total_questions" in data
#     assert data == {
#         "categories": {"1": "Science", "2": "Geography"},
#         "questions": [
#             {
#                 "answer": "Nobody knows",
#                 "category": 1,
#                 "difficulty": 5,
#                 "id": 1,
#                 "question": "What is science?",
#             },
#             {
#                 "answer": "Probably not",
#                 "category": 2,
#                 "difficulty": 5,
#                 "id": 2,
#                 "question": "Is geography real?",
#             },
#         ],
#         "total_questions": 3,
#     }
#
#
# def test_question_by_category_404(setup_app):
#     """Test that a 404 is returned when a category id is not found"""
#
#     _, client = setup_app
#
#     resp = client.get(f"/api/categories/5000/questions")
#     assert resp.status_code == 404
#     assert json.loads(resp.data) == {
#         "error": "404: Not Found",
#         "message": "Category matching the provided ID was not found",
#     }
#
#
# def test_question_by_category(setup_app, setup_test_api):
#     """
#     Test that only questions for a given category will be returned when hitting the GET category questions endpoint.
#     """
#
#     science, _, _, _ = setup_test_api
#     client = setup_app
#
#     assert Category.query.count() == 2
#     cat = science
#     resp = client.get(f"/api/categories/{cat.id}/questions")
#     assert resp.status_code == 200
#     data = json.loads(resp.data)
#     assert "current_category" in data
#     assert data["current_category"] == cat.id
#     assert "questions" in data
#     assert data["questions"][0]["category"] == cat.id
#     # Check response shape
#     assert data == {
#         "current_category": 1,
#         "questions": [
#             {
#                 "answer": "Nobody knows",
#                 "category": 1,
#                 "difficulty": 5,
#                 "id": 1,
#                 "question": "What is science?",
#             }
#         ],
#         "total_questions": 1,
#     }
#
#
# def test_category_list(setup_app):
#     """Test that hitting the categories list GET endpoint returns a dictionary of supported categories"""
#
#     client = setup_app
#
#     resp = client.get("/api/categories")
#     assert resp.status_code == 200
#     data = json.loads(resp.data)
#     assert data == {"categories": {"1": "Science", "2": "Geography"}}
#
#
# def test_create_question_fields(setup_app):
#     """Test field validations on question create POST endpoint"""
#
#     client = setup_app
#
#     url = "/api/questions"
#     # Test missing fields
#     data = {}
#     resp = client.post(url, json=data)
#     assert resp.status_code == 400
#     assert json.loads(resp.data) == {
#         "error": "400: Bad Request",
#         "message": [
#             {"question": "Field is required"},
#             {"answer": "Field is required"},
#             {"difficulty": "Field is required"},
#             {"category": "Field is required"},
#         ],
#     }
#     data = {
#         "question": "Why is science?",
#         "answer": "Only Bill Nye knows",
#         "category": 5000,
#         "difficulty": 0,
#     }
#     # Test difficulty and cateory validation
#     resp = client.post(url, json=data)
#     assert resp.status_code == 400
#     assert json.loads(resp.data) == {
#         "error": "400: Bad Request",
#         "message": [
#             {"difficulty": "Difficulty must be an integer between 1 and 5"},
#             {"category": "Category is not supported"},
#         ],
#     }
#
#
# @patch("flaskr.api.views.Question.insert")
# def test_create_question_422(setup_app, setup_test_api, mock_insert):
#     """Test that a 422 error is returned when there is an error raised while processing question creation"""
#
#     science, _, _, _ = setup_test_api
#     client = setup_app
#
#     # Force raise an exeception while creating question in DB
#     mock_insert.side_effect = Exception
#     assert Question.query.count() == 2
#     data = {
#         "question": "Why is science?",
#         "answer": "Only Bill Nye knows",
#         "category": science.id,
#         "difficulty": 3,
#     }
#     resp = client.post("/api/questions", json=data)
#     assert resp.status_code == 422
#     assert json.loads(resp.data) == {
#         "error": "422: Unprocessable Entity",
#         "message": "The request was well-formed but was unable to be followed due to semantic errors.",
#     }
#     # Ensure changes dont persist
#     assert Question.query.count() == 2
#
#
# def test_create(setup_app, setup_test_api):
#     """Test successful creation of a question"""
#
#     science, _, _, _ = setup_test_api
#     app, client = setup_app
#
#     assert Question.query.count() == 2
#     data = {
#         "question": "Why is science?",
#         "answer": "Only Bill Nye knows",
#         "category": science.id,
#         "difficulty": 3,
#     }
#     resp = client.post("/api/questions", json=data)
#     assert resp.status_code == 200
#     resp_data = json.loads(resp.data)
#     assert resp_data == {
#         "answer": "Only Bill Nye knows",
#         "category": 1,
#         "difficulty": 3,
#         "id": 3,
#         "question": "Why is science?",
#     }
#     # Ensure changes persist in DB
#     assert Question.query.count() == 3
#     question = Question.query.get(resp_data["id"])
#     assert question is not None
#     assert question.format() == resp_data
#
#
# def test_delete_question_404(setup_app):
#     """Test the trying to delete a non-existent question id returns a 404"""
#
#     client = setup_app
#
#     resp = client.delete("/api/questions/5000")
#     assert resp.status_code == 404
#     assert json.loads(resp.data) == {
#         "error": "404: Not Found",
#         "message": "Question matching the provided ID was not found for delete",
#     }
#
#
# @patch("flaskr.api.views.Question.delete")
# def test_delete_question_500(mock_delete, setup_app, setup_test_api):
#     """Test that a 500 error is returned when there is an error raised while processing question deletion"""
#
#     _, _, _, geog_question = setup_test_api
#     client = setup_app
#
#     # Force raise an exeception while deleting question in DB
#     mock_delete.side_effect = Exception
#     assert Question.query.count() == 2
#     resp = client.delete(f"/api/questions/{geog_question.id}")
#     assert resp.status_code == 500
#     assert json.loads(resp.data) == {
#         "error": "500: Internal Server Error",
#         "message": "The server encountered an internal error and was unable to complete your request. "
#         "Either the server is overloaded or there is an error in the application.",
#     }
#     # Ensure delete does not persist in DB
#     assert Question.query.count() == 2
#
#
# def test_delete_question(setup_app, setup_test_api):
#     """Test question deletion response and persists in the database"""
#
#     _, _, _, geog_question = setup_test_api
#     client = setup_app
#
#     assert Question.query.count() == 2
#     resp = client.delete(f"/api/questions/{geog_question.id}")
#     assert resp.status_code == 204
#     # Ensure changes persist in DB
#     assert Question.query.count() == 1
#     assert Question.query.get(geog_question.id) is None
#
#
# @pytest.mark.parametrize(
#     "test_json_single_answer, test_json_multiple_answer",
#     [
#         {
#             "questions": [
#                 {
#                     "answer": "Nobody knows",
#                     "category": 1,
#                     "difficulty": 5,
#                     "id": 1,
#                     "question": "What is science?",
#                 }
#             ],
#             "total_questions": 1,
#         },
#         {
#             "questions": [
#                 {
#                     "answer": "Nobody knows",
#                     "category": 1,
#                     "difficulty": 5,
#                     "id": 1,
#                     "question": "What is science?",
#                 },
#                 {
#                     "answer": "Only Bill Nye knows",
#                     "category": 1,
#                     "difficulty": 5,
#                     "id": 3,
#                     "question": "Why is science?",
#                 },
#             ],
#             "total_questions": 2,
#         },
#     ],
# )
# def test_search(
#     setup_app, setup_test_api, test_json_single_answer, test_json_multiple_answer
# ):
#     """
#     Test that question search can search by:
#         - partial category match
#         - partial question match
#         - partial answer match
#         - Specify a category search under
#     """
#
#     science, _, _, _ = setup_test_api
#     client = setup_app
#
#     url = "/api/questions/search"
#     search = {"searchTerm": "sci"}
#     # test category contains
#     resp = client.post(url, json=search)
#     assert resp.status_code == 200
#     assert json.loads(resp.data) == test_json_single_answer
#     # Test question contains
#     search["searchTerm"] = "what is"
#     resp = client.post(url, json=search)
#     assert resp.status_code == 200
#     assert json.loads(resp.data) == test_json_single_answer
#     # Test answer contains
#     search["searchTerm"] = "nobody"
#     resp = client.post(url, json=search)
#     assert resp.status_code == 200
#     assert json.loads(resp.data) == test_json_single_answer
#     # test within category
#     new_question = Question("Why is science?", "Only Bill Nye knows", science.id, 5)
#     new_question.insert()
#     search["categoryId"] = science.id
#     search["searchTerm"] = "knows"
#     resp = client.post(url, json=search)
#     assert resp.status_code == 200
#     assert json.loads(resp.data) == test_json_multiple_answer
#
#
# def test_quiz_question_categorized(setup_app, setup_test_api):
#     """Test get random quiz question from specific category"""
#
#     science, _, _, _ = setup_test_api
#     client = setup_app
#
#     url = "/api/quizzes"
#     previous_questions = []
#     data = {"previous_questions": previous_questions, "quiz_category": science.id}
#     # There is only 1 possible question in the science category
#     resp = client.post(url, json=data)
#     assert resp.status_code == 200
#     resp_data = json.loads(resp.data)
#     assert resp_data == {
#         "question": {
#             "answer": "Nobody knows",
#             "category": 1,
#             "difficulty": 5,
#             "id": 1,
#             "question": "What is science?",
#         }
#     }
#     # Get depleted  questions
#     previous_questions.append(resp_data["question"]["id"])
#     data["previous_questions"] = previous_questions
#     resp = client.post(url, json=data)
#     assert resp.status_code == 200
#     resp_data = json.loads(resp.data)
#     assert resp_data["question"] is None
#
#
# def test_quiz_question_uncategorized(setup_app):
#     """Test get random quiz question from any category"""
#
#     client = setup_app
#
#     url = "/api/quizzes"
#     previous_questions = []
#     data = {"previous_questions": previous_questions}
#     resp = client.post(url, json=data)
#     assert resp.status_code == 200
#     resp_data = json.loads(resp.data)
#     # Check response for question that was returned
#     assert "question" in resp_data
#     assert "id" in resp_data["question"]
#     question1 = Question.query.get(resp_data["question"]["id"])
#     assert question1 is not None
#     assert resp_data["question"] == question1.format()
#     # Get next question
#     previous_questions.append(question1.id)
#     data["previous_questions"] = previous_questions
#     resp = client.post(url, json=data)
#     assert resp.status_code == 200
#     resp_data = json.loads(resp.data)
#     question2 = Question.query.get(resp_data["question"]["id"])
#     assert question2 is not None
#     assert question2.id not in previous_questions
#     # Get depleted questions
#     previous_questions.append(question2.id)
#     data["previous_questions"] = previous_questions
#     resp = client.post(url, json=data)
#     assert resp.status_code == 200
#     resp_data = json.loads(resp.data)
#     assert resp_data["question"] is None
