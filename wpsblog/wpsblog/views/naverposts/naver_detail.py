from django.shortcuts import render


def naver_detail(request):
    return render(
        request,
        "naverposts/detail.html",
        {},
    )
