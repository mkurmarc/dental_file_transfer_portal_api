from fastapi import APIRouter, File
from fastapi.responses import HTMLResponse
from app.static.html_generator import gen_admin_dashboard


router = APIRouter(
    prefix="/admin",
    tags=["Administrator"]
)

# routes for admin only users
@router.get("/", response_class=HTMLResponse)
async def get_admin_dashboard():    
    return gen_admin_dashboard()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}