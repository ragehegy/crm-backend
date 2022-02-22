def get_hostname(request):
    return request.get_host().split(":")[0]

def get_tenant(request):
    hostname = get_hostname(request)
    subdomain = hostname.split(".")[0]
    return subdomain
