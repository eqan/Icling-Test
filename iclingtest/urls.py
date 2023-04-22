from django.urls import include, path
from rest_framework import routers
from tasks.views import TaskViewSet, TileViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'tiles', TileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
