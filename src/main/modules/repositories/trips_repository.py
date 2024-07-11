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
  
  def find_trip_by_id(self, trip_id: str) -> tuple:
    cursor = self.__conn.cursor()
    cursor.execute(
      ''' SELECT * FROM trips WHERE id = ? ''', (trip_id,)
    )
    trip = cursor.fetchall()
    return trip
  
  def update_trip_status(self, trip_id: str) -> None:
    cursor = self.__conn.cursor()
    cursor.execute(
        '''
            UPDATE trips
                SET status = 1
            WHERE 
                id = ?
        ''', (trip_id,)
      )
    self.__conn.commit()