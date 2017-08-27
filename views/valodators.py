class Valodators:
    def __init__(self, input_object, name_type_valid: str):
        self.input_object = input_object
        self.name_type_valid = name_type_valid

        if self.name_type_valid == 'id':
            valid_id()
            pass

        elif self.name_type_valid == 'password':
            valid_password()
            pass

        elif self.name_type_valid == 'name':
            valid_name()
            pass

    def valid_in_script(self):
        '''Validator for the presence of a script'''
        pass

    def valid_id(self):
        '''ID valodator for int '''
        valid_in_script()
        pass

    def valid_password(self):
        '''Password validator min and max size and ...'''
        valid_in_script()
        pass

    def valid_name(self):
        '''Name validator min and max size and ...'''
        valid_in_script()
        pass
