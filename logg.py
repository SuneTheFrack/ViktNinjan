from routers.matlogg import logg_maltid_intern

def handler(request):
    data = request.get_json()
    return logg_maltid_intern(data)
