from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306202132',
        'name': 'Fadhlurohman Dzaki',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
  