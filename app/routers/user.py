from fastapi import status, HTTPException, APIRouter, Query
from sys import prefix
from fastapi import Request
from fastapi.responses import HTMLResponse



# prefix = adds the string to the beginning of each path op
# tags = is for the docs website for this api, it groups these path ops under 'Users' in the docs
router = APIRouter(
    prefix="/user", 
    tags=['User'] 
)

# path op GETs the create user page to render
@router.get("/create", response_class=HTMLResponse) 
async def get_create_page():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

# path op when user is done filling out form and hits 'done' button
@router.post("/create")
def create_user(username: str = Query(None, max_length=20)):
    return 