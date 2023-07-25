from django.urls import path
from .views import nippoListView # .は同じディレクトリ内を示す
 
urlpatterns = [
  path("", nippoListView), # views.pyでつくった関数名
]