from _pytest.fixtures import fixture

from main import app

@fixture()
def posts_keys():
    return {
        "poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"
    }



@fixture()
def client():
    return app.test_client()