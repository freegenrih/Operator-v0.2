import re
from sqlrw import (crt_users,
                   get_users,
                   up_del_users,
                   get_users_sign_in,
                   wraper_read,
                   wraper_write,
                   )
'''
Need to refactoring
1)Create validators(user, email, password and ....) instead (if if if if...... in def__init__)
'''

class RegUsersForm:
    def __init__(self, email: str, username: str, password: str, re_password: str, statusadmin: int):
        self.email = email
        self.username = username
        self.password = password
        self.re_password = re_password
        self.statusadmin = statusadmin
        self.error_forms = {}
        self.sql = "SELECT `email` FROM `Users` WHERE `email`='{}' ".format(self.email)

        # Need to refactoring
        if self.password != self.re_password \
                or re.match('<script', self.password) != None \
                or len(self.password) > 10 \
                or len(self.password) < 5:
            password_error = {'password': 'No confirm password'}
            self.error_forms.update(password_error)

        # Need to refactoring
        if len(self.username) < 4 \
                or len(self.username) > 15 \
                or re.search(r'[!?<:>/]', self.username) != None \
                or re.match(r'<script', self.username) != None:
            password_error = {
                'username': 'The length of the username must be at least 4 characters and not more than 15'}
            self.error_forms.update(password_error)

        # Need to refactoring
        if len(self.email) > 64 \
                or self.email.find('@') == -1 \
                or self.email.find('.') == -1 \
                or len(self.email) == 0 \
                or re.search(r'[!?<:>/]', self.email) != None \
                or re.match(r'<script', self.email) != None:
            password_error = {'email': 'No  correct email '}
            self.error_forms.update(password_error)

        if get_users(self.sql, self.email) == True:
            password_error = {
                'emailbd': 'Such an email is in the database'
            }
            self.error_forms.update(password_error)

    def write_users(self):
        '''Create users (write to DB)'''
        if len(self.error_forms) == 0:
            crt_users(self.username, self.email, self.password, self.statusadmin)

        else:
            pass

    def errors(self):
        '''Errors register user '''
        return self.error_forms


class UpdateUsersForm:
    def __init__(self, email: str, username: str, old_password: str, new_password: str, re_newpassword: str):
        self.email = email
        self.username = username
        self.old_password = old_password
        self.new_password = new_password
        self.re_newpassword = re_newpassword
        self.error_updates = {}
        self.sql = "UPDATE `Users`SET `password` = '{}' WHERE `Users`.`email` = '{}'" \
            .format(self.new_password, self.email)

        # Need to refactoring
        if self.new_password != self.re_newpassword \
                or re.match('<script', self.new_password) != None \
                or re.match('<script', self.re_newpassword) != None \
                or len(self.old_password) > 10 \
                or len(self.old_password) < 5:
            password_error = {'password': 'No confirm password'}
            self.error_updates.update(password_error)

        # Need to refactoring
        if len(self.username) < 4 \
                or len(self.username) > 15 \
                or re.search(r'[!?<:>/]', self.username) != None \
                or re.match(r'<script', self.username) != None:
            username_error = {
                'username': 'The length of the username must be at least 4 characters and not more than 15'}
            self.error_updates.update(username_error)

        # Need to refactoring
        if len(self.email) > 64 \
                or self.email.find('@') == -1 \
                or self.email.find('.') == -1 \
                or len(self.email) == 0 \
                or re.search(r'[!?<:>/]', self.email) != None \
                or re.match(r'<script', self.email) != None:
            email_error = {
                'email': 'No  correct email '}
            self.error_updates.update(email_error)

    def update_users(self):
        '''Update user'''
        if len(self.error_updates) == 0:
            up_del_users(self.sql)

        else:
            pass

    def errors_updates(self):
        '''Errors update user '''
        return self.error_updates


