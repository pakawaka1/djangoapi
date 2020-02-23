from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CourseView)
router.register('levels', views.LevelView)

urlpatterns = router.urls