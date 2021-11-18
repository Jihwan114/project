from django.shortcuts import render, redirect

# Create your views here.

def weight_compare(request):
    return render(request, 'weight_compare.html')