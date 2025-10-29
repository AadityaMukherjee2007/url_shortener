from django.db import models
from django.utils import timezone
import string, random

def generate_slug(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

class Link(models.Model):
    original_url = models.URLField()
    slug = models.SlugField(unique=True, max_length=15, blank=True)
    clicks = models.PositiveIntegerField(default=0)
    last_accessed = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            max_attempts = 10
            for attempt in range(max_attempts):
                self.slug = generate_slug()
                if not Link.objects.filter(slug=self.slug).exists():
                    break
            else:
                raise ValueError("Could not generate a unique slug after multiple attempts.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} -> {self.original_url}"
        
    


