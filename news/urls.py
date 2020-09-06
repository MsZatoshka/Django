from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    # path('', views.index, name="news"),
]+ static("/image/", document_root="news/image/") 