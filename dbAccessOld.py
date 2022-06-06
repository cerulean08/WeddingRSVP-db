#! C:\xampp\python\python.exe

import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
from sqlite3 import connect
from sqlite3 import IntegrityError
db = "guests.db"


def getInvitee(email):
    try:
        logging.error(email)
        conn = connect(db)
        cursor = conn.cursor()
        sql = f"SELECT guestsnm, id, party FROM invitees WHERE email = '{email}'"
        #  sql = "select guestsnm, id, party from invitees"
        logging.error(sql)
        cursor.execute(sql)
        row = cursor.fetchone()
        logging.error(row)
        conn.close()
        if row != None:
            return row[0], row[1], row[2]
        else:
            return None, None, None
        #  return row
    except Exception as ex:
        raise ex


def addGuest(fname, lname, email, food):
    #  not using this anymore
    try:
        conn = connect(db)
        cursor = conn.cursor()
        sql = f"INSERT INTO demographics VALUES('{fname}', '{lname}', '{email}', '{food}')"
        cursor.execute(sql)
        conn.commit()
        conn.close()
    except Exception as ex:
        raise ex


def addNewGuest(inviteeId, fname, lname, email, food):
    try:
        conn = connect(db)
        cursor = conn.cursor()
        sql = f"INSERT INTO guests (inviteeId, fname, lname, email, foodoption) " \
              f"VALUES('{inviteeId}', '{fname}', '{lname}', '{email}', '{food}')"
        logging.error(sql)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return 0
    except IntegrityError as ex:
        return 1
    except Exception as ex:
        raise ex


def calcTotalGuests():
    try:
        conn = connect(db)
        cursor = conn.cursor()
        sql = f"SELECT COUNT(*) FROM demographics"
        cursor.execute(sql)
        totalGuests = cursor.fetchall()
        conn.close()
        return totalGuests
    except Exception as ex:
        raise ex


def calcFood():
    try:
        conn = connect(db)
        cursor = conn.cursor()
        cursor.execute(f"select f.foodoption, f.cost, c.numguests, f.cost * c.numguests AS total from foods f "
                       f"LEFT JOIN "
                       f"(SELECT foodoption, COUNT(foodoption) AS numguests FROM guests GROUP BY foodoption) c "
                       f"ON f.foodoption = c.foodoption")
        totalFood = cursor.fetchall()
        conn.close()
        return totalFood
        '''for i in f:
            cursor.execute(f"SELECT COUNT(*) FROM demographics WHERE food='{i}'")
            count = cursor.fetchall()
            cursor.execute(f"UPDATE food SET count = '{count}' WHERE foodoption='{i}'")
            conn.commit()
            cursor.execute(f"SELECT cost FROM food WHERE foodoption='{i}'")
            # cursor.execute(f"SELECT food, count() as count from demographics GROUP BY food
            cost = cursor.fetchall()
            cursor.execute(f"UPDATE food SET totals = count * '{cost}' WHERE foodoption='{i}'")
            conn.commit()
        conn.close()'''
    except Exception as ex:
        raise ex


def getAllowed(inviteeId):
    try:
        conn = connect(db)
        cursor = conn.cursor()
        cursor.execute(f"select count(g.inviteeId) as rsvp, i.party "
                       f"from invitees i LEFT JOIN guests g "
                       f"ON g.inviteeId = i.id "
                       f"WHERE i.id = {inviteeId} "
                       f"group by g.inviteeId")
        allowedGuests = cursor.fetchone()
        conn.close()
        rsvp = allowedGuests[0]
        party = allowedGuests[1]
        return rsvp, party
    except Exception as ex:
        raise ex
