from django.urls import path
from .views import(signUp,signinStatus,fetchInbox,addMail,deleteMail,starMail,sentMail)
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'
urlpatterns = [
path('signUp', signUp, name="signUp"),
path('signinStatus', signinStatus, name="signinStatus"),
path('fetchInbox', fetchInbox, name="fetchInbox"),
path('addMail', addMail, name="addMail"),
path('deleteMail', deleteMail, name="deleteMail"),
path('starMail', starMail, name="starMail"),
path('sentMail', sentMail, name="sentMail"),
]