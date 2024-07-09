from .trips_repository import TripsRepository
from src.main.modules.settings.db_connection_handler import db_connection_handler
import uuid
from datetime import datetime, timedelta

db_connection_handler.connect()

def test_create_trip():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trips_info = {
    "id": str(uuid.uuid4()),
    "destination": "São Paulo",
    "start_date": datetime.strptime("09-07-2024", "%d-%m-%Y"),
    "end_date": datetime.strptime("09-07-2024", "%d-%m-%Y") + timedelta(days=5),
    "owner_name": "Thiago",
    "owner_email": "thiago@thiago.com"
  }

  trips_repository.create_trip(trips_info)