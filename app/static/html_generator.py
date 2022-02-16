from fastapi.responses import HTMLResponse

def gen_create_user():
    html_content = """
    <html>
        <head>
            <title>Create User Page</title>
            <style>
                body {
                    background: #1D1E1D;
                    display: flex;
                    justify-content: center;
                }
                
                h1 {
                    color: silver;
                    align-self: center;
                }

                label {
                    color: white;
                    font-size: 0.9rem;
                    font-family: Arial, Verdana, sans-serif;
                }

                button {
                    border-radius: 8px;
                    font-size: 1rem;
                    font-family: Arial, Verdana, sans-serif;
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
                    height: 12%
                }

            </style>
        </head>

        <body>
            <div class="container">
                <h1>Sign Up</h1>
                <input type="text" name="first_name" placeholder="first name" class="items" size="30" spellcheck required>
                <input type="text" name="last_name" placeholder="last name" class="items" size="30" spellcheck required>
                <input type="text" name="email" placeholder="email" class="items" size="50" required>
                <input type="text" name="confirm_email" placeholder="confirm email" class="items" size="50" required>
                <input type="text" name="password" placeholder="password" class="items" size="30" required>
                <input type="text" name="confirm_password" placeholder="confirm password" class="items" size="30" required>
                <label class="items"><input type="checkbox" name="terms_checkbox"> Accept the Terms and Policies</label>
                <button type="button" name="login_b class="items"">Submit</button>
            </div>
        </body>

    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


def gen_login():
    html_content = """
    <html>
        <head>
            <title>Login Page</title>
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
                    height: 12%
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


def gen_upload():
    html_content = """
    <html>
        <head>
            <title>Upload Page</title>
            <style>

                body {
                    background: #1D1E1D;
                    text-align: center;
                    margin-top: 30px;
                }

                #upload-wrapper {
                    text-align: center;
                    color: white;
                }

                h1 {
                    color: silver;
        
                }

            </style>
        </head>

        <body>
        <h1>Upload Files</h1>
        <div id="upload-wrapper">            
            <form action="/uploadfiles" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit" value="Upload">
            </form>
        </div>

        </body>

    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


def gen_admin_dashboard():

    html_content = """
        <html>
            <head>
                <title>Admin Dashboard</title>
                <style>
                    body {
                        background: #1D1E1D;
                        display: flex;
                        justify-content: center;
                    }

                    .sidebar {
                        position: absolute;
                        width: 199px;
                        height: 1014px;
                        left: 0px;
                        top: 0px;
                        background: #C4C4C4;
                    }

                    #current_user_img {
                        position: absolute;
                        width: 81px;
                        height: 81px;
                        left: 59px;
                        top: 105px;
                        background: #FFFFFF;
                    }

                    img {
                        position: absolute;
                        width: 67px;
                        height: 67px;
                        left: 66px;
                        top: 112px;
                    }

                    h1 {
                        color: silver;
                        align-self: center;
                    }
                </style>
            </head>

            <body>
                <h1>Admin Dashboard</h1>
                <div class="sidebar"></div>
                <div id="current_user_img"><img src="img\profile_img.jpg" alt=""></div>
            </body>


        </html>
    """
    # url(img\profile_img.jpg)
    return HTMLResponse(content=html_content, status_code=200)


def gen_home():
    html_content = """
    <html>
        <head>
            <title>Home Page</title>
            <style>
                body {
                    background: #1D1E1D;
                    justify-content: center;
                    display: flex;
                }
                
                .container {
                    display: flex;
                    flex-direction: column;
                    justify-content: center; 
                    gap: 15px;
                }

                .items {
                    width: 100%;
                    height: auto;
                }

                h1 {
                    color: silver;
                    text-align: center;
                }

                .bn54 {
                    position: relative;
                    outline: none;
                    text-decoration: none;
                    border-radius: 50px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    cursor: pointer;
                    text-transform: uppercase;
                    height: 45px;
                    width: 20rem;
                    opacity: 1;
                    background-color: #ffffff;
                    border: 1px solid rgba(0, 0, 0, 0.6);
                }

                .bn54 .bn54span {
                    font-family: Verdana, Geneva, Tahoma, sans-serif;
                    color: #000000;
                    font-size: 12px;
                    font-weight: 500;
                    letter-spacing: 0.7px;
                }

                .bn54:hover {
                    animation: bn54rotate 0.7s ease-in-out both;
                }

                .bn54:hover .bn54span {
                    animation: bn54storm 0.7s ease-in-out both;
                    animation-delay: 0.06s;
                }

                @keyframes bn54rotate {
                    0% {
                        transform: rotate(0deg) translate3d(0, 0, 0);
                    }
                    25% {
                        transform: rotate(3deg) translate3d(0, 0, 0);
                    }
                    50% {
                        transform: rotate(-3deg) translate3d(0, 0, 0);
                    }
                    75% {
                        transform: rotate(1deg) translate3d(0, 0, 0);
                    }
                    100% {
                        transform: rotate(0deg) translate3d(0, 0, 0);
                    }
                }

                @keyframes bn54storm {
                    0% {
                        transform: translate3d(0, 0, 0) translateZ(0);
                    }
                    25% {
                        transform: translate3d(4px, 0, 0) translateZ(0);
                    }
                    50% {
                        transform: translate3d(-3px, 0, 0) translateZ(0);
                    }
                    75% {
                        transform: translate3d(2px, 0, 0) translateZ(0);
                    }
                    100% {
                        transform: translate3d(0, 0, 0) translateZ(0);
                    }
                }
            </style>
        </head>

        <body>
            <div class="container">
                <h1 class="items">Home Page</h1>
                <a href="http://127.0.0.1:8000/login" class="items">
                    <button class="bn54">
                    <span class="bn54span">Login</span>
                    </button>
                </a>
                <a href="http://127.0.0.1:8000/user/create" class="items">
                    <button class="bn54">
                    <span class="bn54span">Create User</span>
                    </button>
                </a>
            </div>
        </body>

    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)