class DeleteUsersForm:
    def __init__(self, email: str, password: str, re_password: str):
        self.email = email
        self.password = password
        self.re_password = re_password
        self.error_delete = {}
        self.sql = "DELETE FROM `Users` WHERE `Users`.`email` = '{}'".format(self.email)

        # Need to refactoring
        if len(self.email) > 64 \
                or self.email.find('@') == -1 \
                or self.email.find('.') == -1 \
                or len(self.email) == 0 \
                or re.search(r'[!?<:>/]', self.email) != None \
                or re.match(r'<script', self.email) != None:
            email_error = {
                'email': 'No  correct email '}
            self.error_delete.update(email_error)

        # Need to refactoring
        if self.password != self.re_password \
                or re.match('<script', self.password) != None \
                or re.match('<script', self.re_password) != None \
                or len(self.password) > 10 \
                or len(self.password) < 5:
            password_error = {'password': 'No confirm password'}
            self.error_delete.update(password_error)

    def delete_users(self):
        '''Delete users of DB'''
        up_del_users(self.sql)

    def errors_delete(self):
        '''Erors deletes users'''
        return self.error_delete


class SignIn:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.error_sign_in = {}
        self.sql = "SELECT `password`, `email` FROM `Users` WHERE `email`='{}'".format(self.email)

        # Need to refactoring
        if len(self.email) > 64 \
                or self.email.find('@') == -1 \
                or self.email.find('.') == -1 \
                or len(self.email) == 0 \
                or re.search(r'[!?<:>/]', self.email) != None \
                or re.match(r'<script', self.email) != None:
            email_error = {
                'email': 'No  correct email '}
            self.error_sign_in.update(email_error)

        # Need to refactoring
        if re.match('<script', self.password) != None \
                or len(self.password) > 10 \
                or len(self.password) < 5:
            password_error = {'password': 'No confirm password'}
            self.error_sign_in.update(password_error)

    def validate(self):
        '''Validate users Sig IN page'''
        if get_users_sign_in(self.sql, self.password, self.email) == True:
            return True
        else:
            False

    def error_signin(self):
        '''Errors Sig In page'''
        return self.error_sign_in


class IPSenderRegDel:
    def __init__(self, name: str, key: str, password: str):
        self.name = name
        self.key = key
        self.password = password
        self.error_ipsender = {}
        self.sql_validate_password = "SELECT `password` FROM `Users` WHERE `password`='{}'".format(self.password)
        self.sql_create = "INSERT INTO `IPSender` (`name_ipsender`,`key_ipsender`) " \
                          "VALUES ('{}','{}')".format(str(self.name), str(self.key))

        self.sql_delete = "DELETE FROM `IPSender` WHERE `name_ipsender`='{}' AND `key_ipsender`='{}'" \
            .format(str(self.name), str(self.key))

        # Need to refactoring
        if re.match('<script', self.name) != None \
                or len(self.name) > 20 \
                or re.match(r'<script', self.name) != None \
                or len(self.name) < 5:
            name_error = {'name': 'Name IP i.O no confirm '}
            self.error_ipsender.update(name_error)


        # Need to refactoring
        if re.match('<script', self.key) != None \
                or len(self.key) > 20 \
                or re.match(r'<script', self.key) != None \
                or len(self.key) < 5:
            key_error = {'key': 'Key no confirm '}
            self.error_ipsender.update(key_error)

        # Need to refactoring
        if re.match('<script', self.password) != None \
                    or len(self.password) > 10 \
                    or re.match(r'<script', self.password) != None \
                    or len(self.password) < 5:
            password_error = {'password': 'No confirm password'}
            self.error_ipsender.update(password_error)

    def create_ipsender(self):
        '''Create IP Sender in DB'''
        validate_password = False
        for row in wraper_read(self.sql_validate_password):
            if row['password'] == self.password:
                validate_password = True
        if len(self.error_ipsender) == 0 and validate_password == True:
            return wraper_write(self.sql_create)
        else:
            password_error = {'password_BD': 'No confirm password DB'}
            self.error_ipsender.update(password_error)


    def delete_ipsender(self):
        '''Delete IP Sender of DB'''
        validate_password = False
        for row in wraper_read(self.sql_validate_password):
            if row['password'] == self.password:
                validate_password = True
        if len(self.error_ipsender) == 0 and validate_password == True:
            return wraper_write(self.sql_delete)
        else:
            password_error = {'password_BD': 'No confirm password DB'}
            self.error_ipsender.update(password_error)

    def get_errors_ipsender(self):
        '''Get all errors IP Sender'''
        return self.error_ipsender


class IPsenderGet:
    sql = "SELECT * FROM `IPSender`"

    def list_ipsender(self):
        ''' Get full list IP Sender of DB '''
        return wraper_read(self.sql)
