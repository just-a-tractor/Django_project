from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/organizations', views.OrganizationViewSet)
router.register(r'api/shops', views.ShopViewSet)

urlpatterns = router.urls
