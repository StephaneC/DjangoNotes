from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from notes import views
 
urlpatterns = [
    url(r'^notes/$', views.notes_list_api, name='notes')
   #url(r'^notes/(?P<pk>[0-9]+)/$', views.NoteD.as_view(), name='note-detail'),
]