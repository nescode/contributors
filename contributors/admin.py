from django.contrib import admin
from.models import CreateContributor


# admin.site.register(Contribution)
# admin.site.register(CreateContributor)

class CreateContributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role', 'resume', 'contributed')
    list_editable = ('role', 'contributed')
    search_fields = ('name', 'email')


admin.site.register(CreateContributor, CreateContributorAdmin)

