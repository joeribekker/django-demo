from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FormField(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.label

class Submission(models.Model):
    form = models.ForeignKey(Form, on_delete=models.PROTECT)

    def __str__(self):
        return self.form.name

class SubmissionField(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    field = models. ForeignKey(FormField, on_delete=models.PROTECT)
    value = models.TextField()

    def __str__(self):
        return self.field.label
