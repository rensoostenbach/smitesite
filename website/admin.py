from django.contrib import admin
from .models import HunterBuild, AssassinBuild, MageBuild, WarriorBuild, GuardianBuild

# Register your models here.
admin.site.register(HunterBuild)
admin.site.register(AssassinBuild)
admin.site.register(MageBuild)
admin.site.register(WarriorBuild)
admin.site.register(GuardianBuild)
