from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from accounts.views import UserViewSet
from scenes.views import SceneViewSet, WordViewSet, BookmarkViewSet, RecommendationViewSet, UnderstoodViewSet 


router = routers.SimpleRouter()
router.register('accounts', UserViewSet)
router.register('scenes', SceneViewSet)
router.register('words', WordViewSet)
router.register('bookmarks', BookmarkViewSet)
router.register('recommendations', RecommendationViewSet)
router.register('understoods', UnderstoodViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]
