from sqlrw import wraper_write


def drop_db():
    sql = "DROP TABLE dbo_electrician_application;" \
          "DROP TABLE dbo_operator_application;" \
          "DROP TABLE dbo_users; " \
          "DROP TABLE user_type; "
    wraper_write(sql)
    print('Database Delete!!!')


def create_db():
    sql = "CREATE TABLE `dbo_operator_application` (`id` int(11) NOT NULL AUTO_INCREMENT," \
          "`date_of_creation` text NOT NULL,`name_operator` text NOT NULL,`name_pult` text NOT NULL," \
          "`number_object` text NOT NULL,`message` text NOT NULL,`checked_engineer` int(1) NOT NULL," \
          "`date_of_completion` text NOT NULL, `name_engineer_completion` text NOT NULL, PRIMARY KEY (`id`))" \
          "ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;" \
          "CREATE TABLE `dbo_users` (`id` int(11) NOT NULL AUTO_INCREMENT,`user_name` text NOT NULL," \
          "`user_password` text NOT NULL,`user_type` text NOT NULL, PRIMARY KEY (`id`)) " \
          "ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;" \
          "CREATE TABLE `user_type` (`id` int(2) NOT NULL AUTO_INCREMENT,`user_type` text NOT NULL, PRIMARY KEY (`id`))" \
          "ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;" \
          "CREATE TABLE IF NOT EXISTS `dbo_electrician_application` ( `id` int(11) NOT NULL AUTO_INCREMENT, " \
          "`date_of_creation` text NOT NULL, `name_operator` text NOT NULL, `number_object` text NOT NULL, " \
          "`name_object` text NOT NULL, `address_object` text NOT NULL, `from_whom_application` text NOT NULL, " \
          "`checked_electrician` text NOT NULL, `date_checked` text NOT NULL, `on_which_date` text NOT NULL, " \
          "`application_description` text NOT NULL, PRIMARY KEY (`id`) ) ENGINE=InnoDB AUTO_INCREMENT=13 " \
          "DEFAULT CHARSET=utf8;" \
          "INSERT INTO `Pult`.`user_type` (`id`, `user_type`) " \
          "VALUES (1, 'Оператор'), (2, 'Инженер'), (3, 'Администратор');"
    wraper_write(sql)
    print('Database Create!!!')


if __name__ == '__main__':
    enter_command = str(input('1 : Drop DB \n2 : Create Clean DB\n'))
    if enter_command == str(1):
        drop_db()
    elif enter_command == str(2):
        create_db()
    else:
        pass
