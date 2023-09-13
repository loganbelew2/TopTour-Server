from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from toptourapi.views import (
    register_user, login_user, AttractionView,
    CategoryView, CommentView, PostView, TouristView
    )

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'attractions', AttractionView, 'attraction')
router.register(r'categories', CategoryView, 'category')
router.register(r'comments', CommentView, 'comment')
router.register(r'posts', PostView, 'post')
router.register(r'tourists', TouristView, 'tourist')
urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]