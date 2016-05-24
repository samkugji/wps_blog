from django.conf.urls import url
from django.contrib import admin

from django.http.response import HttpResponse

# MVC Controller
def home(request):
    return HttpResponse("Hello World")

def room(request, room_id):
    return HttpResponse("This is a room detail")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^$', home),
    url(r'rooms/(?P<room_id>\d+)/$', room),

]

