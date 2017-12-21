import logging
logger = logging.getLogger(__name__)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import HunterBuild, AssassinBuild, MageBuild, WarriorBuild, GuardianBuild
from .hunterform import HunterForm
from .guardianform import GuardianForm
from .mageform import MageForm
from .warriorform import WarriorForm
from .assassinform import AssassinForm

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def contact(request):
    return render(request, 'website/contact.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'website/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

def hunter_build(request):
    hunterbuilds = HunterBuild.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/hunter_build.html', {'hunterbuilds': hunterbuilds})

def hunterbuild_detail(request,pk):
    hunterbuild = get_object_or_404(HunterBuild, pk=pk)
    return render(request, 'website/hunterbuild_detail.html', {'hunterbuild': hunterbuild})

@login_required(login_url='login_view')
def hunter_new(request):
    if request.method == "POST":
        hunterform = HunterForm(request.POST)
        if hunterform.is_valid():
            build = hunterform.save(commit=False)
            build.author = request.user
            build.published_date = timezone.now()
            build.save()
            return redirect('hunterbuild_detail', pk=build.pk)
    else:
        hunterform = HunterForm(request.POST)
    return render(request, 'website/hunterbuild_new.html', {'hunterform': hunterform})

@login_required(login_url= 'login_view')
def deletehunter(request,pk):
    hunterbuild = get_object_or_404(HunterBuild, pk=pk)
    hunterbuild.delete()
    return render(request,'website/hunterbuild_deleted.html')

def mage_build(request):
    magebuilds = MageBuild.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/mage_build.html', {'magebuilds': magebuilds})

def magebuild_detail(request,pk):
    magebuild = get_object_or_404(MageBuild, pk=pk)
    return render(request, 'website/magebuild_detail.html', {'magebuild': magebuild})

@login_required(login_url='login_view')
def mage_new(request):
    if request.method == "POST":
        mageform = MageForm(request.POST)
        if mageform.is_valid():
            build = mageform.save(commit=False)
            build.author = request.user
            build.published_date = timezone.now()
            build.save()
            return redirect('magebuild_detail', pk=build.pk)
    else:
        mageform = MageForm(request.POST)
    return render(request, 'website/magebuild_new.html', {'mageform': mageform})

@login_required(login_url= 'login_view')
def deletemage(request,pk):
    magebuild = get_object_or_404(MageBuild, pk=pk)
    magebuild.delete()
    return render(request,'website/magebuild_deleted.html')

def guardian_build(request):
    guardianbuilds = GuardianBuild.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/guardian_build.html', {'guardianbuilds': guardianbuilds})

def guardianbuild_detail(request,pk):
    guardianbuild = get_object_or_404(GuardianBuild, pk=pk)
    return render(request, 'website/guardianbuild_detail.html', {'guardianbuild': guardianbuild})

@login_required(login_url='login_view')
def guardian_new(request):
    if request.method == "POST":
        guardianform = GuardianForm(request.POST)
        if guardianform.is_valid():
            build = guardianform.save(commit=False)
            build.author = request.user
            build.published_date = timezone.now()
            build.save()
            return redirect('guardianbuild_detail', pk=build.pk)
    else:
        guardianform = GuardianForm(request.POST)
    return render(request, 'website/guardianbuild_new.html', {'guardianform': guardianform})

@login_required(login_url= 'login_view')
def deleteguardian(request,pk):
    guardianbuild = get_object_or_404(GuardianBuild, pk=pk)
    guardianbuild.delete()
    return render(request,'website/guardianbuild_deleted.html')

def assassin_build(request):
    assassinbuilds = AssassinBuild.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/assassin_build.html', {'assassinbuilds': assassinbuilds})

def assassinbuild_detail(request,pk):
    assassinbuild = get_object_or_404(AssassinBuild, pk=pk)
    return render(request, 'website/assassinbuild_detail.html', {'assassinbuild': assassinbuild})

@login_required(login_url='login_view')
def assassin_new(request):
    if request.method == "POST":
        assassinform = AssassinForm(request.POST)
        if assassinform.is_valid():
            build = assassinform.save(commit=False)
            build.author = request.user
            build.published_date = timezone.now()
            build.save()
            return redirect('assassinbuild_detail', pk=build.pk)
    else:
        assassinform = AssassinForm(request.POST)
    return render(request, 'website/assassinbuild_new.html', {'assassinform': assassinform})

@login_required(login_url= 'login_view')
def deleteassassin(request,pk):
    assassinbuild = get_object_or_404(AssassinBuild, pk=pk)
    assassinbuild.delete()
    return render(request,'website/assassinbuild_deleted.html')

def warrior_build(request):
    warriorbuilds = WarriorBuild.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/warrior_build.html', {'warriorbuilds': warriorbuilds})

def warriorbuild_detail(request,pk):
    warriorbuild = get_object_or_404(WarriorBuild, pk=pk)
    return render(request, 'website/warriorbuild_detail.html', {'warriorbuild': warriorbuild})

@login_required(login_url='login_view')
def warrior_new(request):
    if request.method == "POST":
        warriorform = WarriorForm(request.POST)
        if warriorform.is_valid():
            build = warriorform.save(commit=False)
            build.author = request.user
            build.published_date = timezone.now()
            build.save()
            return redirect('warriorbuild_detail', pk=build.pk)
    else:
        warriorform = WarriorForm(request.POST)
    return render(request, 'website/warriorbuild_new.html', {'warriorform': warriorform})

@login_required(login_url= 'login_view')
def deletewarrior(request,pk):
    warriorbuild = get_object_or_404(WarriorBuild, pk=pk)
    warriorbuild.delete()
    return render(request,'website/warriorbuild_deleted.html')
