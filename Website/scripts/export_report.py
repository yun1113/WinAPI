from openpyxl import Workbook
from winapi.models import API, Dll, MalwareAPICall, MalwareAPICallExcutionTrace
import json
import os


def export_report(data, filename='report'):
    report_dict = generte_api_count(data)
    write_to_file(filename, report_dict)
    import pdb;pdb.set_trace()
    update_to_db(filename, report_dict)
    import pdb;
    pdb.set_trace()


def generte_api_count(data):

    report_dict = {}
    for item in data:
        dll, api = item

        if dll in report_dict.keys():
            if api in report_dict[dll].keys():
                report_dict[dll][api] = report_dict[dll][api] + 1
            else:
                report_dict[dll][api] = 1
        else:
            report_dict[dll] = {}
            report_dict[dll][api] = 1

    return report_dict


def write_to_file(filename, data):
    wb = Workbook()
    ws = wb.active

    ws.title = 'API count'
    ws.append(['Api', 'Dll', 'Count'])

    ws2 = wb.create_sheet('Statistic')
    ws2.append(['Total Dll Number', len(data.keys())])

    unsort_list = []
    for k, v in data.items():
        ws2.append(['', k])
        for api, count in v.items():
            unsort_list.append([api, k, count])
    ws2['A2'] = 'Dll List'
    for item in sorted(unsort_list, key=lambda x: x[2], reverse=True):
        ws.append(item)

    wb.save(os.path.basename(filename)+'.xlsx')


def update_to_db(filename, data):

    sha256 = filename.split('_')[0]
    malware_excution_trace, created = MalwareAPICallExcutionTrace.objects.get_or_create(sha256=sha256)

    for dll, v in data.items():
        d = Dll.objects.get(name__iexact=dll.lower())
        malware_excution_trace.dll.add(d)

        for api, count in v.items():
            a = API.objects.get(name__iexact=api.lower())
            malware_excution_trace.api.add(a)
            MalwareAPICall.objects.update_or_create(
                malware_excution_trace=malware_excution_trace, api=a, dll=d,
                defaults={'api': a, 'dll': d, 'count': count})
    malware_excution_trace.save()


def run(*args):
    filename = args[0]
    data = json.load(open(filename, 'r'))
    export_report(data, filename)

# python manage.py runscript export_report --script-args /home/hcy/WinAPI/Website/mimikatz.exe_3584.trace.calls.json
