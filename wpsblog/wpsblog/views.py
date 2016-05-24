import requests

from django.http.response import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello World</h1><p>This is blog</p>")


def room(request, room_id):
    # 방 번호 (room_id) 직방의 데이터를 그대로 보여주는 장고 뷰(MVC 컨트롤러)
    base_url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(base_url)
    
    return HttpResponse(
        response.content,
        content_type="application/json",
    )
