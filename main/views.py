from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306219745',
        'name': 'Salomo Immanuel Putra',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
