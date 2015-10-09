from urlparse import urlparse

def students_proc(request):
    url = urlparse(request.build_absolute_uri(None))
    return {'PORTAL_URL': '{uri.scheme}://{uri.netloc}'.format(uri=url)}