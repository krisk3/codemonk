"""
Defines database models for the Django application.
"""
from django.db import models


class Paragraph(models.Model):
    """
    Database model for storing paragraphs.

    Attributes:
        uid (str): Unique identifier for the paragraph.
        paragraph (str): Text content of the paragraph.
    """

    uid = models.CharField(max_length=255)
    paragraph = models.TextField()

    def __str__(self):
        """
        Returns a human-readable string representation of the Paragraph instance.
        """
        return self.uid


class Word(models.Model):
    """
    Database model for storing words associated with paragraphs.

    Attributes:
        word (str): The word itself.
        paragraph_word (Paragraph): The paragraph to which the word belongs.
    """

    word = models.CharField(max_length=255)
    paragraph_word = models.ForeignKey(Paragraph, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a human-readable string representation of the Word instance.
        """
        return self.word

    class Meta:
        """
        Defines metadata for the Word model.

        Indexes:
            - Index on 'word' and 'paragraph_word' fields for efficient lookups.
        """

        indexes = [models.Index(fields=["word", "paragraph_word"])]
