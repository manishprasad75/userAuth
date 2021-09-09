from .models import UserProfile, OTP
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from .utility import isvalid, getOTPValue, sendMessage
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.


class UserRegister(APIView):
    """
    User Registration
    Post Request
    Email:- String
    Password:- String (length greater than 8)
    """

    def post(self, request, format=None):
        json_data = request.body
        stream = io.BytesIO(json_data)
        try:
            context = JSONParser().parse(stream)
        except:
            return JsonResponse({'msg': 'Invalid Json'}, status=400)

        (status, msg) = isvalid(context)
        user = User.objects.filter(username=context.get('email')).first()
        if user is not None:
            return JsonResponse({'msg': 'Error: Email Already Exist'}, status=400)
        if status:
            user = User.objects.create_user(context.get('email'), context.get('email'), context.get('password'))
            user.save()

            userprofile = UserProfile(is_valid=False, user_id=user)
            userprofile.save()

            return JsonResponse({'msg': 'Successfully Created!!'})
        else:
            return JsonResponse({'msg': msg}, status=400)


class UserEmailVerification(APIView):
    """
    GET Request:-
    email:- String
    return:-
    otp:- String (Also send otp at email if valid)

    POST Request:-
    email:- String
    otp:- String

    if valid than make is_valid property to true
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        json_data = request.body
        stream = io.BytesIO(json_data)
        try:
            context = JSONParser().parse(stream)
        except Exception as e:
            return JsonResponse({'msg': 'Invalid Json'}, status=400)

        email = context.get('email').strip()

        user = User.objects.filter(email=email).first()
        if user is None:
            return JsonResponse({'msg': 'Invalid Email'}, status=400)

        otp = OTP.objects.filter(user_id=user).first()

        if otp is not None:
            value = getOTPValue()
            otp.value = value
            otp.save()
        else:
            value = getOTPValue()
            otp = OTP(value=value, user_id=user)
            otp.save()

        if sendMessage(user, otp):
            return JsonResponse({'msg': 'Email Send Successfully', 'email': email, 'otp': value})
        else:
            return JsonResponse({'msg': "Email Invalid"}, status=400)



    def post(self, request, format=None):
        json_data = request.body
        stream = io.BytesIO(json_data)
        try:
            context = JSONParser().parse(stream)
        except Exception as e:
            return JsonResponse({'msg': 'Invalid Json'}, status=400)

        email = context.get('email').strip()
        otp_val = context.get('otp').strip()

        if email is None:
            return JsonResponse({'msg': 'Email not provided'}, status=400)

        if otp_val is None:
            return JsonResponse({'msg': 'OTP not provided'}, status=400)

        user = User.objects.filter(username=email).first()
        if user is None:
            return JsonResponse({'msg': 'Invalid email'}, status=400)

        otp = OTP.objects.filter(value=otp_val).first()

        if otp is None:
            return JsonResponse({'msg': 'Invalid OTP'}, status=400)

        if otp.user_id_id == user.id:
            userprofile = UserProfile.objects.filter(user_id=user).first()
            try:
                userprofile.is_valid = True
                userprofile.save()
                otp.value = ""
                otp.save()
                return JsonResponse({'msg': 'Email Verified Successfully'})
            except Exception as e:
                return JsonResponse({'msg': e}, status=500)
        else:
            return JsonResponse({'msg': 'Invalid OTP'}, status=400)




class UserLogIn(APIView):
    """
    Login the user
    Post request
    email:- String
    password:- String
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        json_data = request.body
        stream = io.BytesIO(json_data)
        try:
            context = JSONParser().parse(stream)
        except:
            return JsonResponse({'msg': 'Invalid Json'}, status=400)

        email = context.get('email')
        password = context.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            if not user.profile.is_valid:
                return JsonResponse({'msg': "Error Email not verified"}, status=403)

            login(request, user)
            return JsonResponse({'msg': "Login Successfully"})
        else:
            return JsonResponse({'msg': "Email or Password not valid"})


class UserLogout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, reqeust, format=None):
        logout(reqeust)
        return JsonResponse({'msg': "Logout Successfully"})
