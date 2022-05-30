# forms/admin.py

from django.contrib import admin
from forms.models import Form, FormField, Submission, SubmissionField

class FormFieldInline(admin.TabularInline):
    model = FormField

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    inlines = [FormFieldInline, ]

class SubmissionFieldInline(admin.TabularInline):
    model = SubmissionField
    extra = 0

    def has_change_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    inlines = [SubmissionFieldInline, ]

    def has_change_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False
