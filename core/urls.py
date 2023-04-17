from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from quickstart import views
from quickstart import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet) #viewsets automatically create url as for users and groups here
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
