
from rest_framework_simplejwt.views import TokenObtainPairView

from .jwt import WasteOSTokenObtainPairSerializer


class LoginView(TokenObtainPairView):
    serializer_class = WasteOSTokenObtainPairSerializer