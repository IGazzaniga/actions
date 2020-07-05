from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import (
    Day,
    Exercise,
    Register,
    Routine,
    RoutineClient,
    RoutineExercise,
    Serie,
    Week,
)


class RoutineExerciseAdmin(admin.ModelAdmin):
    model = RoutineExercise


class ExerciseAdmin(admin.ModelAdmin):
    fields = ["name", "description", "gif"]


class DayInline(admin.TabularInline):
    model = Day
    fields = ["exercises"]
    extra = 0
    min_num = 3
    formfield_overrides = {
        models.ManyToManyField: {"widget": CheckboxSelectMultiple},
    }


class RoutineAdmin(admin.ModelAdmin):
    fields = ["name"]
    inlines = [DayInline]


class WeekAdmin(admin.ModelAdmin):
    model = Week


class SerieInline(admin.TabularInline):
    model = Serie
    fields = ["number", "weight_lifted", "reps"]
    extra = 1


class WeekInline(admin.StackedInline):
    model = Week
    inlines = [SerieInline]
    fields = ["number"]
    extra = 1


class RoutineClientAdmin(admin.ModelAdmin):
    fields = ["client", "routine", "is_current"]
    inlines = [WeekInline]


class SerieAdmin(admin.ModelAdmin):
    model = Serie


class RegisterAdmin(admin.ModelAdmin):
    fields = ["routine_exercise", "is_completed", "week"]
    inlines = [SerieInline]


admin.site.register(RoutineExercise, RoutineExerciseAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Routine, RoutineAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(RoutineClient, RoutineClientAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Register, RegisterAdmin)
