from django.urls import path
from . import views

app_name= 'challenge4'
urlpatterns = [
    path('',views.home, name='home'),    
    path('blog',views.blog, name='blog'),
    path('mentor',views.mentor, name='mentor'),
    path('mentee',views.mentee, name='mentee'),
    path('author',views.author, name='author'),
    path('input_blog',views.input_blog, name='input_blog'),
    path('save_new_blog',views.save_new_blog, name='save_new_blog'),
    # path('article-base',views.article_base, name='article-base' ),
    path('post/<int:blog_id>', views.article_base, name='article-base'),

]

