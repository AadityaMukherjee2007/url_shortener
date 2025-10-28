from django.shortcuts import render

from url_shortener.Shortener.models import Link

# Create your views here.


def index(request):
    if request.method == "POST":
        original_url = request.POST.get("original_url")
        if original_url:
            link, created = Link.objects.get_or_create(original_url=original_url)
            return render(request, "Shortener/index.html", {"link": link, "created": created})
    return render(request, "Shortener/index.html")




def redirect_view(request, slug):
    try:
        link = get_object_or_404(Link, slug=slug)
        link.clicks += 1
        link.save()
        return redirect(link.original_url)
    except Link.DoesNotExist:
        return render(request, "Shortener/404.html", status=404)