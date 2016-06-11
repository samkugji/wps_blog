from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect


def logout(request):
    auth_logout(request)
    return redirect(reverse("home"))
