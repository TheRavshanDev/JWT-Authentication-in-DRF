from django.contrib import admin
from django.urls import path, include
from base.views import MuallifViewSet, TalksViewSet, MaqolaViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register("maqola",MaqolaViewSet)
router.register("talks",TalksViewSet)
#router.register("muallif",MuallifViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('muallif/',MuallifViewSet.as_view(), name='muallif'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
