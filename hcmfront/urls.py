from django.conf.urls import url, include
from django.contrib import admin
from schedule import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Aqui se crea el link con el modulo schedule, para django 1.11 se ocupa url, para versiones mas nuevas se ocupa path.
    url(r'', include('schedule.urls')),
]
