from . import views
from django.urls import path


app_name = "chat"

urlpatterns = [
    path('', views.ListSendMessage.as_view(), name = "send"),
    path('receive', views.ReceiveMessage.as_view(), name = "receive"),
]