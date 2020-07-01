from django.urls import path
from .views import index, post_new, post_detail, blog, delete_post,publish_post, unpublish_post, edit_post, post_new_comment, post_new_comment_form

urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('post_new/', post_new, name='post_new'),
    path('posts/<int:article_id>/', post_detail, name='post_detail'),
    path('delete_post/<int:article_id>/', delete_post, name='delete_post'),
    path('publish_post/<int:article_id>/', publish_post, name='publish_post'),
    path('unpublish_post/<int:article_id>/', unpublish_post, name='unpublish_post'),
    path('edit_post/<int:article_id>/', edit_post, name='edit_post'),
    path('post_new_comment/', post_new_comment, name='post_new_comment'),
    path('post_new_comment_form/', post_new_comment_form, name='post_new_comment_form'),
]
