from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class VUJSTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token


class VUJSTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class VUJSTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenObtainPairSerializer
