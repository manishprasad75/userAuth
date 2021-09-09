1. Make sure you have Python 3.8.10 installed
2. First you have to install all the requirements so,
    pip install -r requirements.txt

3. There are five Route

A. Generate Token:-
    EndPoint:- api/gettoken/
    Methods:- POST
    json_data = {
        "username": String (email)
        "password": String
    }

    Response:-
    json_data = {
        "token": String(key)
    }

B. Registration:-
    EndPoint:- /api/register/
    Method:- POST
    json_data = {
        "email": String,
        "password": String(len >= 8)
    }

C. Email Verification:-
    Send the OTP to provided email and also json response of email, otp, msg
        EndPoint:- /api/verification/
        Method:- GET

        json_data = {
            "email": String
        }

        Response:- (Success)
        json_data = {
            "msg": String,
            "email": String,
            "otp": String
        }

    Verify given email and otp
        EndPoint:- /api/verification/
        Method:- POST

        json_data = {
            "email": String,
            "otp": String
        }

D. Login:-
    EndPoint:- api/login/
    Methods:- POST
    json_data = {
        "email": String,
        "password": String,
    }

Note:-
1. For every request (except registration), please provide Authorization Token
2. Email Credential:-
    In settings.py at line 136 and 137, please provide email and password to send email (Ideally which should be loaded from environment, done only for ease in testing)
