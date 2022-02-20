from fastapi.responses import HTMLResponse

def gen_create_user():
    html_content = """
        <html>

<head>
    <title>Login Page</title>
    <style>
        @import url(https://fonts.googleapis.com/css?family=Open+Sans);


        .btn {
            display: inline-block;
            *display: inline;
            *zoom: 1;
            padding: 4px 10px 4px;
            margin-bottom: 0;
            font-size: 13px;
            line-height: 18px;
            color: #333333;
            text-align: center;
            text-shadow: 0 1px 1px rgba(255, 255, 255, 0.75);
            vertical-align: middle;
            background-color: #f5f5f5;
            background-image: -moz-linear-gradient(top, #ffffff, #e6e6e6);
            background-image: -ms-linear-gradient(top, #ffffff, #e6e6e6);
            background-image: -webkit-gradient(linear,
                    0 0,
                    0 100%,
                    from(#ffffff),
                    to(#e6e6e6));
            background-image: -webkit-linear-gradient(top, #ffffff, #e6e6e6);
            background-image: -o-linear-gradient(top, #ffffff, #e6e6e6);
            background-image: linear-gradient(top, #ffffff, #e6e6e6);
            background-repeat: repeat-x;
            filter: progid:dximagetransform.microsoft.gradient(startColorstr=#ffffff, endColorstr=#e6e6e6, GradientType=0);
            border-color: #e6e6e6 #e6e6e6 #e6e6e6;
            border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
            border: 1px solid #e6e6e6;
            -webkit-border-radius: 4px;
            -moz-border-radius: 4px;
            border-radius: 4px;
            -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                0 1px 2px rgba(0, 0, 0, 0.05);
            -moz-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                0 1px 2px rgba(0, 0, 0, 0.05);
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                0 1px 2px rgba(0, 0, 0, 0.05);
            cursor: pointer;
            *margin-left: 0.3em;
        }

        .btn:hover,
        .btn:active,
        .btn.active,
        .btn.disabled,
        .btn[disabled] {
            background-color: #e6e6e6;
        }

        .btn-large {
            padding: 9px 14px;
            font-size: 15px;
            line-height: normal;
            -webkit-border-radius: 5px;
            -moz-border-radius: 5px;
            border-radius: 5px;
        }

        .btn:hover {
            color: #333333;
            text-decoration: none;
            background-color: #e6e6e6;
            background-position: 0 -15px;
            -webkit-transition: background-position 0.1s linear;
            -moz-transition: background-position 0.1s linear;
            -ms-transition: background-position 0.1s linear;
            -o-transition: background-position 0.1s linear;
            transition: background-position 0.1s linear;
        }

        .btn-primary,
        .btn-primary:hover {
            text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
            color: #ffffff;
        }

        .btn-primary.active {
            color: rgba(255, 255, 255, 0.75);
        }

        .btn-primary {
            background-color: #4a77d4;
            background-image: -moz-linear-gradient(top, #6eb6de, #4a77d4);
            background-image: -ms-linear-gradient(top, #6eb6de, #4a77d4);
            background-image: -webkit-gradient(linear,
                    0 0,
                    0 100%,
                    from(#6eb6de),
                    to(#4a77d4));
            background-image: -webkit-linear-gradient(top, #6eb6de, #4a77d4);
            background-image: -o-linear-gradient(top, #6eb6de, #4a77d4);
            background-image: linear-gradient(top, #6eb6de, #4a77d4);
            background-repeat: repeat-x;
            filter: progid:dximagetransform.microsoft.gradient(startColorstr=#6eb6de, endColorstr=#4a77d4, GradientType=0);
            border: 1px solid #3762bc;
            text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.4);
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                0 1px 2px rgba(0, 0, 0, 0.5);
        }

        .btn-primary:hover,
        .btn-primary:active,
        .btn-primary.active,
        .btn-primary.disabled,
        .btn-primary[disabled] {
            filter: none;
            background-color: #4a77d4;
        }

        .btn-block {
            width: 100%;
            display: block;
        }

        * {
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            -ms-box-sizing: border-box;
            -o-box-sizing: border-box;
            box-sizing: border-box;
        }

        html {
            width: 100%;
            height: 100%;
            overflow: hidden;
        }

        body {
            width: 100%;
            height: 100%;
            font-family: "Open Sans", sans-serif;
            background: #092756;
            background: -moz-radial-gradient(0% 100%,
                    ellipse cover,
                    rgba(104, 128, 138, 0.4) 10%,
                    rgba(138, 114, 76, 0) 40%),
                -moz-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%),
                -moz-linear-gradient(-45deg, #670d10 0%, #092756 100%);
            background: -webkit-radial-gradient(0% 100%,
                    ellipse cover,
                    rgba(104, 128, 138, 0.4) 10%,
                    rgba(138, 114, 76, 0) 40%),
                -webkit-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42,
                        60,
                        87,
                        0.4) 100%),
                -webkit-linear-gradient(-45deg, #670d10 0%, #092756 100%);
            background: -o-radial-gradient(0% 100%,
                    ellipse cover,
                    rgba(104, 128, 138, 0.4) 10%,
                    rgba(138, 114, 76, 0) 40%),
                -o-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%),
                -o-linear-gradient(-45deg, #670d10 0%, #092756 100%);
            background: -ms-radial-gradient(0% 100%,
                    ellipse cover,
                    rgba(104, 128, 138, 0.4) 10%,
                    rgba(138, 114, 76, 0) 40%),
                -ms-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%),
                -ms-linear-gradient(-45deg, #670d10 0%, #092756 100%);
            background: -webkit-radial-gradient(0% 100%,
                    ellipse cover,
                    rgba(104, 128, 138, 0.4) 10%,
                    rgba(138, 114, 76, 0) 40%),
                linear-gradient(to bottom,
                    rgba(57, 173, 219, 0.25) 0%,
                    rgba(42, 60, 87, 0.4) 100%),
                linear-gradient(135deg, #670d10 0%, #092756 100%);
            filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#3E1D6D', endColorstr='#092756', GradientType=1);
        }

        .login {
            position: absolute;
            top: 30%;
            left: 50%;
            margin: -150px 0 0 -150px;
            width: 300px;
        }

        .login h1 {
            color: #fff;
            text-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
            letter-spacing: 1px;
            text-align: center;
        }

        input {
            width: 100%;
            margin-bottom: 10px;
            background: rgba(0, 0, 0, 0.3);
            border: none;
            outline: none;
            padding: 10px;
            font-size: 13px;
            color: #fff;
            text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(0, 0, 0, 0.3);
            border-radius: 4px;
            box-shadow: inset 0 -5px 45px rgba(100, 100, 100, 0.2),
                0 1px 1px rgba(255, 255, 255, 0.2);
            -webkit-transition: box-shadow 0.5s ease;
            -moz-transition: box-shadow 0.5s ease;
            -o-transition: box-shadow 0.5s ease;
            -ms-transition: box-shadow 0.5s ease;
            transition: box-shadow 0.5s ease;
        }

        input:focus {
            box-shadow: inset 0 -5px 45px rgba(100, 100, 100, 0.4),
                0 1px 1px rgba(255, 255, 255, 0.2);
        }
    </style>
</head>

<body>
    <div class="login">
        <h1>Create User</h1>
        <form action="http://127.0.0.1:8000/user" method="post">
            <input class="items" type="text" name="first_name" placeholder="First Name" size="30" required>
            <input class="items" type="text" name="last_name" placeholder="Last Name" size="30" required>
            <input class="items" type="text" name="company_name" placeholder="Company Name" size="50">
            <input class="items" type="email" name="email" placeholder="your@email.com" size="30" required>
            <input class="items" type="password" name="password" placeholder="Password" size="20" required>
            <input class="items" type="password" name="confirm_password" placeholder="Confirm Password" size="20" required>
            <input type="submit" value="Submit" class="btn btn-primary btn-block btn-large">
        </form>
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
                @import url(https://fonts.googleapis.com/css?family=Open+Sans);


                .btn {
                    display: inline-block;
                    *display: inline;
                    *zoom: 1;
                    padding: 4px 10px 4px;
                    margin-bottom: 0;
                    font-size: 13px;
                    line-height: 18px;
                    color: #333333;
                    text-align: center;
                    text-shadow: 0 1px 1px rgba(255, 255, 255, 0.75);
                    vertical-align: middle;
                    background-color: #f5f5f5;
                    background-image: -moz-linear-gradient(top, #ffffff, #e6e6e6);
                    background-image: -ms-linear-gradient(top, #ffffff, #e6e6e6);
                    background-image: -webkit-gradient(linear,
                            0 0,
                            0 100%,
                            from(#ffffff),
                            to(#e6e6e6));
                    background-image: -webkit-linear-gradient(top, #ffffff, #e6e6e6);
                    background-image: -o-linear-gradient(top, #ffffff, #e6e6e6);
                    background-image: linear-gradient(top, #ffffff, #e6e6e6);
                    background-repeat: repeat-x;
                    filter: progid:dximagetransform.microsoft.gradient(startColorstr=#ffffff, endColorstr=#e6e6e6, GradientType=0);
                    border-color: #e6e6e6 #e6e6e6 #e6e6e6;
                    border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
                    border: 1px solid #e6e6e6;
                    -webkit-border-radius: 4px;
                    -moz-border-radius: 4px;
                    border-radius: 4px;
                    -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                        0 1px 2px rgba(0, 0, 0, 0.05);
                    -moz-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                        0 1px 2px rgba(0, 0, 0, 0.05);
                    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                        0 1px 2px rgba(0, 0, 0, 0.05);
                    cursor: pointer;
                    *margin-left: 0.3em;
                }

                .btn:hover,
                .btn:active,
                .btn.active,
                .btn.disabled,
                .btn[disabled] {
                    background-color: #e6e6e6;
                }

                .btn-large {
                    padding: 9px 14px;
                    font-size: 15px;
                    line-height: normal;
                    -webkit-border-radius: 5px;
                    -moz-border-radius: 5px;
                    border-radius: 5px;
                }

                .btn:hover {
                    color: #333333;
                    text-decoration: none;
                    background-color: #e6e6e6;
                    background-position: 0 -15px;
                    -webkit-transition: background-position 0.1s linear;
                    -moz-transition: background-position 0.1s linear;
                    -ms-transition: background-position 0.1s linear;
                    -o-transition: background-position 0.1s linear;
                    transition: background-position 0.1s linear;
                }

                .btn-primary,
                .btn-primary:hover {
                    text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
                    color: #ffffff;
                }

                .btn-primary.active {
                    color: rgba(255, 255, 255, 0.75);
                }

                .btn-primary {
                    background-color: #4a77d4;
                    background-image: -moz-linear-gradient(top, #6eb6de, #4a77d4);
                    background-image: -ms-linear-gradient(top, #6eb6de, #4a77d4);
                    background-image: -webkit-gradient(linear,
                            0 0,
                            0 100%,
                            from(#6eb6de),
                            to(#4a77d4));
                    background-image: -webkit-linear-gradient(top, #6eb6de, #4a77d4);
                    background-image: -o-linear-gradient(top, #6eb6de, #4a77d4);
                    background-image: linear-gradient(top, #6eb6de, #4a77d4);
                    background-repeat: repeat-x;
                    filter: progid:dximagetransform.microsoft.gradient(startColorstr=#6eb6de, endColorstr=#4a77d4, GradientType=0);
                    border: 1px solid #3762bc;
                    text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.4);
                    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                        0 1px 2px rgba(0, 0, 0, 0.5);
                }

                .btn-primary:hover,
                .btn-primary:active,
                .btn-primary.active,
                .btn-primary.disabled,
                .btn-primary[disabled] {
                    filter: none;
                    background-color: #4a77d4;
                }

                .btn-block {
                    width: 100%;
                    display: block;
                }

                * {
                    -webkit-box-sizing: border-box;
                    -moz-box-sizing: border-box;
                    -ms-box-sizing: border-box;
                    -o-box-sizing: border-box;
                    box-sizing: border-box;
                }

                html {
                    width: 100%;
                    height: 100%;
                    overflow: hidden;
                }

                body {
                    width: 100%;
                    height: 100%;
                    font-family: "Open Sans", sans-serif;
                    background: #092756;
                    background: -moz-radial-gradient(0% 100%,
                            ellipse cover,
                            rgba(104, 128, 138, 0.4) 10%,
                            rgba(138, 114, 76, 0) 40%),
                        -moz-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%),
                        -moz-linear-gradient(-45deg, #670d10 0%, #092756 100%);
                    background: -webkit-radial-gradient(0% 100%,
                            ellipse cover,
                            rgba(104, 128, 138, 0.4) 10%,
                            rgba(138, 114, 76, 0) 40%),
                        -webkit-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42,
                                60,
                                87,
                                0.4) 100%),
                        -webkit-linear-gradient(-45deg, #670d10 0%, #092756 100%);
                    background: -o-radial-gradient(0% 100%,
                            ellipse cover,
                            rgba(104, 128, 138, 0.4) 10%,
                            rgba(138, 114, 76, 0) 40%),
                        -o-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%),
                        -o-linear-gradient(-45deg, #670d10 0%, #092756 100%);
                    background: -ms-radial-gradient(0% 100%,
                            ellipse cover,
                            rgba(104, 128, 138, 0.4) 10%,
                            rgba(138, 114, 76, 0) 40%),
                        -ms-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%),
                        -ms-linear-gradient(-45deg, #670d10 0%, #092756 100%);
                    background: -webkit-radial-gradient(0% 100%,
                            ellipse cover,
                            rgba(104, 128, 138, 0.4) 10%,
                            rgba(138, 114, 76, 0) 40%),
                        linear-gradient(to bottom,
                            rgba(57, 173, 219, 0.25) 0%,
                            rgba(42, 60, 87, 0.4) 100%),
                        linear-gradient(135deg, #670d10 0%, #092756 100%);
                    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#3E1D6D', endColorstr='#092756', GradientType=1);
                }

                .login {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    margin: -150px 0 0 -150px;
                    width: 300px;
                    height: 300px;
                }

                .login h1 {
                    color: #fff;
                    text-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
                    letter-spacing: 1px;
                    text-align: center;
                }

                input {
                    width: 100%;
                    margin-bottom: 10px;
                    background: rgba(0, 0, 0, 0.3);
                    border: none;
                    outline: none;
                    padding: 10px;
                    font-size: 13px;
                    color: #fff;
                    text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.3);
                    border: 1px solid rgba(0, 0, 0, 0.3);
                    border-radius: 4px;
                    box-shadow: inset 0 -5px 45px rgba(100, 100, 100, 0.2),
                        0 1px 1px rgba(255, 255, 255, 0.2);
                    -webkit-transition: box-shadow 0.5s ease;
                    -moz-transition: box-shadow 0.5s ease;
                    -o-transition: box-shadow 0.5s ease;
                    -ms-transition: box-shadow 0.5s ease;
                    transition: box-shadow 0.5s ease;
                }

                input:focus {
                    box-shadow: inset 0 -5px 45px rgba(100, 100, 100, 0.4),
                        0 1px 1px rgba(255, 255, 255, 0.2);
                }
            </style>
        </head>

    <body>
        <div class="login">
            <h1>Login</h1>
            <form method="POST" action="http://127.0.0.1:8000/login/">
                <input class="items" type="text" name="username" id="username" placeholder="your@email.com" size="30" required>
                <input class="items" type="password" name="password" id="password" placeholder="password" size="20" required>
                <input type="submit" value="Login" class="btn btn-primary btn-block btn-large">
            </form>
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

            .btn {
                display: inline-block;
                *display: inline;
                *zoom: 1;
                padding: 4px 10px 4px;
                margin-bottom: 0;
                font-size: 13px;
                line-height: 18px;
                color: #333333;
                text-align: center;
                text-shadow: 0 1px 1px rgba(255, 255, 255, 0.75);
                vertical-align: middle;
                background-color: #f5f5f5;
                background-image: -moz-linear-gradient(top, #ffffff, #e6e6e6);
                background-image: -ms-linear-gradient(top, #ffffff, #e6e6e6);
                background-image: -webkit-gradient(linear,
                        0 0,
                        0 100%,
                        from(#ffffff),
                        to(#e6e6e6));
                background-image: -webkit-linear-gradient(top, #ffffff, #e6e6e6);
                background-image: -o-linear-gradient(top, #ffffff, #e6e6e6);
                background-image: linear-gradient(top, #ffffff, #e6e6e6);
                background-repeat: repeat-x;
                filter: progid:dximagetransform.microsoft.gradient(startColorstr=#ffffff, endColorstr=#e6e6e6, GradientType=0);
                border-color: #e6e6e6 #e6e6e6 #e6e6e6;
                border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
                border: 1px solid #e6e6e6;
                -webkit-border-radius: 4px;
                -moz-border-radius: 4px;
                border-radius: 4px;
                -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                    0 1px 2px rgba(0, 0, 0, 0.05);
                -moz-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                    0 1px 2px rgba(0, 0, 0, 0.05);
                box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                    0 1px 2px rgba(0, 0, 0, 0.05);
                cursor: pointer;
                *margin-left: 0.3em;
            }

            .btn:hover,
            .btn:active,
            .btn.active,
            .btn.disabled,
            .btn[disabled] {
                background-color: #e6e6e6;
            }

            .btn-large {
                padding: 9px 14px;
                font-size: 15px;
                line-height: normal;
                -webkit-border-radius: 5px;
                -moz-border-radius: 5px;
                border-radius: 5px;
            }

            .btn:hover {
                color: #333333;
                text-decoration: none;
                background-color: #e6e6e6;
                background-position: 0 -15px;
                -webkit-transition: background-position 0.1s linear;
                -moz-transition: background-position 0.1s linear;
                -ms-transition: background-position 0.1s linear;
                -o-transition: background-position 0.1s linear;
                transition: background-position 0.1s linear;
            }

            .btn-primary,
            .btn-primary:hover {
                text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
                color: #ffffff;
            }

            .btn-primary.active {
                color: rgba(255, 255, 255, 0.75);
            }

            .btn-primary {
                background-color: #4a77d4;
                background-image: -moz-linear-gradient(top, #6eb6de, #4a77d4);
                background-image: -ms-linear-gradient(top, #6eb6de, #4a77d4);
                background-image: -webkit-gradient(linear,
                        0 0,
                        0 100%,
                        from(#6eb6de),
                        to(#4a77d4));
                background-image: -webkit-linear-gradient(top, #6eb6de, #4a77d4);
                background-image: -o-linear-gradient(top, #6eb6de, #4a77d4);
                background-image: linear-gradient(top, #6eb6de, #4a77d4);
                background-repeat: repeat-x;
                filter: progid:dximagetransform.microsoft.gradient(startColorstr=#6eb6de, endColorstr=#4a77d4, GradientType=0);
                border: 1px solid #3762bc;
                text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.4);
                box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
                    0 1px 2px rgba(0, 0, 0, 0.5);
            }

            .btn-primary:hover,
            .btn-primary:active,
            .btn-primary.active,
            .btn-primary.disabled,
            .btn-primary[disabled] {
                filter: none;
                background-color: #4a77d4;
            }

            .btn-block {
                width: 100%;
                display: block;
            }

            * {
                -webkit-box-sizing: border-box;
                -moz-box-sizing: border-box;
                -ms-box-sizing: border-box;
                -o-box-sizing: border-box;
                box-sizing: border-box;
            }

            html {
                width: 100%;
                height: 100%;
                overflow: hidden;
            }

            body {
                width: 100%;
                height: 100%;
                font-family: "Open Sans", sans-serif;
                background: #092756;
                background: -moz-radial-gradient(0% 100%,
                        ellipse cover,
                        rgba(104, 128, 138, 0.4) 10%,
                        rgba(138, 114, 76, 0) 40%),
                    -moz-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%),
                    -moz-linear-gradient(-45deg, #670d10 0%, #092756 100%);
                background: -webkit-radial-gradient(0% 100%,
                        ellipse cover,
                        rgba(104, 128, 138, 0.4) 10%,
                        rgba(138, 114, 76, 0) 40%),
                    -webkit-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42,
                            60,
                            87,
                            0.4) 100%),
                    -webkit-linear-gradient(-45deg, #670d10 0%, #092756 100%);
                background: -o-radial-gradient(0% 100%,
                        ellipse cover,
                        rgba(104, 128, 138, 0.4) 10%,
                        rgba(138, 114, 76, 0) 40%),
                    -o-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%),
                    -o-linear-gradient(-45deg, #670d10 0%, #092756 100%);
                background: -ms-radial-gradient(0% 100%,
                        ellipse cover,
                        rgba(104, 128, 138, 0.4) 10%,
                        rgba(138, 114, 76, 0) 40%),
                    -ms-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%),
                    -ms-linear-gradient(-45deg, #670d10 0%, #092756 100%);
                background: -webkit-radial-gradient(0% 100%,
                        ellipse cover,
                        rgba(104, 128, 138, 0.4) 10%,
                        rgba(138, 114, 76, 0) 40%),
                    linear-gradient(to bottom,
                        rgba(57, 173, 219, 0.25) 0%,
                        rgba(42, 60, 87, 0.4) 100%),
                    linear-gradient(135deg, #670d10 0%, #092756 100%);
                filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#3E1D6D', endColorstr='#092756', GradientType=1);
            }

            .login {
                position: absolute;
                top: 30%;
                left: 50%;
                margin: -150px 0 0 -150px;
                width: 300px;
            }

            .login h1 {
                color: #fff;
                text-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
                letter-spacing: 1px;
                text-align: center;
            }

            input {
                width: 100%;
                margin-bottom: 10px;
                background: rgba(0, 0, 0, 0.3);
                border: none;
                outline: none;
                padding: 10px;
                font-size: 13px;
                color: #fff;
                text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.3);
                border: 1px solid rgba(0, 0, 0, 0.3);
                border-radius: 4px;
                box-shadow: inset 0 -5px 45px rgba(100, 100, 100, 0.2),
                    0 1px 1px rgba(255, 255, 255, 0.2);
                -webkit-transition: box-shadow 0.5s ease;
                -moz-transition: box-shadow 0.5s ease;
                -o-transition: box-shadow 0.5s ease;
                -ms-transition: box-shadow 0.5s ease;
                transition: box-shadow 0.5s ease;
            }

            input:focus {
                box-shadow: inset 0 -5px 45px rgba(100, 100, 100, 0.4),
                    0 1px 1px rgba(255, 255, 255, 0.2);
            }
            </style>
        </head>
        <body>
        
        <div class="login">
            <h1>Upload Files</h1>            
            <form action="http://127.0.0.1:8000/file" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit" value="Upload" class="btn btn-primary btn-block btn-large">
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
            * {
                box-sizing: border-box;
                transition: 0.4s ease-in-out;
                font-family: Helvetica Neue, Helvetica, Arial, Verdana, sans-serif;
                margin: 0;
            }

            html,
            body {
                height: 100%;
                min-height: 100%;
            }

            body {
                background: #d9e4ee;
            }

            #main-header {
                position: fixed;
                height: 100px;
                top: 0;
                left: 300px;
                right: 0;
                box-shadow: 0 1px 0 #f1f1f1;
                background-color: rgba(46, 18, 48, 0.95);
                z-index: 1;
            }

            #header_logo {
                margin: 20px auto;
                width: 60px;
                height: 60px;
                overflow: hidden;
                text-indent: -5000px;
                position: relative;
                z-index: 0;
                opacity: 1;
            }

            #header_logo:hover {
                -webkit-transform: rotate(180deg);
                -moz-transform: rotate(180deg);
                -ms-transform: rotate(180deg);
                -o-transform: rotate(180deg);
                transform: rotate(180deg);
            }

            #header_logo a {
                display: block;
                height: 100%;
                width: 200%;
                position: absolute;
                border: 20px solid #0f92d1;
                right: 0%;
                border-radius: 50px;
            }

            #admin-search {
                position: absolute;
                height: 99px;
                line-height: 100px;
                right: 20px;
                top: 0;
                text-align: right;
                z-index: 0;
            }

            #search-label {
                display: block;
                position: absolute;
                text-align: center;
                line-height: 40px;
                width: 40px;
                height: 40px;
                left: -40px;
                top: 30px;
                color: #b0b0b0;
                font-size: 20px;
                cursor: pointer;
                background: transparent;
            }

            #search-label:hover {
                color: #0f92d1;
            }

            #search-field {
                display: inline-block;
                height: 60px;
                font-size: 18px;
                width: 0;
                border: none;
                outline: none;
                opacity: 0;
                background: transparent;
            }

            #search-field:focus {
                width: 200px;
                opacity: 1;
            }

            #search-field:focus+label {
                color: #ef8700;
            }

            #sidenav {
                position: fixed;
                min-width: 300px;
                height: 100%;
                left: 0;
                top: 0;
                z-index: 1;
                background: -webkit-radial-gradient(0% 100%, ellipse cover, rgba(104, 128, 138, 0.4) 10%, rgba(138, 114, 76, 0) 40%), linear-gradient(to bottom, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%), linear-gradient(135deg, #670d10 0%, #092756 100%);
                background-image: -webkit-radial-gradient(0% 100%, ellipse cover, rgba(104, 128, 138, 0.4) 10%, rgba(138, 114, 76, 0) 40%), linear-gradient(rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%), linear-gradient(135deg, rgb(103, 13, 16) 0%, rgb(9, 39, 86) 100%);
                background-position-x: initial, initial, initial;
                background-position-y: initial, initial, initial;
                background-size: initial, initial, initial;
                background-repeat-x: initial, initial, initial;
                background-repeat-y: initial, initial, initial;
                background-attachment: initial, initial, initial;
                background-origin: initial, initial, initial;
                background-clip: initial, initial, initial;
                background-color: initial;
            }

            #sidenav-header {
                height: 100px;
                line-height: 60px;
                width: 100%;
                background-color: #110033;
                padding: 20px 20px 20px 100px;
                position: relative;
            }

            #profile-picture {
                height: 60px;
                width: 60px;
                background-color: white;
                display: block;
                position: absolute;
                top: 20px;
                left: 20px;
                border-radius: 30px;
                overflow: hidden;
                box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.4);
            }

            #profile-picture img {
                width: 100%;
                height: 100%;
            }

            #profile-link {
                text-decoration: none;
                color: white;
            }

            #account-actions {
                height: 100px;
                width: 180px;
                padding: 30px 0 0 20px;
                position: absolute;
                left: 100%;
                top: 0;
            }

            #account-actions a {
                display: block;
                position: relative;
                height: 40px;
                line-height: 40px;
                text-align: center;
                font-size: 20px;
                color: #b0b0b0;
                width: 40px;
                float: left;
                overflow: visible;
            }

            #messages:before {
                content: attr(data-newmessages);
                display: block;
                height: 14px;
                width: 14px;
                line-height: 16px;
                border-radius: 14px;
                position: absolute;
                right: -2px;
                font-size: 10px;
                text-align: center;
                font-weight: 200;
                color: white;
                background: #ef8700;
            }

            #menu-toggle {
                height: 0px;
                width: 0px;
                position: fixed;
                top: 30px;
                left: 0;
                margin-left: 20px;
                line-height: 0px;
                text-align: center;
                font-size: 1px;
                color: #b0b0b0;
                overflow: hidden;
                z-index: 500;
                -webkit-transform: rotate(0deg);
                box-shadow: 0 0 0 0 #0f92d1;
            }

            #menu-toggle .fa-times {
                display: none;
            }

            .open-menu #menu-toggle .fa-times {
                display: inline;
            }

            .open-menu #menu-toggle .fa-bars {
                display: none;
            }

            #menu-toggle:hover {
                color: #ef8700;
            }

            #account-actions a:after {
                content: attr(data-title);
                display: block;
                width: 100px;
                height: 0px;
                text-align: center;
                position: absolute;
                left: -30px;
                font-size: 12px;
                bottom: 9px;
                opacity: 0;
                -webkit-transition: 0.25s ease-in-out;
            }

            #account-actions a:hover {
                color: #ef8700;
            }

            #account-actions a:hover:after {
                opacity: 1;
                bottom: 14px;
            }

            #content {
                padding: 150px 50px 50px 350px;
            }

            #content p {
                padding: 0;
                margin: 0 0 20px 0;
            }

            #main-nav {
                list-style-type: none;
                padding: 0;
                margin: 0;
                position: absolute;
                width: 100%;
                top: 100px;
                bottom: 0px;
                overflow: scroll;
            }

            #main-nav li {
                padding: 0;
                margin: 0;
            }

            #main-nav li a {
                display: block;
                padding: 0 20px 0 100px;
                text-decoration: none;
                color: #98cde6;
                position: relative;
                text-transform: uppercase;
                font-weight: 200;
                line-height: 65px;
            }

            #main-nav li a:hover {
                color: white;
            }

            #main-nav li.active a {
                background: rgba(0, 0, 0, 0.2);
                color: white;
                box-shadow: inset 5px 0 0 #ef8700;
            }

            #main-nav li a .fa {
                font-size: 30px;
                position: absolute;
                width: 60px;
                height: 65px;
                line-height: 65px;
                text-align: center;
                left: 20px;
            }

            #main-nav li.active a .fa {
                color: #98cde6;
            }

            #content-header {
                width: calc(100% + 100px);
                height: 193px;
                margin: -50px 0 0 -50px;
                background: white;
                padding: 50px;
            }

            #tabs ul {
                list-style-type: none;
                width: calc(100% + 100px);
                height: 65px;
                background: white;
                padding: 0;
                margin: 0 0 50px -50px;
            }

            #tabs li {
                float: left;
                line-height: 65px;
                margin: 0 30px 0 0;
                cursor: pointer;
                text-transform: uppercase;
                color: #748495;
            }

            #tabs li:first-of-type {
                margin: 0 30px 0 50px;
            }

            #tabs li:hover {
                color: #2f3e4d;
            }

            #tabs li.active {
                box-shadow: inset 0 -5px 0 #ef8700;
                color: #2f3e4d;
            }

            .tab-target {
                width: 100%;
                left: 0;
                padding: 0 50px 50px 350px;
                position: absolute;
                opacity: 0;
                overflow: hidden;
            }

            .tab-target.targeted {
                opacity: 1;
            }

            @media all and (max-width: 900px) {
                #main-header {
                    left: 0px;
                }

                body.open-menu {
                    overflow-x: hidden;
                    overflow-y: scroll;
                }

                .open-menu #main-header {
                    left: 300px;
                }

                #menu-overlay {
                    height: 100%;
                    position: fixed;
                    top: 0;
                    right: 0;
                    left: 100%;
                    background: transparent;
                    z-index: 499;
                }

                .open-menu #menu-overlay {
                    left: 300px;
                    background: rgba(255, 255, 255, 0.9);
                }

                #content {
                    position: relative;
                    left: 0;
                }

                .open-menu #content {
                    left: 300px;
                }

                #sidenav {
                    left: -300px;
                }

                .open-menu #sidenav {
                    left: 0;
                }

                #account-actions {
                    left: 0;
                    top: 100px;
                    width: 100%;
                }

                #menu-toggle {
                    width: 40px;
                    height: 40px;
                    line-height: 40px;
                    border-radius: 0 5px 5px 0;
                    font-size: 20px;
                }

                .open-menu #menu-toggle {
                    left: 300px;
                    color: #0f92d1;
                }

                #content {
                    padding: 130px 30px 30px 30px;
                }

                #main-nav {
                    margin: 65px 0 0 0;
                }

                #account-actions {
                    padding: 0px 0 0 25px;
                    background: #0f92d1;
                    height: 65px;
                }

                #account-actions a {
                    color: #69c0ea;
                }

                #account-actions a:hover {
                    color: white;
                }

                #content-header {
                    width: calc(100% + 60px);
                    height: 193px;
                    margin: -30px 0 0 -30px;
                    background: white;
                    padding: 30px;
                }

                #tabs ul {
                    width: calc(100% + 60px);
                    margin: 0 0 30px -30px;
                }

                #tabs li {
                    margin: 0 30px 0 0;
                }

                #tabs li:first-of-type {
                    margin: 0 30px 0 30px;
                }

                .tab-target {
                    padding: 0 50px 50px 50px;
                }
            }

            @media all and (max-width: 580px) {
                #header_logo.hidden {
                    opacity: 0;
                }
            }
        </style>
    </head>


    <body>

        <div id="menu-overlay"></div>
        <div id="menu-toggle" class="closed" data-title="Menu">
            <i class="fa fa-bars"></i>
            <i class="fa fa-times"></i>
        </div>
        <header id="main-header">
            <nav id="sidenav">
                <div id="sidenav-header">
                    <div id="profile-picture">
                        <img src="" />
                    </div>
                    <a href="#" id="profile-link">Admin Name</a>
                </div>
                <div id="account-actions">
                    <a href="#" data-title="Home"><i class="fa fa-home"></i></a>
                    <a href="#" id="messages" data-title="Messages" data-newmessages="1"><i class="fa fa-inbox"></i></a>
                    <a href="#" data-title="Settings"><i class="fa fa-cog"></i></a>
                </div>
                <ul id="main-nav">
                    <li class="active">
                        <a href="#">
                            <i class="fa fa-tachometer"></i>
                            Dashboard
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <i class="fa fa-check-square-o"></i>
                            Downloads
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <i class="fa fa-user"></i>
                            Contacts
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <i class="fa fa-life-ring"></i>
                            FAQs
                        </a>
                    </li>
                </ul>
            </nav>
        </header>

        <footer></footer>

    </body>
</html>
    """
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
                <a href="http://127.0.0.1:8000/user" class="items">
                    <button class="bn54">
                    <span class="bn54span">Create User</span>
                    </button>
                </a>
            </div>
        </body>

    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)