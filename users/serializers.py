from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import AppUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # AppUser만을 사용하여 토큰 발급
        if isinstance(user, AppUser):
            return super().get_token(user)
        raise serializers.ValidationError("Invalid user type")

    def validate(self, attrs):
        # 로그인할 때 사용자를 AppUser로 제한
        try:
            username = attrs["username"].lower()
            username = username.replace("-", "")
            user = AppUser.objects.get(username=username)
        except AppUser.DoesNotExist:
            try:
                user = AppUser.objects.get(phone_number=username)
            except AppUser.DoesNotExist:
                raise serializers.ValidationError("No active account found with the given credentials")

        # 비밀번호 확인
        if not user.check_password(attrs["password"]):
            raise serializers.ValidationError("Incorrect credentials")

        # 사용자 활성화 상태 확인
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = "__all__"
