from django.urls import path

from api.views import upload_file


urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
]
