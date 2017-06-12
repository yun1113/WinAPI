from winapi.models import API, Dll
import json
import hashlib


win7API = json.loads(open('/home/hcy/WinAPI/Win7/win7', 'r').read())
for dll_name, api_info in win7API.items():
    print(dll_name)
    dll, create = Dll.objects.get_or_create(name=dll_name,)
    for api_name in api_info['ExportedFunctions']:
        api, created = API.objects.get_or_create(name=api_name,
                                                 hash_value=hashlib.sha256(api_name).hexdigest(),)
        if created:
            api.dll.add(dll)
            api.remark = 'win7 - ' + dll_name
        else:
            if 'win7' in api.remark:
                api.remark = '{0}, {1}'.format(api.remark, dll_name)
            else:
                api.remark = '{0}\nwin7 - {1}'.format(api.remark, dll_name)
        api.save()


count = []
for k, v in win7API.items():
    count.extend(v['ExportedFunctions'])
print(len(set(count)))

