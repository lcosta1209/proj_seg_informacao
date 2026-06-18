from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CurriculoForm
from .models import Curriculo

def listagem(request):
    termo = request.GET.get('q', '').strip()[:200]
    if termo:
        curriculos = Curriculo.objects.filter(nome__icontains=termo)
    else:
        curriculos = Curriculo.objects.all()
    return render(request, 'curriculos/listagem.html', {
        'curriculos': curriculos,
        'termo': termo,
    })

def cadastro(request):
    if request.method == 'POST':
        form = CurriculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Currículo cadastrado com sucesso.')
            return redirect('listagem')
    else:
        form = CurriculoForm()
    return render(request, 'curriculos/cadastro.html', {'form': form})

def consulta(request, pk):
    curriculo = get_object_or_404(Curriculo, pk=pk)
    return render(request, 'curriculos/consulta.html', {'curriculo': curriculo})