import influxdb

class DBAdapter:

  def openDB(self):
    self.Db = influxdb.DataFrameClient(database="raw", host="localhost:8086")
    return self.Db

  def getValueFromDB(self):
    return self.Db.query("test")

