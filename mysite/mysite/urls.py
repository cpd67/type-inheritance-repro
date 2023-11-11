from django.contrib import admin
from django.urls import include, path
from .schema import schema
from myapp.views import CustomGraphqlView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('graphql', CustomGraphqlView.as_view(schema=schema)),
]
