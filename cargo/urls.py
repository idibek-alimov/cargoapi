from django.urls import path
from .views import CalculatorDataList, ClientList  # ,ProductDetail,ProductList
urlpatterns = [
    # path("<int:pk>/", MessageDetail.as_view(), name="message_detail"),
    # path("", MessageList.as_view(), name="message_list"),
    path("client/", ClientList.as_view(), name="client_list"),
    path("calculator/", CalculatorDataList.as_view(), name="calculator_list")
    # path("product/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    # path("product/", ProductList.as_view(), name="product_list"),
]
