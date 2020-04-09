"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from food import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('food/', views.FoodListView.as_view(), name="list"),
    path('food/detail/<int:food_id>/', views.FoodDetailView.as_view(), name='detail'),
    # path('food/<int:food_id>/create/', views.PokemonCreateView.as_view(), name='create'),
    # path('food/<int:food_id>/update/', views.PokemonUpdateView.as_view(),name='update'),
    #Authentication
    path('login/', TokenObtainPairView.as_view(), name='login'),
    # path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('register/', views.RegisterView.as_view(), name='register'),

]
