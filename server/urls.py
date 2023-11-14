from django.contrib import admin
from django.urls import path, include
from api.views import ProjectView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("", ProjectView, basename="projectview")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),

]
