import sqlite3
from sqlite3 import Connection

class DbConnectionHandler:
  def __init__(self) -> None:
    self.__conecction_string__ = "storage.db"
    self.__conn = None

  def connect(self) -> None:
    conn = sqlite3.connect(self.__conecction_string__, check_same_thread=False)
    self.__conn = conn

  def get_connection(self) -> Connection:
    return self.__conn
  
db_connection_handler = DbConnectionHandler()