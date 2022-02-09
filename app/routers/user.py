from fastapi import status, HTTPException, APIRouter, Query
from sys import prefix
from fastapi import Request
from fastapi.responses import HTMLResponse, FileResponse
# from app.main import templates
from app.static.html_generator import generate_create_user

# prefix = adds the string to the beginning of each path op
# tags = is for the docs website for this api, it groups these path ops under 'Users' in the docs
router = APIRouter(
    prefix="/user", 
    tags=['User']
)

# path op GETs the create user page to render
@router.get("/create", response_class=HTMLResponse) 
async def get_create_page():
    return generate_create_user()

# @router.get("/create") 
# async def get_create_page(request: Request):
#     return templates.TemplateResponse(
#         "app/static/template_base.html", {"request": request}
#     )

# path op when user is done filling out form and hits 'done' button
@router.post("/create")
def create_user(username: str = Query(None, max_length=20)):
    return 