from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Food, Comment, Like
from .forms import FoodForm, CommentForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    foods = Food.objects.all()
    categories = Category.objects.all()
    context = {
        'foods': foods,
        'categories': categories,
    }
    return render(request, 'home.html', context)

@login_required
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


@login_required
def create_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('home')
    else:
        form = FoodForm()

    return render(request, 'create_food.html', {'form': form})


@login_required
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

@login_required
def delete_food(request, id):
    food = get_object_or_404(Food, id=id)
    if request.method == 'POST':
        food.delete()  
        return redirect('home')  
    return render(request, 'confirm_delete.html', {'food': food}) 


@login_required
def food_detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)  
    food.views += 1  
    food.save()  
    return render(request, 'food_detail.html', {'food': food})


@login_required
def add_comment(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.food = food
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully')
    return redirect('food_detail', food_id=pk)


@login_required
def like_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, food=food)
    if not created:
        like.delete()
    return redirect('food_detail', food_id=pk)


def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
