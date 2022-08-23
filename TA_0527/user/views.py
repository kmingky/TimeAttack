from .models import UserClass
from django.http import HttpResponse

# Create your views here.
def join_view(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        UserClass.objects.create_user(email=email, password=password)

        return HttpResponse(
            "<script>alert('회원 가입 완료'); location.href='/index';</script>"
        )
