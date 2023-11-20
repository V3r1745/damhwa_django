import json
import re
from rest_framework.response import Response
from rest_framework.decorators import api_view
from passlib.hash import pbkdf2_sha256
from login_api.models import Account
from login_api.exception import EmptyResult, EmptyQuery, SameAccountException, WrongSyntax, NotMatched

# Create your views here.

@api_view(["GET"])
def check_id(request):
  try:
    input_id = request.GET.get("id")

    if (input_id is None or input_id == ""):
      raise EmptyQuery

    result = Account.objects.filter(user_id = input_id)

    if (len(result) == 0):
      raise EmptyResult

  except EmptyResult as e:
    print(e)
    return Response({"result": {"error": str(e)}})

  except EmptyQuery as e:
    print(e)
    return Response({"result": {"error": str(e)}}, status = 400)

  except Exception as e:
    print(e)
    return Response({"result": {"error": str(e)}}, status = 400)

  else:
    return Response({"match": True})

@api_view(["GET"])
def check_account(request):
  input_id = request.GET.get("id")
  input_pw = request.GET.get("pw")
  result_pw = None

  try:
    if input_id is None or input_id == "" or input_pw is None or input_pw == "":
      raise EmptyQuery("id" if input_id is None or input_id == "" else "", "pw" if input_pw is None or input_pw == "" else "")

    account_results = Account.objects.filter(user_id = input_id)

    if len(account_results) != 1:
      raise SameAccountException(input_id)

    account_result = account_results[0]

    if (not pbkdf2_sha256.verify(input_pw, account_result.user_pw)):
      raise NotMatched
    else:
      result_pw = account_result.user_pw

  except NotMatched as e:
    print(e)

    return Response({"result": {"error": str(e)}}, status = 404)

  except EmptyQuery as e:
    print(e)
    return Response({"result": {"error": str(e)}}, status = 400)

  except Exception as e:
    print(e)
    return Response({"result": {"error": str(e)}}, status = 400)

  else:
    response = Response({"result": True})
    response.set_cookie("id", input_id, samesite="Lax")
    response.set_cookie("pw", result_pw, samesite="Lax")

    return response

@api_view(["POST"])
def create_account(request):
  request_body = json.loads(request.body)
  input_id = request_body.get("id")
  input_pw = request_body.get("pw")

  try:
    print("id", input_id)
    print("pw", input_pw)

    if input_id == "" or input_id is None or input_pw == "" or input_pw is None:
      raise EmptyQuery("id" if input_id == "" or input_id is None else "", "password" if input_pw == "" or input_pw is None else "")

    check_same = Account.objects.filter(user_id = input_id)

    if len(check_same) != 0:
      raise SameAccountException(input_id)

    if (re.search(r"\W", input_id)):
      raise WrongSyntax("id" if re.search(r"\W", input_id) else "")

  except SameAccountException as e:
    print(e)

    return Response({"result": {"error": str(e)}}, status = 400)

  except EmptyQuery as e:
    print(e)

    return Response({"result": {"error": str(e)}}, status = 400)

  except WrongSyntax as e:
    print(e)

    return Response({"result": {"error": str(e)}}, status = 400)

  except Exception as e:
    print(e)

    return Response({"result": {"error": str(e)}}, status = 400)

  else:
    Account.objects.create(user_id = input_id, user_pw = pbkdf2_sha256.hash(input_pw))

    return Response({"result": "success"})
