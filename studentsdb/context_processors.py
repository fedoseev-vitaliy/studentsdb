from urlparse import urlparse
from django.contrib.messages.api import get_messages


def students_proc(request):
    url = urlparse(request.build_absolute_uri(None))
    return {'PORTAL_URL': '{uri.scheme}://{uri.netloc}'.format(uri=url)}


def message_collection(request):
    message_collection = {}
    all_messages = get_messages(request)
    for message in all_messages:       
        message_collection[message.extra_tags] = message
    return {'message_collection': message_collection}