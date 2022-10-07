from django.shortcuts import render, redirect
from django.http import HttpResponse
from animator_service import animate


def create_animation_by_name(request, animation_name):
    return HttpResponse(animate.animate(animation_name))


def home(request):
    return create_animation_by_name(request, 'basic_dfs')
