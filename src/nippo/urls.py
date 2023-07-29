from django.urls import path
from .views import nippoListView, nippoDetailView, nippoCreateView # .は同じディレクトリ内を示す
 
urlpatterns = [
    path("", nippoListView), # views.pyでつくった関数名 ''で親のnippo/
    path('detail/<int:number>/', nippoDetailView),
    path('create/', nippoCreateView),
]