from django.urls import path
from .views import nippoListView, nippo_detail_view, nippoCreateView # .は同じディレクトリ内を示す
 
urlpatterns = [
    path("", nippoListView, name="nippo-list"),
    path("detail/<int:pk>/", nippo_detail_view, name="nippo-detail"),
    path("create/", nippoCreateView, name="nippo-create"),
]