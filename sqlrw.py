import pymysql.cursors

from Settings_app import config_db
'''
Need to refactoring
1) delete repeat foo()
--OK-- 2) create file settings connect DB 
'''


def list_users():
    '''read all users'''
    try:
        connection = pymysql.connect(**config_db, cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:

            sql = "SELECT * FROM `Users` "
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    finally:
        connection.close()


def crt_users(username, email, password, statusadmin):
    '''create users'''
    try:
        connection = pymysql.connect(**config_db, cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `Users` (`username`,`email`, `password`, `statusadmin`) " \
                  "VALUES ('{}','{}','{}','{}')".format(str(username), str(email), str(password), int(statusadmin))
            cursor.execute(sql)

            print('Create Users')

        connection.commit()
    finally:
        connection.close()


def get_users(sql, email):
    ''' checked users for email'''
    try:
        connection = pymysql.connect(**config_db, cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:

            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                if email in row['email']:
                    return True
                else:
                    return False
        connection.commit()

    finally:
        connection.close()


def up_del_users(sql):
    '''update users password and delete users '''
    try:
        connection = pymysql.connect(**config_db, cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Read a single record

            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()


def get_users_sign_in(sql, password, email):
    ''' checked users sign in'''
    try:
        connection = pymysql.connect(**config_db, cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:

            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                if row['password'] == password and row['email'] == email:
                    return True
                else:
                    return False

        connection.commit()

    finally:
        connection.close()


def wraper_read(sql):
    ''' wraper  read sql  '''
    try:
        connection = pymysql.connect(**config_db, cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Read a single record
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    finally:
        connection.close()


def wraper_write(sql):
    '''wraper write sql'''
    try:
        connection = pymysql.connect(**config_db, cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Create a new record
            cursor.execute(sql)

        connection.commit()
    finally:
        connection.close()


if __name__ == '__main__':
    sql = "DELETE FROM `IPSender` WHERE `name_ipsender`='lkjsdkflj' AND `key_ipsender`='lkjkldf' "
    wraper_write(sql)
