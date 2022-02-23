from business.models import Business

def get_hostname(request):
    return request.get_host().split(":")[0]

def get_tenant(request):
    hostname = get_hostname(request)
    subdomain = hostname.split(".")[0]
    return subdomain

def get_business(request):
    return Business.objects.filter(domain=get_tenant(request)).first()
