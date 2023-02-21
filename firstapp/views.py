from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# Create your views here.


class FirstView(View):
    def get(self, request):
        return JsonResponse({"hello": "world-get"})

    def post(self, request):
        return JsonResponse({"hello": "world-post"})

    def put(self, request):
        return JsonResponse({"hello": "world-put"})

    def delete(self, request):
        return JsonResponse({"hello": "world-delete"})
def functionview(request):
    return JsonResponse({"hey":"it works"})