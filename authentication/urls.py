from django.urls import path
from authentication.views import login, register, proxy_image, create_news_flutter, logout

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_news_flutter, name='create_news_flutter'),
    path('logout/', logout, name='logout'),
]