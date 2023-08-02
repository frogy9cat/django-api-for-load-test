from django.contrib import admin
from .models import Counter


class CounterAdmin(admin.ModelAdmin):
    list_display = ('icounter', 'created_at')
    list_display_links = ('icounter', 'created_at')
    search_fields = ('icounter', 'created_at')


admin.site.register(Counter, CounterAdmin)