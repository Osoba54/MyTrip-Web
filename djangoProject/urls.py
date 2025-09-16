from django.contrib import admin
from django.urls import path
from users import views as user_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import PrivateDataView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/private-data/', PrivateDataView.as_view(), name='private_data'),
    path('register/', user_views.register_view,name='register'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('', user_views.home_view, name='home'),
    path('dashboard/', user_views.dashboard_view, name="dashboard")
]
