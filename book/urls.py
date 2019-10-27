from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('book', views.BookViewSet)
router.register('diary', views.DiaryViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
]

# router = 복잡한 url들의 묶음