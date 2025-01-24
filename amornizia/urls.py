from django.contrib import admin
from django.conf.urls import handler404
# from django.conf.urls.static import static
# from django.contrib.auth.views import LogoutView
from django.conf import settings    
from django.urls import path, include
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name="login"),  # Use sua função de login personalizada
    path('', include('vitrine.urls')),
    # path('logout/', LogoutView.as_view(), name='logout'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'vitrine.views.nao_encontrado'
