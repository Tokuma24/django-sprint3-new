from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .constants import POSTS_ON_MAIN_PAGE


def index(request):
    """Главная страница: последние опубликованные посты."""
    posts = Post.published.filter(
        category__is_published=True,
    )[:POSTS_ON_MAIN_PAGE]
    context = {
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    """Страница категории: посты конкретной опубликованной категории."""
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    posts = Post.published.filter(category=category)

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category.html', context)


def post_detail(request, id):
    """Детальная страница поста."""
    post = get_object_or_404(
        Post.published,
        id=id,
        category__is_published=True,
    )
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)
