from django.shortcuts import render

from hodimlar.models import Hodim

# Create your views here.
def hodim(request,pk):
    try:
        hodim = Hodim.objects.get(pk=pk)
    except:
        pass
    context = {
        'hodim':hodim
    }
    return render(request, 'hodim.html', context)
