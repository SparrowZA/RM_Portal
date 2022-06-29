from django.http import HttpResponseRedirect
from console.utils.authentication_utils import is_authenticated

def login_required(storage):
    '''
    A very rudimentary authentication wrapper.

    This decorator makes sure the relationship manager id
    is in the database.
    '''
    def decorator(view_func):
        def inner(request, rm_id, *args, **kwargs):
            if is_authenticated(storage, rm_id):
                return view_func(request, rm_id, *args, **kwargs)
            else:
                return HttpResponseRedirect('/error/')
        return inner
    return decorator
