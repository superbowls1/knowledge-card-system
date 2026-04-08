from django.db import models
# represents a card stored in the database


class Card(models.Model):
#title of card max 100 chars

    title = models.CharField(max_length=100)
#description content of the card
    description = models.TextField()
    image_url = models.URLField()
#url link to the image with the card
    def __str__(self):
        return self.title
#defines how the object appears in django
