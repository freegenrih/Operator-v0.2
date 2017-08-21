import pymysql.cursors
from random import randint
import time
import datetime


def crt_users():
    '''
    create users
    '''
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='password',
                                     db='BigTester',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `IPSenderData` (`id`,`kay`,`ch1`, `ch2`,`ch3`,`ch4`,`ch5`,`ch6`,`ch7`,`ch8`,`datetimes`) " \
                  "VALUES (NULL,'2qwq',{},{},{},{},{},{},{},{},'{}')".format(randint(0, 1024), randint(0, 1024),
                                                                             randint(0, 1024),
                                                                             randint(0, 1024), randint(0, 1024),
                                                                             randint(0, 1024), randint(0, 1024),
                                                                             randint(0, 1024), datetime.datetime.now())
            cursor.execute(sql)

            print('Insert_datas')

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        connection.close()


i = 0

while True:
    kay = 'kjhasd'
    print('colum', i)
    crt_users()
    time.sleep(2)
    i += 1
