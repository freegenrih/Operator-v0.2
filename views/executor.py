from datetime import datetime

from sqlrw import wraper_write, wraper_read


class EngineerUpdate:
    def __init__(self, id_update_note, name_user):
        self.name_user = name_user
        self.id_update_note = id_update_note
        self.sql_update_note = "UPDATE `dbo_operator_application` " \
                               "SET `checked_engineer` = '1', `date_of_completion` = '{}', " \
                               "`name_engineer_completion` = '{}' " \
                               "WHERE `dbo_operator_application`.`id` = {}".format(str(datetime.now())[0:-7],
                                                                                   str(self.name_user),
                                                                                   int(self.id_update_note))

    def update_note(self):
        return wraper_write(self.sql_update_note)


class EngineerGet:
    def get_list_note(self):
        sql = "SELECT * FROM `dbo_operator_application` WHERE `checked_engineer`=0"
        return wraper_read(sql)


class OperatorCreate:
    def __init__(self, name_user: str, select_pult: str, number_object: str, select_operation: str, add_comment: str):
        self.name_user = name_user
        self.select_pult = select_pult
        self.namber_object = number_object
        self.select_operation = select_operation
        self.add_comment = add_comment
        self.sql_insert_note = "INSERT INTO `dbo_operator_application` " \
                               "(`id`, `date_of_creation`, `name_operator`, `name_pult`, `number_object`, `message`," \
                               "`checked_engineer`, `date_of_completion`, `name_engineer_completion`) " \
                               "VALUES (NULL, '{}', '{}', '{}', '{}', '{}',0, '', ' ');".format(
            str(datetime.now())[0:-7],
            str(self.name_user),
            str(self.select_pult),
            str(self.namber_object),
            str(self.select_operation)
            + ' ' + str(self.add_comment)
        )

    def create_note(self):
        return wraper_write(self.sql_insert_note)



class OperatorGet:
    def get_list_note(self):
        self.sql_get_list_note = "SELECT * FROM `dbo_operator_application` WHERE `checked_engineer`=0"
        return wraper_read(self.sql_get_list_note)

    def get_list_electritian_application(self):
        self.sql_get_list_electrician_application = "SELECT * FROM `dbo_electrician_application` " \
                                                    "WHERE `checked_electrician`=0"
        return wraper_read(self.sql_get_list_electrician_application)


class OperatorDel:
    def __init__(self, id: int):
        self.id = id
        self.sql_delete_note = "DELETE FROM `dbo_operator_application` " \
                               "WHERE `dbo_operator_application`.`id` = {};".format(int(self.id))

    def delete_note(self):
        return wraper_write(self.sql_delete_note)


class SettingsUsersRegUser:
    def __init__(self, user_name: str, user_password: str, user_type: str):
        self.user_name = user_name
        self.user_password = user_password
        self.user_type = user_type
        self.sql_reg_user = "INSERT INTO `dbo_users` (`id`, `date_register_user`, `user_name`, `user_password`, `user_type`) " \
                            "VALUES (NULL, '{}', '{}', '{}', '{}');".format(str(datetime.now())[0:-7],
                                                                            str(self.user_name),
                                                                            str(self.user_password),
                                                                            str(self.user_type)
                                                                            )

    def reg_user(self):
        return wraper_write(self.sql_reg_user)


class SettingsUsersDel:
    def __init__(self, id: int):
        self.id = id
        self.sql_delete_user = "DELETE FROM `dbo_users` WHERE `dbo_users`.`id` ={} ".format(int(self.id))
        self.sql_delete_user_type = "DELETE FROM `user_type` " \
                                    "WHERE `user_type`.`id` = {} ".format(int(self.id))

    def delete_users(self):
        return wraper_write(self.sql_delete_user)

    def delete_user_type(self):
        return wraper_write(self.sql_delete_user_type)


class SettingsUsersRegType:
    def __init__(self, name_type: str):
        self.name_type = name_type
        self.sql_reg_new_type_user = "INSERT INTO `user_type` (`id`, `user_type`) " \
                                     "VALUES (NULL, '{}')".format(str(self.name_type))

    def reg_new_type(self):
        return wraper_write(self.sql_reg_new_type_user)


class UsersGet:
    def __init__(self):
        self.sql_type_user = "SELECT * FROM `user_type`"
        self.sql_list_users = "SELECT * FROM `dbo_users`"

    def get_type_user(self):
        return wraper_read(self.sql_type_user)

    def get_list_user(self):
        return wraper_read(self.sql_list_users)
