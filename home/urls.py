from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('price', views.price, name='pricePage'),
    path('ourwork', views.our_work, name='ourWorkPage'),
    path('ourwork/<int:pk>', views.our_work_photo, name='ourWorkPhotoPage'),
    path('login',views.login_user, name='login'),
    path('addSlide', views.addSlideImage, name='addSlideImage'),
]