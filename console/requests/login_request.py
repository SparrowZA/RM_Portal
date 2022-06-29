from importlib import invalidate_caches
from typing import Mapping


class LoginInvalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False

class LoginValidRequest:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __bool__(self):
        return True
    
def build_login_request(form=None):
    accepted_keys = ['email', 'password']
    invalid_request = LoginInvalidRequest()

    if form is None:
        invalid_request.add_error('form', 'The form is empty.')
        return invalid_request
    elif len(form) != len(accepted_keys):
        invalid_request.add_error('form', 'Incorrect number of keys.') 
        
    for key, value in form.items():
        if key not in accepted_keys:
            invalid_request.add_error(
                'form',
                'Key {} cannot be used.'.format(key)
            )
    if invalid_request.has_errors():
        return invalid_request

    return LoginValidRequest(form['email'], form['password'])
