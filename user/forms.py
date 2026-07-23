from django import forms
from django.contrib.auth import get_user_model
from .models import (Category,Product,CustomUser)
User = get_user_model()


# LOGIN FORM
class UserForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:

        model = User

        fields = [
            'username',
            'password'
        ]


# CATEGORY FORM
class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = '__all__'


# PRODUCT FORM
class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = '__all__'


# REGISTER FORM
class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm Password'}
        )
    )

    class Meta:

        model = CustomUser

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'address',
            'password',
        ]

        widgets = {

            'first_name': forms.TextInput(
                attrs={'placeholder': 'ชื่อ'}
            ),

            'last_name': forms.TextInput(
                attrs={'placeholder': 'นามสกุล'}
            ),

            'username': forms.TextInput(
                attrs={'placeholder': 'Username'}
            ),

            'email': forms.EmailInput(
                attrs={'placeholder': 'Email'}
            ),

            'phone': forms.TextInput(
                attrs={'placeholder': 'เบอร์โทรศัพท์'}
            ),

            'address': forms.Textarea(
                attrs={
                    'placeholder': 'ที่อยู่',
                    'rows':3
                }
            ),
        }

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)

        self.fields['first_name'].required=True
        self.fields['last_name'].required=True
        self.fields['username'].required=True
        self.fields['email'].required=True
        self.fields['phone'].required=True
        self.fields['address'].required=True
        self.fields['password'].required=True
        self.fields['confirm_password'].required=True

    # CHECK PASSWORD MATCH
    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')

        confirm_password = cleaned_data.get(
            'confirm_password'
        )

        if password != confirm_password:

            raise forms.ValidationError(
                'Passwords do not match'
            )

        return cleaned_data
# UPDATE USER FORM
class UpdateUserForm(forms.ModelForm):

    class Meta:

        model = CustomUser

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]

        widgets = {

            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                    'class': 'form-control'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                    'class': 'form-control'
                }
            ),

            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                    'class': 'form-control'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                    'class': 'form-control'
                }
            ),
        }