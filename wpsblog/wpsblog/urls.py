from django.conf.urls import url
from django.contrib import admin

from django.http.response import HttpResponse

# MVC Controller
def home(request):
    return HttpResponse("Hello World")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^$', home),

]

