from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Product


class IndexView(generic.ListView):
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all().order_by('name')

def buy(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.stock -= 1
    product.save()
    return HttpResponseRedirect(reverse('itemstore:index'))

def restock(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.stock += 1
    product.save()
    return HttpResponseRedirect(reverse('itemstore:index'))
