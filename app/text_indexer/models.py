from django.db import models

class Paragraph(models.Model):
    uid = models.CharField(max_length=255)
    paragraph = models.TextField()

    def __str__(self):
        return self.uid

class Word(models.Model):
    word = models.CharField(max_length=255)
    paragraph_word = models.ForeignKey(Paragraph, on_delete=models.CASCADE)

    def __str__(self):
        return self.word



