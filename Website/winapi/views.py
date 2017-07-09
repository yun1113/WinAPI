from django.shortcuts import render_to_response, render
from django.db.models import Count
from models import API, Dll


def api_info(request):
    if request.method == 'POST':
        api_name = request.POST.get('name', '')
        api = API.objects.filter(name=api_name)

        if api:
            return render(request, 'api_info.html', {'api': api[0]})
        else:
            return render(request, 'api_info.html', {'no_result': True})

    return render(request, 'api_info.html', locals())


def dll_info(request):
    if request.method == 'POST':
        dll_name = request.POST.get('name', '')
        dll = Dll.objects.filter(name=dll_name)

        if dll:
            return render(request, 'dll_info.html', {'dll': dll[0]})
        else:
            return render(request, 'dll_info.html', {'no_result': True})

    return render(request, 'dll_info.html', locals())


def temp_view(request):
    if request.method == 'POST':

        model_name = request.POST.get('type', 'dll').encode('utf8')
        name = request.POST.get('name', '')

        if model_name == 'API':
            data = API.objects.filter(name=name)
        else:
            data = Dll.objects.filter(name=name)

        if data:
            samples = data[0].malwareapicallexcutiontrace_set.all()
            return render(request, 'search.html', {'request': request, 'model_name': model_name,
                                                  'samples': samples, 'data': data[0]})

        else:
            return render(request, 'search.html', {'no_result': True})
    return render(request, 'search.html', locals())


def temp_view2(request):

    frquency_list = [(dll.name, len(dll.malwareapicallexcutiontrace_set.all()))
                     for dll in Dll.objects.annotate(num_malware=Count('malwareapicallexcutiontrace')).filter(
                     num_malware__gt=0)]
    sorted(frquency_list, key=lambda x: x[1])

    return render(request, 'frequency.html', locals())
