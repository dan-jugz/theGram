from django.urls import path, include
from .views import PostListView,PostCreateView,PostDetailView,PostDeleteView,PostUpdateView

app_name = 'insta'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(),name='post_create'),
    path('<int:id>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:id>/delete/', PostDeleteView.as_view(), name='post_delete')
]