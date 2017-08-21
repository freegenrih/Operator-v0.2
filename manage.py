from sqlrw import wraper_write


def drop_db():
    sql = "DROP TABLE IPSenderData;" \
          "DROP TABLE IPSender; " \
          "DROP TABLE LogerData; " \
          "DROP TABLE Users;"
    wraper_write(sql)
    print('Database Delete!!!')


def create_db():
    sql="CREATE TABLE IF NOT EXISTS `IPSender` ( `id` int(11) NOT NULL AUTO_INCREMENT," \
        "`name_ipsender` text NOT NULL, `key_ipsender` text NOT NULL, PRIMARY KEY (`id`) ) " \
        "ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8; " \
        "CREATE TABLE IF NOT EXISTS `IPSenderData` ( `id` int(11) NOT NULL AUTO_INCREMENT, `kay` text NOT NULL, " \
        "`ch1` int(11) NOT NULL, `ch2` int(11) NOT NULL, `ch3` int(11) NOT NULL, `ch4` int(11) NOT NULL, `ch5` int(11) " \
        "NOT NULL, `ch6` int(11) NOT NULL, `ch7` int(11) NOT NULL, `ch8` int(11) NOT NULL, `datetimes` text NOT NULL, " \
        "PRIMARY KEY (`id`) ) ENGINE=InnoDB AUTO_INCREMENT=176 DEFAULT CHARSET=utf8;" \
        "CREATE TABLE IF NOT EXISTS `LogerData` ( `id` int(11) NOT NULL AUTO_INCREMENT, `name` text NOT NULL, " \
        "`idsender` text NOT NULL, `ch1` int(4) NOT NULL, `ch2` int(4) NOT NULL, `ch3` int(4) NOT NULL, `ch4` int(4) " \
        "NOT NULL, `ch5` int(4) NOT NULL, `ch6` int(4) NOT NULL, `ch7` int(4) NOT NULL, `ch8` int(4) NOT NULL, " \
        "`datatime` text NOT NULL, PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8;" \
        "CREATE TABLE IF NOT EXISTS `Users` ( `id` int(11) NOT NULL AUTO_INCREMENT, `username` text NOT NULL, " \
        "`email` text NOT NULL, `password` text NOT NULL, `statusadmin` tinyint(1) NOT NULL, PRIMARY KEY (`id`) ) " \
        "ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8;" \
        "INSERT INTO `BigTester`.`Users` (`id`, `username`, `email`, `password`, `statusadmin`) " \
        "VALUES  (1, 'Gennadiy', 'admin@admin.ru', 'admins', 1);"
    wraper_write(sql)
    print('Database Create!!!')


if __name__ == '__main__':
    enter_command = str(input('1 : Drop DB \n2 : Create Clean DB(user=admin@admin.ru password=admins)\n'))
    if enter_command == str(1):
        drop_db()
    elif enter_command == str(2):
        create_db()
    else:
        pass
