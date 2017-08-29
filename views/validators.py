import re


class Validators:
    '''
        object: str or int
        (object, 'id')
        (object, 'password', min_len=int, max_len=int)
        (object, 'name', min_len=int, max_len=int)

    '''

    def __init__(self, input_object, name_type_valid: str, min_len=None, max_len=None):
        self.input_object = input_object
        self.name_type_valid = name_type_valid
        self.min_len = min_len
        self.max_len = max_len
        self.script_injection = ('SELECT', '\'SELECT', '\"SELECT', 'INSERT', 'DELETE', 'WHEARE', '<SCRIPT')

        if self.name_type_valid == 'id':
            self.valid_id()

        elif self.name_type_valid == 'password':
            self.valid_password()


        elif self.name_type_valid == 'name':
            self.valid_name()

        else:
            pass

    def valid_in_script(self):
        '''Validator for the presence of a script'''
        result_valid_in_script = None
        result_for_lowercase = None
        result_for_uppercase = None

        for number in range(0, len(self.script_injection)):
            if re.match(str(self.script_injection[number].upper()), str(self.input_object)) != None:
                result_for_lowercase = False
                break
            else:
                result_for_lowercase = True

        if result_for_lowercase == True:
            for number in range(0, len(self.script_injection)):
                if re.match(str(self.script_injection[number]).lower(), str(self.input_object)) != None:
                    result_for_uppercase = False
                    break
                else:
                    result_for_uppercase = True
        else:
            pass

        if result_for_lowercase == True and result_for_uppercase == True:
            result_valid_in_script = True
        else:
            result_valid_in_script = False

        return result_valid_in_script

    def valid_id(self):
        '''ID valodator for type int '''
        result_valid_id = None
        if self.valid_in_script() == True and type(self.input_object) == int:
            result_valid_id = True
        else:
            result_valid_id = False

        return result_valid_id

    def valid_password(self):
        '''Password validator min and max size and ...'''
        result_valid_password = None
        if self.valid_in_script() == True \
                and len(self.input_object) > self.min_len - 1 \
                and len(self.input_object) < self.max_len + 1:
            result_valid_password = True
        else:
            result_valid_password = False

        return result_valid_password

    def valid_name(self):
        '''Name validator min and max size and ...'''
        result_valid_name = None
        if self.valid_in_script() == True \
                and len(self.input_object) > self.min_len - 1 \
                and len(self.input_object) < self.max_len + 1:
            result_valid_name = True

        else:
            result_valid_name = False

        return  result_valid_name



if __name__ == '__main__':
    # tests validators id ----------------------------------------------------------------------------------------------
    idn = 947
    text1 = 'sdkijfgjfgjh'
    text2 = '\'SELECT * FROM'
    text3 = 'DELETE'
    text4 = 'select 857 '

    id = Validators(idn, 'id')
    id_1 = Validators(text1, 'id')
    id_2 = Validators(text2, 'id')
    id_3 = Validators(text3, 'id')
    id_4 = Validators(text4, 'id')

    # ------------------------------------------------------------------------------------------------------------------

    # test valodators password -----------------------------------------------------------------------------------------
    password1 = 'jhbsdefjhgjhgsdf76564590798awsjyhgfoipuy3rfi'
    password2 = '123456'
    password3 = 'SELECT'
    password4 = 'select'
    password5 = '<script'
    password6 = '1234567891'

    psw1 = Validators(password1, 'password', min_len=5, max_len=10)
    psw2 = Validators(password2, 'password', min_len=5, max_len=10)
    psw3 = Validators(password3, 'password', min_len=5, max_len=10)
    psw4 = Validators(password4, 'password', min_len=5, max_len=10)
    psw5 = Validators(password5, 'password', min_len=5, max_len=10)
    psw6 = Validators(password6, 'password', min_len=6, max_len=9)

    # ------------------------------------------------------------------------------------------------------------------

    #Validator name-----------------------------------------------------------------------------------------------------
    name1= 'Андрей' # len=6
    name2= 'Григорий' # len=8
    name3= 'SELECT' # len=6

    nm1 = Validators(name1, 'name', min_len=4, max_len=10)
    nm2 = Validators(name2, 'name', min_len=9, max_len=12)
    nm3 = Validators(name3, 'name', min_len=7, max_len=10)
    #-------------------------------------------------------------------------------------------------------------------

    # validation id
    print('=' * 15, 'ID', '=' * 15)
    print(idn, ':', id.valid_id())
    print(text1, ':', id_1.valid_id())
    print(text2, ':', id_2.valid_id())
    print(text3, ':', id_3.valid_id())
    print(text4, ':', id_4.valid_id())

    # validation password
    print('=' * 15, 'PASSWORD', '=' * 15)
    print(password1, psw1.valid_password())
    print(password2, psw2.valid_password())
    print(password3, psw3.valid_password())
    print(password4, psw4.valid_password())
    print(password5, psw5.valid_password())
    print(password6, psw6.valid_password())

    #validation name
    print('=' * 15, 'Name', '=' * 15)
    print(name1, nm1.valid_name())
    print(name2, nm2.valid_name())
    print(name3, nm3.valid_name())
