"""request_generator URL Configuration

TODO:
    * formのchoiceをファイル読み込みに変更する
"""

from django.urls import path
from . import views

app_name = 'main_page'
urlpatterns = [
    #path('', views.IndexView.as_view(), name="index"),
    path('request/', views.RequestView.as_view(), name="request"),
]
