from django.shortcuts import render_to_response, render
from models import API, Dll


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
            return render(request, 'index.html', {'request': request, 'model_name': model_name,
                                                  'samples': samples, 'data': data[0]})

    return render(request, 'index.html', locals())
