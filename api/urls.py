from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

router = routers.DefaultRouter()

router.register("Igitabo", LivreViewSet)
router.register("Umusomyi", LecteurViewSet)
router.register("Retrait",RetraitViewSet)
router.register("Remise", RemiseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('retrait/', Retrait, name="Retrait"),
    path('Remise/', Remise, name="Remise"),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]