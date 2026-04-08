import secrets
import shelve
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
from app.schemas.link import LinkCreate


router = APIRouter()
# NOTE: This is for just for the very minimal setup to quickly get up and running ofcourse I'm gonna use environment variables in production ;)
DB_NAME = "cutlet.db"


#TODO: Add error handling
"""
@params: Destination URL
@method: POST
@return: Short Code
"""
@router.post("/links", tags=["Links"])
async def create_short_code(link: LinkCreate):
    short_code = secrets.token_urlsafe(6)
    # short_code = base64.urlsafe_b64encode(key.encode('utf-8')).decode('utf-8').rstrip('=')
    with shelve.open(filename=DB_NAME) as db:
        db[short_code[:6]] = link.url
        db.close()

    print("SC:", short_code[:6])
    return {"short_code": short_code[:6]}


"""
@params: Short Code
@method: GET
@return: Redirects to the Destination URL
"""
