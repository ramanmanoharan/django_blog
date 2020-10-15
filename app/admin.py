from django.contrib import admin

# Register your models here.
from .models import App
from .models import Slider
from .models import About
from .models import Team
from .models import Client


admin.site.register(App)

admin.site.register(Slider)

admin.site.register(About)

admin.site.register(Team)

admin.site.register(Client)