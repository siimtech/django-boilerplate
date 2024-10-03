from django import forms
from django.core.validators import RegexValidator
from .models import AppUser, Admin
from unfold.widgets import (
    UnfoldAdminTextInputWidget,
    UnfoldAdminImageFieldWidget,
    UnfoldBooleanSwitchWidget,
)


class AppUserForm(forms.ModelForm):
    username = forms.CharField(
        validators=[
            RegexValidator(
                regex=r"^[\w.@+-]+$",
                message="50자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다.",
            ),
        ],
        widget=UnfoldAdminTextInputWidget(attrs={"placeholder": "50자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다."}),
        help_text="50자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다.",
        label="유저네임",
    )
    phone_number = forms.CharField(
        required=False,
        widget=UnfoldAdminTextInputWidget(attrs={"placeholder": "010-1234-5678"}),
        validators=[
            RegexValidator(
                regex=r"^010-\d{3,4}-\d{4}$",
                message="휴대폰 번호 형식이 맞지 않습니다.",
            )
        ],
        label="휴대폰 번호",
    )
    is_phone_verified = forms.BooleanField(
        required=False,
        disabled=True,
        widget=UnfoldBooleanSwitchWidget(),
        help_text="휴대폰 인증여부는 관리자페이지에서 수정하실 수 없습니다.",
        label="휴대폰 인증 여부",
    )

    class Meta:
        model = AppUser
        fields = "__all__"
        help_texts = {
            "is_active": "이 사용자가 활성화되어 있는지를 나타냅니다. 계정을 삭제하는 대신 이것을 선택 해제하세요.",
        }
        readonly_fields = ("is_phone_verified",)

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password and (user.id is None or not password.startswith("pbkdf2_sha256$")):
            user.set_password(password)

        user = super().save(commit=False)
        
        if commit:
            user.save()
        
        return user

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"

    def save(self, commit=True):
        admin = self.instance
        password = self.cleaned_data.get("password")

        if password and (admin.id is None or not password.startswith("pbkdf2_sha256$")):
            admin.set_password(password)

        admin = super().save(commit=False)
        
        if commit:
            admin.save()
        
        return admin