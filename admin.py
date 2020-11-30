from django.contrib import admin


@admin.register({{ app_name|title }})
class {{ app_name|title }}(admin.ModelAdmin):
    pass
