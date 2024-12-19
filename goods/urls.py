from operator import index
from django.urls import include, path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index' ),
    path('product/', views.product, name='product' ),
]
