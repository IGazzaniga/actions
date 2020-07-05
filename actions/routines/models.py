from django.db import models

# Create your models here.


class Exercise(models.Model):
    name = models.CharField(max_length=30, default="")
    description = models.TextField(default="")
    gif = models.ImageField(default="")

    def __str__(self):
        return self.name


class Routine(models.Model):
    name = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name


class Day(models.Model):
    exercises = models.ManyToManyField(Exercise)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)


class RoutineClient(models.Model):
    client = models.ForeignKey("users.Client", on_delete=models.PROTECT)
    routine = models.ForeignKey(Routine, on_delete=models.PROTECT)
    is_current = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.is_current:
            RoutineClient.objects.filter(is_current=True).update(is_current=False)
        super(RoutineClient, self).save(*args, **kwargs)


class RoutineExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    routine = models.ForeignKey(Routine, on_delete=models.PROTECT)
    day = models.ForeignKey(Day, on_delete=models.PROTECT)


class Week(models.Model):
    number = models.IntegerField(default=1)
    routine_client = models.ForeignKey(
        RoutineClient, on_delete=models.PROTECT, null=True
    )
    days = models.ManyToManyField(Day)


class Register(models.Model):
    routine_exercise = models.ForeignKey(RoutineExercise, on_delete=models.PROTECT)
    is_completed = models.BooleanField(default=False)
    week = models.ForeignKey(Week, on_delete=models.PROTECT, null=True)


class Serie(models.Model):
    number = models.IntegerField(default=1)
    weight_lifted = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    register = models.ForeignKey(Register, on_delete=models.CASCADE)
