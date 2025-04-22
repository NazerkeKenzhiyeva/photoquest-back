from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    QuestViewSet,
    SubmissionViewSet,
    RegisterView,
    current_user
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Роутер для ViewSet'ов
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'quests', QuestViewSet, basename='quest')
router.register(r'submissions', SubmissionViewSet, basename='submission')

# Основные URL
urlpatterns = [
    path('', include(router.urls)),  # API для категорий, квестов и сабмишнов
    path('me/', current_user, name='current_user'),  # Получить данные о текущем пользователе
    path('register/', RegisterView.as_view(), name='register'),  # Регистрация пользователя
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Логин (JWT)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
]

