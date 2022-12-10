from django.shortcuts import render, redirect, get_object_or_404, reverse 
from django.views import generic, View
from .models import Recipe, Submission
from .forms import CommentForm, SubmitRecipeForm
from django.http import HttpResponseRedirect


class HomePage(generic.TemplateView):
    template_name = 'index.html'


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipe_posts.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'recipe_detail.html',
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
            )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'recipe_detail.html',
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
            )


class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):

        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class SubmissionPage(generic.ListView):

    model = Submission
    queryset = Submission.objects.all()

    template_name = 'user_submissions.html'
    paginate_by = 8


def submit_recipe(request):

    if request.method == 'POST':

        submission_form = SubmitRecipeForm(request.POST, request.FILES)

        if submission_form.is_valid():
            submission_form.instance.user = request.user
            submission_form.save()

            return redirect('submissions')
        else:
            submission_form = SubmitRecipeForm()

    return render(
            request, 
            'submit_recipe.html',
            {
                'submission_form': SubmitRecipeForm(),
            },
        )