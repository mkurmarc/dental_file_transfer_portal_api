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
        <form method="POST" action="/user/create">
            <input class="items" type="text" name="first_name" placeholder="First Name" size="30" required>
            <input class="items" type="text" name="last_name" placeholder="Last Name" size="30" required>
            <input class="items" type="text" name="company_name" placeholder="Company Name" size="50">
            <input class="items" type="email" name="email" placeholder="your@email.com" size="30" required>
            <input class="items" type="email" name="confirm_email" placeholder="Confirm Email" size="30" required>
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
        <form method="POST" action="/login">
            <input class="items" type="email" name="email" placeholder="your@email.com" size="30" required>
            <input class="items" type="password" name="password" placeholder="password" size="20" required>
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
            <form action="/uploadfiles" enctype="multipart/form-data" method="POST">
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