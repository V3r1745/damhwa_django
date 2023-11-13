from django.urls import path
from web_api.views import add_cart, add_cart_item, delete_cart, get_festa, mod_cart_item_count, pro_list, pro_one, get_cart

urlpatterns = [
    path("product/", pro_list),
    path("pro/", pro_one),
    path("bucket/get/", get_cart),
    path("bucket/new/", add_cart),
    path("bucket/add/", add_cart_item),
    path("bucket/delete/", delete_cart),
    path("bucket/mode/", mod_cart_item_count),
    path("festa/", get_festa)
]
