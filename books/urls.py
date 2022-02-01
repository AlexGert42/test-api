from django.contrib import admin
from django.urls import path, include


from rest_framework.routers import SimpleRouter

from store.views import BookViewSet

router = SimpleRouter()
router.register(r'book', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/books/', include('store.urls'))
]

urlpatterns += router.urls
