from .views import PageView, TaskView, RedirectedPageView
from django.urls import path

app_name = 'pages'

urlpatterns = [
    path('', PageView.as_view(), name='page'),
    path('task/', TaskView.as_view(), name='task_view'),
    path('redirected_page/', RedirectedPageView.as_view(), name='redirected_page'),
]