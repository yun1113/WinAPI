from winapi.models import API, Dll
import json
import hashlib


win10API = json.loads(open('/home/hcy/WinAPI/win10_v2', 'r').read())
for dll_name, api_info in win10API.items():

    dll, create = Dll.objects.get_or_create(name=dll_name,)
    for api_name in api_info['ExportedFunctions']:
        print api_name
        api, created = API.objects.get_or_create(name=api_name,
                                                 hash_value=hashlib.sha256(api_name).hexdigest(),)
        api.dll.add(dll)
        if created:
            api.remark = 'win10 - ' + dll_name
        else:
            print api.name
            api.remark = '{0}, {1}'.format(api.remark, dll_name)
        api.save()
