from django.shortcuts import render


# Create your views here.
def home(request):
    return render(
        request=request,
        template_name='core/home.html',
        context={}
    )


def profile(request):
    return render(
        request=request,
        template_name='account/profile.html',
        context={}
    )
