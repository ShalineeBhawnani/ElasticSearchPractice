from django.urls import path, include ,re_path
from . import views
app_name = 'product'
urlpatterns = [ 
    re_path(r'^product/+(?P<id>\d+)?', views.ProductView.as_view(), name ='product'),
] 