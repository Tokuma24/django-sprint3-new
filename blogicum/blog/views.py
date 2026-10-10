from django.shortcuts import get_object_or_404, render

from blog.constants import POSTS_ON_MAIN_PAGE
from blog.models import Category, Post


def index(request):
    """Главная страница: последние опубликованные посты."""
    posts = Post.published.select_related(
        'author',
        'category',
        'location',
    )[:POSTS_ON_MAIN_PAGE]
    context = {
        'post_list': posts,
    }
    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    """Страница категории: посты конкретной опубликованной категории."""
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    posts = Post.published.select_related(
        'author',
        'category',
        'location',
    ).filter(category=category)
    context = {
        'category': category,
        'post_list': posts,
    }
    return render(request, 'blog/category.html', context)


def post_detail(request, post_id):
    """Детальная страница поста."""
    post = get_object_or_404(
        Post.published.select_related(
            'author',
            'category',
            'location',
        ),
        id=post_id,
    )
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)
