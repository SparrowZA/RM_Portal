from console.adapters.django_storage import DjangoStorage

storage = DjangoStorage()

# class RmAuth():
def get_user_Id(rm_email):
    return storage.get_rm_id(rm_email=rm_email).id

def is_authenticated(rm_id) -> bool:
    '''
    This is a wrapper for authenticating the rm manager.

    *** Note ***
    Currently this only checks if the id exists in the DB.
    '''
    rm_obj = storage.get_rm(rm_id=rm_id)
    if rm_obj:
        return True
    else:
        False