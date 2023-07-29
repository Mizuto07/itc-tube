from django.shortcuts import render
from random import randint

# Create your views here.

def nippoListView(request): # requestは必ず引数で指定
	return render(request, "nippo/nippo-list.html") # 第一引数にrequest 第二引数に表示したいhtml

def nippoDetailView(request, number):
    template_name = "nippo/nippo-detail.html"
    random_int = randint(1, 10)
    ctx = {
        "random_number": random_int,
        'number': number,
    }
    return render(request, template_name, ctx)

def nippoCreateView(request):
    template_name = 'nippo/nippo-form.html'
    if request.POST: # 値がある場合のみPOSTする
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(title)
    return render(request, template_name)
