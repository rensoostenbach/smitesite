from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import HunterBuild
from .hunterform import HunterForm

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def hunter_build(request):
    hunterbuilds = HunterBuild.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/hunter_build.html', {'hunterbuilds': hunterbuilds})

def hunterbuild_detail(request,pk):
    hunterbuild = get_object_or_404(HunterBuild, pk=pk)
    return render(request, 'website/hunterbuild_detail.html', {'hunterbuild': hunterbuild})

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

def deletehunter(request,pk):
    hunterbuild = get_object_or_404(HunterBuild, pk=pk)
    hunterbuild.delete()
    return render(request,'website/hunterbuild_deleted.html')
