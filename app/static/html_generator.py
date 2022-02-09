from fastapi.responses import HTMLResponse

def generate_create_user():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
            <style>
                h1 {
                    color: red;
                }
            </style>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)