from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.showblog, name='showblog'),
    path('<int:post_id>/', blog.views.specific_post, name='specific_post')
]
