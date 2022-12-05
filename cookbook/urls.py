from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('recipeposts/', views.RecipeList.as_view(), name='recipe_posts'),
]