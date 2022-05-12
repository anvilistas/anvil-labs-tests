from anvil.tables import app_tables


def test_dummy(clean_db, uplink):
    app_tables.events.add_row(event_id=42, event_type="hello")
    rows = app_tables.events.search()
    assert len(rows) == 1
