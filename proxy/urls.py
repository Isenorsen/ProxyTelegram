from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('proxy', views.ProxySerView)


urlpatterns = [
    path('send/', views.contact_form),
    path('add/', views.proxy_add),
    path('api/v1/', include(router.urls)),
    path('', views.proxy_list),
]