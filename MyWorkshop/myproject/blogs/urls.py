from django.urls import path
from .views import index,blogDetail

urlpatterns=[
    path('',index),
    path('blog/<int:id>',blogDetail,name="blogDetail")
]