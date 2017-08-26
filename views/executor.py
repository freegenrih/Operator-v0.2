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


class EngineerList:
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
