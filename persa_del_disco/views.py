from django.http import HttpResponseNotFound

def handler404(request, exception):
    return HttpResponseNotFound("404: Page not found") # TODO: a more useful handler