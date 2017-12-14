# тут пипец что начало твориться такой Быдлокодище Июня что повеситься можно :)
from datetime import datetime

from sqlrw import wraper_write, wraper_read


# ----------------------------------------Операторская часть-----------------------------------------------

class OperatorGet:
    def __init__(self, start_date=None, end_date=None, search_date=None):
        self.start_date = start_date
        self.end_date = end_date
        self.search_date = search_date

        self.sql_read_date_search_no_tests = "SELECT `data_search_no_tests` FROM `dbo_settings`"

        self.sql_get_list_note = "SELECT * FROM `dbo_operator_application` WHERE `checked_engineer`=0"

        self.sql_get_list_electrician_application = "SELECT * FROM `dbo_electrician_application` " \
                                                    "WHERE `checked_electrician`=0"

        self.sql_list_no_tests = "SELECT * FROM `dbo_no_tests` " \
                                 "WHERE `date_no_test` " \
                                 "LIKE'{}'".format(str(datetime.now())[0:-16] + '%')

        self.sql_list_no_tests_search_date = "SELECT * FROM `dbo_no_tests` " \
                                             "WHERE `date_no_test` " \
                                             "LIKE'{}'".format(self.read_date_search_in_db() + '%')

    def counter_no_test(self):
        pass

    def read_date_search_in_db(self):
        return wraper_read(self.sql_read_date_search_no_tests)[0]['data_search_no_tests']

    def get_list_note(self):
        return wraper_read(self.sql_get_list_note)

    def get_list_electritian_application(self):
        return wraper_read(self.sql_get_list_electrician_application)

    def get_list_no_tests_now(self):
        return wraper_read(self.sql_list_no_tests)

    def get_list_no_test_search_date(self):
        self.read_date_search_in_db()
        return wraper_read(self.sql_list_no_tests_search_date)  # доделать


class OperatorConfig:
    def __init__(self, date_save=None):
        self.date_save = str(date_save)
        self.sql_write_date_search_no_tests = "UPDATE `dbo_settings` SET `data_search_no_tests` = '{}' " \
                                              "WHERE `dbo_settings`.`id` = 1;".format(self.date_save)

    def write_date_search_no_test(self):
        return wraper_write(self.sql_write_date_search_no_tests)


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
            str(self.select_operation) + ' ' + str(self.add_comment)
        )

    def create_note(self):
        return wraper_write(self.sql_insert_note)


class OperatorCreateNoTests:
    def __init__(self, object_number, name_operator, why_there_is_no_test):
        self.object_number = object_number
        self.name_operator = name_operator
        self.why_there_is_no_test = why_there_is_no_test
        self.sql_create_no_test_note = "INSERT INTO `dbo_no_tests` (" \
                                       "`id`, `date_no_test`, `object_number`, " \
                                       "`name_operator`, `why_there_is_no_test`) " \
                                       "VALUES (NULL, '{}', '{}', '{}', '{}');" \
            .format(
            str(datetime.now())[0:-15],
            str(self.object_number),
            str(self.name_operator),
            str(self.why_there_is_no_test)
        )

    def create_note_no_test(self):
        return wraper_write(self.sql_create_no_test_note)


class OperatorDel:
    def __init__(self, id: int):
        self.id = id
        self.sql_delete_note = "DELETE FROM `dbo_operator_application` " \
                               "WHERE `dbo_operator_application`.`id` = {};".format(int(self.id))

        self.sql_delete_note_electrician = "DELETE FROM `dbo_electrician_application` " \
                                           "WHERE `dbo_electrician_application`.`id` = {};".format(int(self.id))

        self.sql_delete_note_no_tests = "DELETE FROM `dbo_no_tests` WHERE `dbo_no_tests`.`id` = {};".format(
            int(self.id))

    def delete_note(self):
        return wraper_write(self.sql_delete_note)

    def delete_note_electrician(self):
        return wraper_write(self.sql_delete_note_electrician)

    def delete_note_no_tests(self):
        return wraper_write(self.sql_delete_note_no_tests)


# ---------------------------------------------------------------------------------------------------------

class UsersGet:
    def __init__(self):
        self.sql_type_user = "SELECT * FROM `user_type`"
        self.sql_list_users = "SELECT * FROM `dbo_users`"

        self.sql_get_application_pc = "SELECT * FROM `dbo_user_application_pc` " \
                                      "WHERE `dbo_user_application_pc`.`checked_engineer` = 0;"

    def get_application_pc(self):
        return wraper_read(self.sql_get_application_pc)

    def get_type_user(self):
        return wraper_read(self.sql_type_user)

    def get_list_user(self):
        return wraper_read(self.sql_list_users)


# -------------------------------------------Юзер часть----------------------------------------------------
class UsersDel:
    def __init__(self, id: int):
        self.id = id
        self.sql_delete_application_pc = "DELETE FROM `dbo_user_application_pc` " \
                                         "WHERE `dbo_user_application_pc`.`id` = {};".format(int(self.id))

    def delete_application_pc(self):
        return wraper_write(self.sql_delete_application_pc)


