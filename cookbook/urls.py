from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('recipeposts/', views.RecipeList.as_view(), name='recipe_posts'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path(
        'user_submissions/', views.SubmissionPage.as_view(), name='submissions'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]