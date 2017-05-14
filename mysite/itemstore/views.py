from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db import transaction

from .models import Product


class IndexView(generic.ListView):
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all().order_by('name')

def buy(request, product_id):
    with transaction.atomic():
        product = get_object_or_404(Product.objects.select_for_update(), pk=product_id)
        product.stock -= 1
        product.save()
        messages.success(request, "You have bought %s" % product.name)
        return redirect('itemstore:index')

def restock(request, product_id):
    with transaction.atomic():
        product = get_object_or_404(Product.objects.select_for_update(), pk=product_id)
        product.stock += 1
        product.save()
        messages.success(request, "You have restocked %s" % product.name)
        return redirect('itemstore:index')
