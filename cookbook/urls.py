from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('recipeposts/', views.RecipeList.as_view(), name='recipe_posts'),
    path(
        'user_submissions/', views.SubmissionPage.as_view(
        ), name='submissions'),
    path('submitrecipe/', views.submit_recipe, name='submit_recipe'),
    path(
        'user_submissions/<slug:slug>', views.SubmissionDetail.as_view(), name='submission_detail'),
    path('user_submissions/<slug:slug>/', views.edit_submission, name='edit_submission'),
    path('user_submission/<slug:slug>/', views.delete_submission, name='delete_submission'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
]
