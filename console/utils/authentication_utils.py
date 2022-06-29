def get_user_Id(storage, rm_email):
    user = storage.authenticate_email(rm_email=rm_email)
    if user is None:
        return None
    else:
        return user.id

def is_authenticated(storage, rm_id) -> bool:
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