from django import forms
from .models import Category, Food

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

  
