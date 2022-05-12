import anvil.server
import pytest
from anvil.tables import app_tables

APP_URL = "ws://app:3030/_/uplink"


@pytest.fixture
def client_uplink():
    anvil.server.connect("client-uplink-key", url=APP_URL, quiet=True)


@pytest.fixture
def uplink():
    anvil.server.connect("uplink-key", url=APP_URL, quiet=True)


@pytest.fixture
def clean_db(uplink):
    tables = ("current", "events", "projections", "sequences")
    for table in tables:
        getattr(app_tables, table).delete_all_rows()
    yield
    anvil.server.disconnect()
