from django import forms
from .models import Category, Food, Comment
from django.contrib.auth.models import User


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'photo', 'price', 'have']
        widgets = {
            'name': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ovqat nomi",
                'style': "border: 1px dashed green;"
            }),
            'description': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Ovqat haqida",
                "rows": 4,
            }),
            'photo': forms.FileInput(attrs={ 
                "class": "form-control"
            }),
            'price': forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Ovqat narxi",
            }),
            'category': forms.Select(attrs={
                "class": "form-control"
            }),
            'have': forms.CheckboxInput(attrs={
                "class": "form-check-input mb-5",
                "checked": "checked"
            }),
        }




def create(self):
    food = Food.objects.create(
        name=self.cleaned_data.get("name"),
        description=self.cleaned_data.get("description"),
        photo=self.cleaned_data.get("photo"),
        price=self.cleaned_data.get("price"),
        category=self.cleaned_data.get("turi"), 
        have=self.cleaned_data.get("have", False),
    )
    return food


def update(self, instance: Food):
        instance.name = self.cleaned_data.get("name", instance.name)
        instance.description = self.cleaned_data.get("description", instance.description)
        instance.price = self.cleaned_data.get("price", instance.price)
        instance.have = self.cleaned_data.get("have", instance.have)
        if self.cleaned_data.get("image"):
            instance.image = self.cleaned_data.get("image")  
        instance.save()
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add a comment...',
                'aria-label': 'Comment Content',
                'required': True,
            }),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'aria-label': 'Username',
            'required': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'aria-label': 'Password',
            'required': True,
        })
    )

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password',
        'aria-label': 'Password',
        'required': True,
    }))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm your password',
        'aria-label': 'Confirm Password',
        'required': True,
    }), label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username',
                'aria-label': 'Username',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'aria-label': 'Email',
                'required': True,
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

