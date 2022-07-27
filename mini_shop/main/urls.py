from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.DefaultRouter()
router.register(r'api/organizations', views.OrganizationViewSet)
router.register(r'api/shops', views.ShopViewSet)
# router.register(r'api/token', TokenObtainPairView, basename='token_obtain_pair')
# router.register(r'api/token/refresh', TokenRefreshView, basename='token_refresh')

urlpatterns = [
    path('', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
