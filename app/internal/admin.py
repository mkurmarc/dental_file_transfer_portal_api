from fastapi import APIRouter, File, Depends
from fastapi.responses import HTMLResponse
from app.static.html_generator import gen_admin_dashboard
from sqlalchemy.orm import Session 
from app import database, schemas, models, utils, oauth2

router = APIRouter(
    prefix="/admin",
    tags=["Administrator"]
)

# routes for admin only users
@router.get("/", response_class=HTMLResponse)
async def get_admin_dashboard(admin_user: int = Depends(oauth2.get_admin_user),
db: Session = Depends(database.get_db), limit: int = 10):
       
    # load 10 most recent files uploaded
    files = []
    files = db.query(models.File).limit(limit)
    return gen_admin_dashboard()


@router.post("/")
async def update_admin(admin_user: int = Depends(oauth2.get_admin_user)):
    return {"message": "Admin getting schwifty"}
