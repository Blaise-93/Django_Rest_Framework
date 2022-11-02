
from django.contrib import admin
from django.urls import path, include
from musicapp.views import (
    SongDeleteView, SongListCreateView, ArtisteListView,
    song_detail_view, SongUpdateView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('<int:pk>/', song_detail_view, name='detail'),
    path('<int:pk>/update', SongUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', SongDeleteView.as_view(), name='delete'),
    path('', SongListCreateView.as_view(), name='test'),
    path('artiste/', ArtisteListView.as_view(), name='artiste'),


]
