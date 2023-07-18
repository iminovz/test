from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import CsvForm
from .forms import UserRegisterForm
from .models import CsvFile


class HomePageView(ListView):
    model = CsvFile
    template_name = 'home.html'


class CreatePostView(CreateView):
    model = CsvFile
    form_class = CsvForm
    template_name = 'csv.html'
    success_url = reverse_lazy('home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Создан аккаунт {username}!')
        return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'datacsv/register.html', {'form': form})


def home(request):
    return render(request, "csv/home.html")


@login_required
def profile(request):
    return render(request, 'users/profile.html')
