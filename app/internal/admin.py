from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter(
    prefix="/admin"
)

# routes for admin only users
@router.get("/", response_class=HTMLResponse)
async def get_admin_dashboard():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>ADMIN DASHBOARD, GET RESPONSE</h1>
        </body>
    </html>
    """


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}