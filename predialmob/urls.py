from django.contrib import admin
from django.urls import include, path

import demo.views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('template/', include('protend.urls')),

    path('', demo.views.view_index),
    path('calendario/', demo.views.view_calendar),
    path('atividade/', demo.views.view_manutencao),
    path('helpdesk/', demo.views.view_helpdesk),
]
