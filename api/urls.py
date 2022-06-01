from django.urls import path
from .views import PostList, PostRetrieveUpdate

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostRetrieveUpdate.as_view(),)
]