from django.urls import path
from .views import home, sign_up, create_post

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('sign-up/', sign_up, name='sign-up'),
    path('create-post/', create_post, name='create-post'),
]

# Kiro pass b63#r]y;%TwevmL