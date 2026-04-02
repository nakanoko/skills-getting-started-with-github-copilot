"""
Test configuration and shared fixtures for the activity management system tests.
"""
import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """
    Fixture providing a TestClient for the FastAPI application.
    Resets activities before each test.
    """
    from src.app import app
    client = TestClient(app)
    client.post("/reset")  # Reset activities before each test
    return client


@pytest.fixture
def sample_activities():
    """
    Fixture providing sample activity data for testing.
    """
    return {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu"]
        }
    }