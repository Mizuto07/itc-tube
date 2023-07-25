from django.urls import path
from .views import nippoListView, nippoDetailView # .は同じディレクトリ内を示す
 
urlpatterns = [
    path("", nippoListView), # views.pyでつくった関数名 ''で親のnippo/
    path('detail/', nippoDetailView)
]