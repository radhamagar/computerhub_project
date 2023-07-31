from django.shortcuts import render, get_object_or_404, redirect
from .forms import ComputerForm, BrandForm, SpecificationForm, GenerationForm
from .models import Computer
from django.views import View
from django.http import HttpResponse



def aboutus(request):
    return HttpResponse("<b>Welcome to ComputerHub</b>")
class HomeView(View):
    def get(self, request):
        list = Computer.objects.all()
        context = {
                    'list': list
                }
        return render(request, 'home.html', context)
            

class CreateComputerView(View):
    def get(self, request):
        form = ComputerForm()
        context = {
                    'form': form,
                }
        return render(request, 'computerform.html', context)
    
    def post(self, request):
        form = ComputerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

class UpdateComputerView(View):
    def get(self, request, pk):
        computer = get_object_or_404(Computer, pk=pk)
        form = ComputerForm(instance=computer)
        return render(request, 'update.html', {'form': form})

    def post(self, request, pk):
        computer = get_object_or_404(Computer, pk=pk)
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
        return redirect('/')

class DeleteComputerView(View):
    def get(self, request, pk):
        computer = get_object_or_404(Computer, pk=pk)
        computer.delete()
        return redirect('/')
    def post(self, request, pk):
        computer = get_object_or_404(Computer, pk=pk)
        computer.delete()
        return redirect('/')

class CreateBrandView(View):
     def get(self, request):
        form = BrandForm()
        context = {
                    'form': form,
                }
        return render(request, 'brandform.html', context)
     
     def post(self, request):
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
class CreateGenerationView(View):
    def get(self, request):
        form = GenerationForm()
        context = {
                    'form': form,
                }
        return render(request, 'generationform.html', context)
    def post(self, request):
        form = GenerationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
class CreateSpecificationView(View):
    def get(self, request):
        form = SpecificationForm()
        context = {
                    'form': form,
                }
        return render(request, 'specificationform.html', context)
    def post(self, request):
        form = SpecificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    def home(request):
            return HttpResponse("<b>home</b>")















