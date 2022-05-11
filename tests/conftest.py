import anvil.server
import pytest


@pytest.fixture(scope="session", autouse=True)
def anvil_connection():
    anvil.server.connect("client-uplink-key", url="ws://app:3030/_/uplink")
