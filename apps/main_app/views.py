from django.shortcuts import render, redirect

def index(request):
    if 'input' not in request.session:
        request.session['input'] = {}
        request.session['counter'] = 1
    return render(request, 'main_app/index.html')

def process(request):
    request.session['input'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'fav_lang': request.POST['language'],
        'comment': request.POST['comment']
    }
    request.session['counter'] += 1
    print(request.session['counter'])
    return redirect('/result')

def result(request):
    return render(request, 'main_app/result.html')
