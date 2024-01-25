from django.urls import path
from . import views

urlpatterns = [
    path("",views.api_view),
    path("api/",views.ReactCreateAPIView.as_view()),
    
]
