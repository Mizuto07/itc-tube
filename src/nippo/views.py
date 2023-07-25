from django.shortcuts import render

# Create your views here.

def nippoListView(request): # requestは必ず引数で指定
	return render(request, "nippo/nippo-list.html") # 第一引数にrequest 第二引数に表示したいhtml
