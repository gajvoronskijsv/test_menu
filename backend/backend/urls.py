from django.contrib import admin
from django.urls import path, reverse_lazy, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy('home'))),
    path('menu/', include('menu.urls')),
]
