from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from passlib.hash import pbkdf2_sha256

# Create your views here.

@api_view(["GET"])
def check_id(request):
  print(request)
  return Response()

@api_view(["GET"])
def check_account(request):
  return Response()

@api_view(["POST"])
def create_account(request):
  input_pw = request.POST.get("pw")
  input_id = request.POST.get("id")
  print(pbkdf2_sha256.hash(input_pw))
  print(input_pw)
  return Response()
