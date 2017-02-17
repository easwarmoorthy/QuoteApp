from django.contrib import admin
from forms import *
from models import *
admin.site.register(QuoteModel)

class QuoteModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
# Register your models here.
