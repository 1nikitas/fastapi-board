from fastapi import Request

def is_authorized(request: Request):
    if not request.cookies.get('access_token'):
        return False
    return True
