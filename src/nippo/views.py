from django.shortcuts import render
from random import randint
from .models import NippoModel # データベースアクセス用

# Create your views here.

def nippoListView(request): # requestは必ず引数で指定
    template_name = "nippo/nippo-list.html"
    ctx = {}
    qs = NippoModel.objects.all() # データベースNippoModelからすべてのデータを取得
    print(qs)
    ctx["object_list"] = qs
    return render(request, template_name, ctx)

def nippo_detail_view(request, pk):
    template_name = "nippo/nippo-detail.html"
    ctx = {}
    q = NippoModel.objects.get(pk=pk)
    print('aaaaaa')
    ctx["object"] = q
    return render(request, template_name, ctx)

def nippoCreateView(request):
    template_name = 'nippo/nippo-form.html'
    if request.POST: # 値がある場合のみPOSTする
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(title)
        print(content)
    return render(request, template_name)
