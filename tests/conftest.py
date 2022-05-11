import anvil.server
import pytest


@pytest.fixture(scope="session", autouse=True)
def anvil_connection():
    anvil.server.connect("12345")
