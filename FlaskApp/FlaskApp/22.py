from sqlrw import wraper_write, wraper_read

sql="SELECT * FROM `dbo_users`;"

db ={'user':{'username':'gena', 'password':'123456', 'type_user':'admin'}}

psw = '1234562'
def check_base_in_users(psw):

    for key in db:
        if db[key]['password'] == psw:
            print("True")
        else:
            print("False")


if __name__=='__main__':
    for row in wraper_read(sql):
        if row['user_password'] == psw:
            print("name:",row['user_name'], " ", "type user:",row['user_type'])
        else:
            print('False')
