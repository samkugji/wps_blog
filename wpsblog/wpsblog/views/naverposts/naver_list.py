from django.shortcuts import render


def naver_list(request):
    return render(
        request,
        "naverposts/list.html",
        {},
    )
