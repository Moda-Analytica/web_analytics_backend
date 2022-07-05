from pytest import fixture


from starlette.testclient import TestClient
from starlette.config import environ

from app.main import app
from app.db.mongodb_utils import connect_to_mongo


@fixture(scope="session")
def test_client():
    from app.main import app
    with TestClient(app) as test_client:
        
        yield test_client

    

# This line would raise an error if we use it after 'settings' has been imported.
environ['TESTING'] = 'TRUE'
