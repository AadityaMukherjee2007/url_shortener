from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Link

def redirect_view(request, slug):
    
    from django.db.models import F

   
    Link.clicks = F('clicks') + 1
    Link.last_accessed = timezone.now()
    Link.save()
    
    Link.refresh_from_db()
    from django.core.validators import URLValidator
    from django.core.exceptions import ValidationError

    url_validator = URLValidator()
    try:
        url_validator(Link.original_url)
        return redirect(Link.original_url)
    except ValidationError:
        
        return render(request, "invalid_url.html", status=400)



def analytics(request):
    links = Link.objects.all().order_by('-created_at')
    return render(request, 'analytics.html', {'links': links})