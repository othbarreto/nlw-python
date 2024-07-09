from sqlite3 import Connection

class TripsRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn
  
  def create_trip(self, trips_info: dict) -> None:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
          INSERT INTO trips
              (id, destination,start_date, end_date, owner_name, owner_email)
          VALUES
              (?,?,?,?,?,?)
      ''', (
        trips_info["id"],
        trips_info["destination"],
        trips_info["start_date"],
        trips_info["end_date"],
        trips_info["owner_name"],
        trips_info["owner_email"],
      )
    )
    self.__conn.commit()