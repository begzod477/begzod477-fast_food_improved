from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Food
from .forms import FoodForm


def home(request):
    foods = Food.objects.all()
    categories = Category.objects.all()
    context = {
        'foods': foods,
        'categories': categories,
    }
    return render(request, 'home.html', context)

def select_by_category(request, category_id):
    selected_category = get_object_or_404(Category, id=category_id) 
    foods = Food.objects.filter(category=selected_category) 
    categories = Category.objects.all()
    context = {
        'foods': foods,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'home.html', context)


def create_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('home')
    else:
        form = FoodForm()

    return render(request, 'create_food.html', {'form': form})

def update_food(request, id):
    food = get_object_or_404(Food, id=id)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()  
            return redirect('home')
    else:
        form = FoodForm(instance=food)
    return render(request, 'update_food.html', {'form': form})

def delete_food(request, id):
    food = get_object_or_404(Food, id=id)
    if request.method == 'POST':
        food.delete()  
        return redirect('home')  
    return render(request, 'confirm_delete.html', {'food': food}) 

def food_detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)  
    food.views += 1  
    food.save()  
    return render(request, 'food_detail.html', {'food': food})