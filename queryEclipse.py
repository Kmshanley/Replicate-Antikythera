import sqlite3 as sq
from datetime import datetime, timedelta


def query(date):
    db = sq.connect("events.db")
    frmtStr = date.strftime("%Y %B %#d")
    sql = "SELECT * FROM Eclipses WHERE SolarEclipses = '" + frmtStr +"' OR LunarEclipses ='" + frmtStr +"'"
    result = db.execute(sql)
    for x in result:
        if x[0] == frmtStr:
            return ("Solar")
        elif x[1] == frmtStr:
            return ("Lunar")
    