import pytest

from kodilla.module_2_quiz_app_backend.backend.flaskr import create_app
from kodilla.module_2_quiz_app_backend.backend.config import TestConfig
from kodilla.module_2_quiz_app_backend.backend.flaskr.models import Category, Question, db, setup_db


@pytest.fixture
def setup_app():
    app = create_app(TestConfig)
    client = app.test_client()
    app_context = app.app_context()
    app_context.push()
    db.drop_all()
    setup_db()

    def teardown_app():
        db.session.remove()
        db.drop_all()
        app_context.pop()

    yield client

    teardown_app()


@pytest.fixture
def setup_test_api():
    # Add some categories
    science = Category("Science")
    geography = Category("Geography")
    db.session.add(science)
    db.session.add(geography)
    db.session.commit()
    # Add some questions
    science_question = Question("What is science?", "Nobody knows", science.id, 5)
    geog_question = Question("Is geography real?", "Probably not", geography.id, 5)
    science_question.insert()
    geog_question.insert()
    yield science, geography, science_question, geog_question
