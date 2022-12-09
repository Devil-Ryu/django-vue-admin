from rest_framework.routers import SimpleRouter
from .views import holemendModelViewSet

router = SimpleRouter()
router.register("api/itsm_app", holemendModelViewSet)

urlpatterns = []
urlpatterns += router.urls