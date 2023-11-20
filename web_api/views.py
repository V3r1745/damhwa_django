from rest_framework.response import Response
from rest_framework.decorators import api_view
from web_api.models import Festival, Product, Bucket
from django.core import serializers
import json
from web_api.exception import AlreadyItemIsExist, ParameterNoneError, SameIdIsExist, SameUserBucketError, CookieIsNoneException, UserBucketIsNotFound

# Create your views here.

@api_view(["GET"])
def pro_list(request):
  result = json.loads(serializers.serialize("json",
                                            Product.objects.filter(product_type = int(request.GET.get("type")))))[(int(request.GET.get("page")) - 1) *
                                                                                                                  4:int(request.GET.get("page")) * 4]

  return Response(result)

@api_view(["GET"])
def pro_one(request):
  result = json.loads(serializers.serialize("json", Product.objects.filter(pk = int(request.GET.get("pk")))))

  return Response(result)

# 카트 수정

@api_view(["GET"])
def get_cart(request):
  result = None
  try:
    user_id = request.COOKIES.get("id")

    if user_id is None or user_id == "":
      raise CookieIsNoneException

    if not Bucket.objects.filter(user_id = user_id):
      raise UserBucketIsNotFound

    result = json.loads(serializers.serialize("json", Bucket.objects.filter(user_id = user_id)))

  except CookieIsNoneException as e:
    print(e)

    return Response(str(e), status = 400)

  except UserBucketIsNotFound as e:
    print(e)

    return Response(str(e), status = 404)

  except Exception as e:
    print(e)

    return Response(str(e), status = 400)

  else:
    return Response({"result": result})

@api_view(["POST"])
def add_cart(request):
  try:
    user_id = json.loads(request.body).get("id")

    if Bucket.objects.filter(user_id = user_id):
      raise SameUserBucketError(user_id)

    Bucket.objects.create(user_id = user_id)

  except SameUserBucketError as e:
    print(e)

    return Response(str(e), status = 400)

  except Exception as e:
    print(e)

    return Response(str(e), status = 400)

  else:
    return Response({"result": True})

@api_view(["PUT"])
def add_cart_item(request):
  try:
    user_id = request.COOKIES.get("id")

    if not Bucket.objects.filter(user_id = user_id):
      raise UserBucketIsNotFound

    bucket_json = Bucket.objects.filter(user_id = user_id)

    if len(bucket_json) > 1:
      raise SameIdIsExist(user_id)

    if not (request.GET.get("url") and request.GET.get("name") and request.GET.get("price") and request.GET.get("count")):
      raise ParameterNoneError

    # {url: "", name: "name", price: "price", count: "count"}

    add_json = {
        "url": request.GET.get("url"),
        "name": request.GET.get("name"),
        "price": request.GET.get("price"),
        "count": request.GET.get("count"),
    }

    print(add_json)

    mode_json = bucket_json.first().bucket_list

    print(mode_json)

    if len(list(filter(lambda v: v.get("name") == request.GET.get("name"), mode_json))) != 0:
      raise AlreadyItemIsExist(request.GET.get("name"))

    mode_json.append(add_json)
    bucket_json.update(bucket_list = mode_json)

  except UserBucketIsNotFound as e:
    print(e)

    return Response(str(e), status = 404)

  except ParameterNoneError as e:
    print(e)

    return Response(str(e), status = 400)

  except AlreadyItemIsExist as e:
    print(e)

    return Response(str(e), status = 400)

  except Exception as e:
    print(e)

    return Response(str(e), status = 400)

  else:
    return Response("success")

@api_view(["PATCH"])
def mod_cart_item_count(request):
  try:
    req_body = json.loads(request.body).get("data")

    bucket_object = Bucket.objects.filter(user_id = request.COOKIES.get("id"))

    if len(bucket_object) > 1:
      raise SameIdIsExist(request.COOKIES.get("id"))

    update_target = bucket_object.first()

    bucket_list = update_target.bucket_list
    bucket_list[req_body.get("num")]["count"] = req_body.get("count")

    bucket_object.update(bucket_list = bucket_list)

    return Response()

  except Exception as e:
    print(e)

    return Response(str(e), status = 400)

@api_view(["DELETE"])
def delete_cart(request):
  try:
    bucket_result = Bucket.objects.filter(user_id = request.COOKIES.get("id"))

    if len(bucket_result) > 1:
      raise SameUserBucketError

    bucket_json = bucket_result.first().bucket_list
    print(bucket_json)

    delete_list = json.loads(request.body)

    result = [v for i, v in enumerate(bucket_json) if i not in delete_list]

    print(result)

    bucket_result.update(bucket_list = result)

    return Response("success")
  except SameUserBucketError as e:
    print(e)

    return Response(str(e), status = 400)

  except Exception as e:
    print(e)

    return Response(e, status = 400)

@api_view(["DELETE"])
def delete_all(request):
  return Response("success")

@api_view(["GET"])
def get_festa(request):
  festival = json.loads(serializers.serialize("json", Festival.objects.all()))
  return Response(festival)
