from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage,name="landingPage"),
    path("loginPage/", views.loginPage, name="loginPage"),
    path("registerPage/", views.registerPage, name="registerPage"),
    path("infoList/", views.infoLists, name="infoList"),
    path("quesList/", views.quesLists, name="quesList"),
    path("infoDelete/", views.infoDelete, name="infoDelete"),
    path("quesDelete/", views.quesDelete, name="quesDelete"),
    path("priceList/", views.priceLists, name="priceList"),
    path("addPrice/", views.addPrice, name="addPrice"),
    path("priceDelete/", views.priceDelete, name="priceDelete"),
    path("priceEdit/<int:nid>/", views.editPrice, name="priceEdit"),
    path("imageList/", views.imageList, name="imageList"),
    path("addImage/", views.addImage, name="addImage"),
]