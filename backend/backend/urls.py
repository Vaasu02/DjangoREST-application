# Import Django's admin module for administrative interface
from django.contrib import admin
# Import path for defining URLs and include for including other URL patterns
from django.urls import path, include
# Import our custom view for user registration
from api.views import CreateUserView
# Import JWT token views for handling authentication tokens
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Define a list of URL patterns for our application
urlpatterns = [
    # Django admin interface URL - accessible at /admin/
    path('admin/', admin.site.urls),
    
    # User registration endpoint - accessible at /api/user/register/
    path('api/user/register/', CreateUserView.as_view(), name='register'),
    
    # JWT token endpoints:
    # Login endpoint to get initial tokens - accessible at /api/token/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Endpoint to refresh expired tokens - accessible at /api/token/refresh/
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Include Django REST Framework's authentication URLs (login/logout views)
    path("api/auth/", include("rest_framework.urls")),
    path('api/', include('api.urls')),
]
