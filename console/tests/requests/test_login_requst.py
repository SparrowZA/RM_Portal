from unittest import TestCase

from console.requests.login_request import ( 
        build_login_request, LoginValidRequest, LoginInvalidRequest) 

class LoginRequest(TestCase):
    def test_login_valid_form_data(self):
        form = {
            'email': 'dirk.trevin@test.com',
            'password': ''
        }

        request = build_login_request(form)

        assert bool(request) is True
        assert type(request) is LoginValidRequest
        assert request.email == 'dirk.trevin@test.com'
    
    def test_login_missing_password_key(self):
        form = {
            'email': 'dirk.trevin@test.com'
        }

        request = build_login_request(form)

        assert type(request) is LoginInvalidRequest
        assert bool(request) is False
        assert request.has_errors() is True
        assert request.errors[0]['parameter'] == 'form'
        assert request.errors[0]['message'] == 'Incorrect number of keys.'
    
    def test_login_missing_email_key(self):
        form = {
            'password': ''
        }

        request = build_login_request(form)

        assert type(request) is LoginInvalidRequest
        assert bool(request) is False
        assert request.has_errors() is True
        assert request.errors[0]['parameter'] == 'form'
        assert request.errors[0]['message'] == 'Incorrect number of keys.'
    
    def test_login_empty_form(self):
        form = {
        }

        request = build_login_request(form)

        assert type(request) is LoginInvalidRequest
        assert bool(request) is False
        assert request.has_errors() is True
        assert request.errors[0]['parameter'] == 'form'
        assert request.errors[0]['message'] == 'Incorrect number of keys.'
    
    def test_login_form_of_none(self):
        form = None

        request = build_login_request(form)

        assert type(request) is LoginInvalidRequest
        assert bool(request) is False
        assert request.has_errors() is True
        assert request.errors[0]['parameter'] == 'form'
        assert request.errors[0]['message'] == 'The form is empty.'
    
    def test_login_incorrect_key_in_form(self):
        form = {
            'email': 'test@gmail.com',
            'id': 1
        }

        request = build_login_request(form)

        assert type(request) is LoginInvalidRequest
        assert bool(request) is False
        assert request.has_errors() is True
        assert request.errors[0]['parameter'] == 'form'
        assert request.errors[0]['message'] == 'Key id cannot be used.'
