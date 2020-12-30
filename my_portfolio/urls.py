from django.conf.urls import url
from my_portfolio import views

app_name='my_portfolio'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^projects',views.projects,name='projects'),
    url(r'^info',views.info,name='info'),
    url(r'^msg',views.messages.as_view(),name='msgs')
    ]
