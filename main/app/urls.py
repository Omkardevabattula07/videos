from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('upload/',views.upload,name='upload'),
    path('download/<str:video_id>/',views.download,name='download_video')
]
