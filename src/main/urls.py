from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nippo/', include('nippo.urls')), # nippo/にアクセスされたらincludeの中を見にいきましょう
    path('detail/', include('nippo.urls'))
]
