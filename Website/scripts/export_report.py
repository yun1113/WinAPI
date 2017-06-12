from openpyxl import Workbook
import json
import os


def export_report(data, filename='report'):
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

    write_to_file(filename, report_dict)


def write_to_file(filename, data):
    wb = Workbook()
    ws = wb.active
    ws.append(['Api', 'Dll', 'Count'])
    for k, v in data.items():
        for api, count in v.items():
            ws.append([api, k, count])
    wb.save(os.path.basename(filename)+'.xlsx')


def run(*args):
    filename = args[0]
    data = json.load(open(filename, 'r'))
    export_report(data, filename)

# python manage.py runscript export_report --script-args /home/hcy/WinAPI/Website/mimikatz.exe_3584.trace.calls.json
