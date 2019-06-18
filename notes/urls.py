from django.urls import path,include,re_path
from . import views
from .views import *

urlpatterns = [
    re_path(r'^register/$',views.RegistrationView.as_view()), #registration of new users
    re_path(r'^notes/$',NoteList.as_view()), #todo endpoint
    re_path('<pk>/',NoteLists.as_view()),
    re_path(r'^oauth2/',include('oauth2_provider.urls',namespace='oauth2')),
    re_path(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),

   
]

    