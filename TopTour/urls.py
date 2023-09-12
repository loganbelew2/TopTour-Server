from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from toptourapi.views import register_user, login_user, AttractionView, CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'attractions', AttractionView, 'attraction')
router.register(r'categories', CategoryView, 'category')
urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]