class UsersCreate:
    def __init__(self, name_user: str, message: str):
        self.name_user = name_user
        self.message = message
        self.sql_create_application_pc = "INSERT INTO `dbo_user_application_pc` " \
                                         "(`id`, `date_of_creation`, `name_user_creation_app`, `message`, " \
                                         "`checked_engineer`, `date_of_completion`,`name_engineer_completion`," \
                                         "`commit_of_close_applocation_pc`) " \
                                         "VALUES (NULL, '{}', '{}', '{}', '0', ' ', ' ',' ');" \
            .format(
            str(datetime.now())[0:-7],
            self.name_user,
            self.message
        )

    def create_application_pc(self):
        return wraper_write(self.sql_create_application_pc)


# работа с оперативными карточками
class OperMap:
    def __init__(self, username=None, message_text=None, link_file=None, object_number=None, id=None):
        self.id = id
        self.username = str(username)
        self.message_text = str(message_text)
        self.link_file = str(link_file)
        self.object_number = object_number

        self.sql_get_oper_map = "SELECT * FROM `dbo_application_map_for_pult` WHERE `dbo_application_map_for_pult`.`checked_engineer`=0 ;"

        self.sql_detete = "DELETE FROM `dbo_application_map_for_pult` WHERE `dbo_application_map_for_pult`.`id` = {};".format(
            self.id)

        self.sql_write_oper_map = "INSERT INTO `dbo_application_map_for_pult` (" \
                                  "`id`, " \
                                  "`date_of_creation`, " \
                                  "`username_create`, " \
                                  "`object_number`, " \
                                  "`checked_engineer`, " \
                                  "`link_file`, " \
                                  "`date_of_completion`, " \
                                  "`name_engineer_completion`, " \
                                  "`message`) " \
                                  "VALUES (NULL, '{}', '{}', '{}', '0', '{}', '', '', '{}');".format(
            str(datetime.now())[0:-7],
            self.username,
            self.object_number,
            self.link_file,
            self.message_text
        )

        self.sql_update_oper_map = "UPDATE `dbo_application_map_for_pult` " \
                                   "SET `checked_engineer` = '1', `name_engineer_completion` = '{}'," \
                                   "`date_of_completion` = '{}'" \
                                   "WHERE `dbo_application_map_for_pult`.`id` = {};".format(
            self.username,
            str(datetime.now())[0:-7],
            self.id,
        )

    def get_map(self):
        return wraper_read(self.sql_get_oper_map)

    def create_map(self):
        return wraper_write(self.sql_write_oper_map)

    def update_map(self):
        return wraper_write(self.sql_update_oper_map)

    def delete_map(self):
        return wraper_write(self.sql_detete)

# месячный отчет по нетестируемым объектам
class ObjectsNoTests:
    def __init__(self, id=None, username=None,  link_file=None, month_number=None):
        self.id = id
        self.month_number = month_number
        self.username = str(username)
        self.link_file = str(link_file)

        self.sql_get_report_no_tests_object = "SELECT * FROM `dbo_reports_no_tets_objects`" \
                                          "WHERE `dbo_reports_no_tets_objects`.`checked_user` = 0;"

        self.sql_create_report_no_test_object = "INSERT INTO `dbo_reports_no_tets_objects` (`id`, `date_of_creation`, `username_create`, `for_what_month`, `link_file`, `checked_user`, `date_of_completion`, `username_completion`) " \
                                            "VALUES (NULL, '{}', '{}', '{}', '{}', '0',' ',' ' );".format(
            str(datetime.now())[0:-7],
            self.username,
            self.month_number,
            self.link_file
        )


        self.sql_update_report_no_test_object = "UPDATE `dbo_reports_no_tets_objects` " \
                                             "SET `checked_user` = '1',`date_of_completion`='{}',`username_completion` = '{}'" \
                                             "WHERE `dbo_reports_no_tets_objects`.`id` = {};".format(

            str(datetime.now())[0:-7],
            self.username,
            self.id,
        )


        self.sql_delete_report_no_test_object = "DELETE FROM `dbo_reports_no_tets_objects` " \
                                             "WHERE `dbo_reports_no_tets_objects`.`id` = {};".format(self.id)

    def get_report_no_tests_objects(self):
        return wraper_read(self.sql_get_report_no_tests_object)

    def create_report_no_test_objects(self):
        return wraper_write(self.sql_create_report_no_test_object)

    def update_report_no_test_objects(self):
        return wraper_write(self.sql_update_report_no_test_object)

    def delete_report_no_test_objects(self):
        return wraper_write(self.sql_delete_report_no_test_object)

