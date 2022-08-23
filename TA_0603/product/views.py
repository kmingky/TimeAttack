from django.shortcuts import render
from .models import Category, Drink

# from django.views import View

# Create your views here.


def Select_view(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        category = request.POST.get("category", None)
        category_obj = Category.objects.get(id=category)
        data = Drink.objects.filter(drink_category=category_obj)
        return render(request, "index.html", {"data": data})


# class HmoeView(View):
#     def get(self, request):
#         return render(request, 'index.html')
#
#     def post(self, request):
#         category = request.POST.get('category', None)
#
#         category_obj = Category.objects.get(id=category)
#
#         data = Drink.objects.filter(category=category_obj).values()
#
#         return render(request, 'index.html', {"data":data})
