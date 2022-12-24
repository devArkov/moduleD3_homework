from django.urls import path

from . import views


urlpatterns = [
    path('', views.NewsListView.as_view()),
    path('<int:pk>', views.SingleNewsView.as_view()),
]