# обновление данных ХО на объектах
class UpdateObjectsData:
    def __init__(self, id=None, username=None, object_number=None, name_object=None, address_object=None, message_object=None):
        self.id = id
        self.username = username
        self.object_number = object_number
        self.name_object = name_object
        self.address_object = address_object
        self.message_object = message_object

        self.sql_get_object_datas ="SELECT * FROM `dbo_application_update_users_objects` WHERE `checked_engineer` = '0';"

        self.sql_create_object_datas ="INSERT INTO `dbo_application_update_users_objects` (" \
                                      "`id`, `date_of_creation`, `username_creation`, `object_number`, `name_object`," \
                                      " `address_object`, `message_object`, `checked_engineer`, `date_of_completion`, " \
                                      "`name_engineer_completion`) " \
                                      "VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}', '0', '', '');".format(
            str(datetime.now())[0:-7],
            self.username,
            self.object_number,
            self.name_object,
            self.address_object,
            self.message_object
        )

        self.sql_update_object_datas ="UPDATE `dbo_application_update_users_objects` SET `checked_engineer` = '1'," \
                                      "`date_of_completion` = '{}',`name_engineer_completion` = '{}' " \
                                      "WHERE `dbo_application_update_users_objects`.`id` = {};".format(

            str(datetime.now())[0:-7],
            self.username,
            self.id
        )


        self.sql_delete_object_datas ="DELETE FROM `dbo_application_update_users_objects` " \
                                      "WHERE `dbo_application_update_users_objects`.`id` = {};".format(self.id)


    def get_object_data(self):
        return wraper_read(self.sql_get_object_datas)

    def create_object_data(self):
        return wraper_write(self.sql_create_object_datas)

    def update_object_data(self):
        return wraper_write(self.sql_update_object_datas)

    def delete_object_data(self):
        return wraper_write(self.sql_delete_object_datas)

# ---------------------------------------------------------------------------------------------------------


# -----------------------------------------Инженерная часть------------------------------------------------

class EngineerUpdate:
    def __init__(self, id_update_note, name_user, comment=None):
        self.id_update_note = id_update_note
        self.name_user = name_user
        self.comment = comment
        self.sql_update_note = "UPDATE `dbo_operator_application` " \
                               "SET `checked_engineer` = '1', `date_of_completion` = '{}', " \
                               "`name_engineer_completion` = '{}' " \
                               "WHERE `dbo_operator_application`.`id` = {}".format(str(datetime.now())[0:-7],
                                                                                   str(self.name_user),
                                                                                   int(self.id_update_note))
        self.sql_update_application_pc = "UPDATE `dbo_user_application_pc` " \
                                         "SET `checked_engineer` = '1', `date_of_completion` = '{}', " \
                                         "`name_engineer_completion` = '{}', `commit_of_close_applocation_pc` = '{}' " \
                                         "WHERE `dbo_user_application_pc`.`id` = {}".format(str(datetime.now())[0:-7],
                                                                                            str(self.name_user),
                                                                                            str(self.comment),
                                                                                            int(self.id_update_note))

    def update_note(self):
        return wraper_write(self.sql_update_note)

    def update_application_pc(self):
        return wraper_write(self.sql_update_application_pc)


class EngineerGet:
    def get_list_note(self):
        sql = "SELECT * FROM `dbo_operator_application` WHERE `checked_engineer`=0"
        return wraper_read(sql)
# заявки сисадмину
    def get_count_application_pc_no_checed(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_user_application_pc` WHERE `checked_engineer`=0;"
        return wraper_read(sql)

    def get_count_application_pc_checed(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_user_application_pc` WHERE `checked_engineer`=1;"
        return wraper_read(sql)

    def get_count_application_pc_all(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_user_application_pc` WHERE 1;"
        return wraper_read(sql)
# заявки от оператора


    def get_count_operator_application_no_checked(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_operator_application` WHERE `checked_engineer`=0;"
        return wraper_read(sql)

    def get_count_operator_application_checked(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_operator_application` WHERE `checked_engineer`=1;"
        return wraper_read(sql)

    def get_count_operator_application_all(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_operator_application` WHERE 1;"
        return wraper_read(sql)
# оперативные карточки
    def count_application_map_no_checked(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_application_map_for_pult` WHERE `checked_engineer`=0;"
        return wraper_read(sql)

    def count_application_map_checked(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_application_map_for_pult` WHERE `checked_engineer`=1;"
        return wraper_read(sql)

    def count_application_map_all(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_application_map_for_pult` WHERE 1;"
        return wraper_read(sql)

# обновление хоз органов
    def count_app_update_data_object_no_checked(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_application_update_users_objects` WHERE `checked_engineer`=0;"
        return wraper_read(sql)

    def count_app_update_data_object_checked(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_application_update_users_objects` WHERE `checked_engineer`=1;"
        return wraper_read(sql)

    def count_app_update_data_object_all(self):
        sql = "SELECT COUNT(*) AS `temp` FROM `dbo_application_update_users_objects` WHERE 1;"
        return wraper_read(sql)
# ---------------------------------------------------------------------------------------------------------


# ------------------------------------------Админская часть------------------------------------------------

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


class SettingsUsersRegType:
    def __init__(self, name_type: str):
        self.name_type = name_type
        self.sql_reg_new_type_user = "INSERT INTO `user_type` (`id`, `user_type`) " \
                                     "VALUES (NULL, '{}')".format(str(self.name_type))

    def reg_new_type(self):
        return wraper_write(self.sql_reg_new_type_user)


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
        # ---------------------------------------------------------------------------------------------------------

        # ---------------------------------------------------------------------------------------------------------
