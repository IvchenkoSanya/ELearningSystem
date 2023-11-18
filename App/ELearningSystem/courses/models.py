from django.db import models

class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword_text = models.CharField(max_length=100)
    is_soft_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.keyword_text

class Prompt(models.Model):
    prompt_id = models.AutoField(primary_key=True)
    prompt_text = models.CharField(max_length=500)
    is_soft_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.prompt_text

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    description = models.JSONField()
    keyword = models.ForeignKey(Keyword, on_delete=models.SET_NULL, null=True)
    prompt = models.ForeignKey(Prompt, on_delete=models.SET_NULL, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name