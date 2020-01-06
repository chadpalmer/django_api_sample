from django.contrib import admin
from axioms.models import Axiom, Intro
from django.contrib.admin import AdminSite


class SingleInstanceAdminMixin(object):
    """Hides the "Add" button when there is already an instance."""
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        return super(SingleInstanceAdminMixin, self).has_add_permission(request)


class IntroAdmin(SingleInstanceAdminMixin, admin.ModelAdmin):
     fields = ['title', 'description', 'footer']
     list_display = ('title', 'description', 'footer')


class AxiomAdmin(admin.ModelAdmin):
    fields = ['category', 'text', 'owner']
    list_display = ('category', 'text', 'owner')


admin.site.register(Axiom, AxiomAdmin)
admin.site.register(Intro, IntroAdmin)
