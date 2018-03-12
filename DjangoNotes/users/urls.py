from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views
 
urlpatterns = [
    url(r'^users/$', views.user_list_api, name='users-list'),
]