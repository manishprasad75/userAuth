1. Make sure you have python3 installed
2. First you have to install all the requirements so,
    pip install -r requirements.txt

3. There are five Route


4. For Registration:-
    EndPoint:- api/register/
    Method:- POST
    json_data = {
        "email": String,
        "password": String(len >= 8)
    }


5. Email Verification:-
    EndPoint:- api/verification/
    Method:- GET, POST

    GET:-
    Send the OTP to provided email and also json response of email, otp, msg

    json_data = {
        "email": String
    }

    Response:- (Success)
    json_data = {
        "msg": String,
        "email": String,
        "otp": String
    }

    POST:-
    Verify given email and otp

    json_data = {
        "email": String,
        "otp": String
    }


 6. Login:-
    EndPoint:- api/login/
    Methods:- POST
    json_data = {
        "email": String,
        "password": String,
    }




 7. Token:-
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


 Note:-
1. For every request (except registration), please provide Authorization Token
2. Email Credential:-
    In settings.py at line 136 and 137, please provide username and password to send email