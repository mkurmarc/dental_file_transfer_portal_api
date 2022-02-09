from fastapi.responses import HTMLResponse

def gen_create_user():
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


def gen_login():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
            <style>
                body {
                    background: #1D1E1D;
                    display: flex;
                    justify-content: center;
                }

                .container {
                    width: 35%;
                    height: 35%;
                    display: flex;
                    flex-direction: column;
                    justify-content: center; 
                    gap: 10px;
                }

                .items {
                    width: 100%;
                }

                h1 {
                    color: silver;
                    align-self: center;
                }

                button {
                    border-radius: 8px;
                }


            </style>
        </head>

        <body>
            
            <div class="container">
                <h1>Login</h1>
                <input class="items" type="email" name="email" placeholder="your@email.com" size="30" required>
                <input class="items" type="password" name="password" placeholder="password" size="20" required>
                <button class="items" type="button" name="login_b">Login</button>
            </div>

        </body>

    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)