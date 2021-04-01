from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import RegistrationSerializer,SignInStautsSerializer,MailSerializer,SMailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import login as django_login, logout as django_logout
from .models import Mail
# Create your views here.

@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def signUp(request):
    serializer = RegistrationSerializer(data=request.data)
    username=request.data.get('username')
    first_name=request.data.get('first_name')
    last_name=request.data.get('last_name')
    password=request.data.get('password')
    data = {}
    if validate_username(username) != None:
            data['error_message'] = 'That username is already in use.'
            data['response'] = 'Error'
            return Response(data,status=201)
    myuser = User.objects.create_user(username, '',password)
    myuser.first_name = first_name
    myuser.last_name = last_name
    myuser.save()
    user = authenticate(username=username, password=password)
    if user is not None:
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        data['token'] = str(token)
        data['username'] = username
    print(username,first_name,last_name,password)
    return Response(data,status=200)

def validate_username(username):
    account = None
    try:
        account = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    if account != None:
        return username
 
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def signinStatus(request):
    serializer = SignInStautsSerializer(data=request.data)
    token=request.data.get('token')
    token = Token.objects.filter(key=token)
    print(token[0].user.username)
    user={'username':token[0].user.username,'first_name':token[0].user.first_name,'last_name':token[0].user.last_name}
    if len(token) > 0:
        return Response({'Response': user}, status=200)
    else:
        return Response({'Response': 'ok'}, status=201)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def fetchInbox(request):
    mail=Mail.objects.filter(to=request.user.username).order_by('-timeStamp').values()
    inbox=[]
    for item in mail:
        user=User.objects.filter(id=int(item['sender_id'])).values()
        inbox.append([user[0],item])
    return Response({'Response': inbox}, status=200)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def addMail(request):
    serializer = MailSerializer(data=request.data)
    subject=request.data.get('subject')
    text=request.data.get('text')
    to=request.data.get('to')
    mail=Mail(subject=subject,text=text,to=to[:-10],sender=request.user)
    mail.save()
    return Response({'Response': 'ok'}, status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def deleteMail(request):
    serializer = SMailSerializer(data=request.data)
    sno=int(request.data.get('sno'))
    mail=Mail.objects.get(sno=sno)
    mail.delete()
    return Response({'Response': 'ok'}, status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def starMail(request):
    serializer = SMailSerializer(data=request.data)
    sno=int(request.data.get('sno'))
    mail=Mail.objects.get(sno=sno)
    mail.isStarred=True
    mail.save()
    return Response({'Response': 'ok'}, status=200)
    
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def sentMail(request):
    mail=Mail.objects.filter(sender=request.user).values()
    return Response({'Response': mail}, status=200)