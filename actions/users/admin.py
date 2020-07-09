from django.contrib import admin

from .models import BranchManager, Client, MedicalRecord, Score, Trainer

# Register your models here.


class BranchManagerAdmin(admin.ModelAdmin):
    model = BranchManager


class MedicalRecordInline(admin.TabularInline):
    model = MedicalRecord


class ClientAdmin(admin.ModelAdmin):
    model = Client
    exclude = ("client_until",)


class MedicalRecordAdmin(admin.ModelAdmin):
    model = MedicalRecord


class TrainerAdmin(admin.ModelAdmin):
    model = Trainer
    exclude = ("employee_until",)


admin.site.register(BranchManager, BranchManagerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(Trainer, TrainerAdmin)
