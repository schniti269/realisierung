# core/util/security.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Retrieves the current user based on the provided OAuth2 token.
    """
    # TODO: Implement token validation with OpenStack
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Mock user data for illustration purposes
    user = {"username": "testuser", "email": "testuser@example.com"}
    return user
