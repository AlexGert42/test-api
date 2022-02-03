from django.contrib import admin

from django.urls import path, include, re_path


from rest_framework.routers import SimpleRouter

from store.views import *

router = SimpleRouter()
router.register(r'book', BookViewSet)
router.register(r'book_relation', UserBooksRelationView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('auth/', auth)


    # path('api/v1/books/', include('store.urls'))
]

urlpatterns += router.urls
