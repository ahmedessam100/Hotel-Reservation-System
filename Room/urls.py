from django.conf.urls import url
from . import views

urlpatterns = [
    # r is regex , ^ is start , $ is the end
    url(r'^addRoom', views.addRoom , name='addRoom' ),
    #extract the integer
    #url(r'^(?P<album_id>[0-9]+)$', views.detail , name='detail' ),
]