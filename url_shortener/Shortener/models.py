from django.db import models

# Create your models here.
import string , random


def generate_slug(length=6):
    characters = string.ascii_letters + string.digits
    slug = ''.join(random.choice(characters) for _ in range(length))
    return slug


class Link(models.Model):
    original_url = models.URLField()
    slug = models.SlugField(max_length=15, unique=True, default=generate_slug)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug()
            while Link.objects.filter(slug=self.slug).exists():
                self.slug = generate_slug()

        super().save(*args, **kwargs)

        
    def __str__(self):
        return f"{self.original_url} -> {self.slug}"