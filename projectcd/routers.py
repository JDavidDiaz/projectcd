from rest_framework import routers
from api.viewsets import DataViewSet

router = routers.DefaultRouter()
router.register(r'files', DataViewSet, 'data')
