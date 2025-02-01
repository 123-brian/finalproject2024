# accnt/views.py

from django.shortcuts import render
from .models import HouseHelp, Employer
from django.http import HttpResponse
# views.py
from django.contrib.auth.decorators import login_required

# views.py
from django.shortcuts import render, redirect
from .forms import HouseHelpRegistrationForm, EmployerRegistrationForm


def house_help_registration(request):
    if request.method == 'POST':
        form = HouseHelpRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employer_list')  # Change to the URL you want to redirect to
    else:
        form = HouseHelpRegistrationForm()
    return render(request, 'accnt/house_help_registration.html', {'form': form})


def house_employer_registration(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('house_help_list')
    else:
        form = EmployerRegistrationForm()
    return render(request, 'accnt/house_employer_registration.html', {'form': form})


def index(request):
    return render(request, 'myportfolio/index.html')


@login_required()
def house_help_list(request):
    house_helps = HouseHelp.objects.all()
    print(house_helps)
    return render(request, 'accnt/house_help_list.html', {'house_helps': house_helps})


@login_required()
def employer_list(request):
    employers = Employer.objects.all()
    return render(request, 'accnt/employer_lists.html', {'employers': employers})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomAuthenticationForm

from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .models import HouseHelp, Employer


def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return render(request, 'accnt/my_login.html', {'error': 'Invalid credentials'})
        except PermissionDenied as e:
            return render(request, 'accnt/my_login.html', {'error': str(e)})

    return render(request, 'accnt/my_login.html')


@login_required()
def profile(request):
    return render(request, 'accnt/profile.html', {'user': request.user})


# views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accnt/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
