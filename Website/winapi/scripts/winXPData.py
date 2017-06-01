from winapi.models import API, Dll
import json
import hashlib


winXPAPI = json.loads(open('/home/hcy/WinAPI/WinXP/winxp', 'r').read())
for dll_name, api_info in winXPAPI.items():
    print(dll_name)
    dll, create = Dll.objects.get_or_create(name=dll_name,)
    for api_name in api_info['ExportedFunctions']:
        api, created = API.objects.get_or_create(name=api_name,
                                                 hash_value=hashlib.sha256(api_name).hexdigest(),)
        if created:
            api.dll.add(dll)
            api.remark = 'winxp - ' + dll_name
        else:
            if 'winxp' in api.remark:
                api.remark = '{0}, {1}'.format(api.remark, dll_name)
            else:
                api.remark = '{0}\nwinxp - {1}'.format(api.remark, dll_name)
        api.save()
