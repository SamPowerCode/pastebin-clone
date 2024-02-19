from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Paste(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
