from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406408224',
        'name': 'Nadine Aisyah Putri Maharani',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
