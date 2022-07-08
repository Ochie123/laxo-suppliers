from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login

from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import ProductEnrollForm


from django.views.generic.list import ListView
from categories.models import Product

from django.views.generic.detail import DetailView
# Create your views here.
class BuyerRegistrationView(CreateView):
    template_name = 'students/student/registration.html' 
    form_class = UserCreationForm
    success_url = reverse_lazy('buyer_product_list') 
    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],password=cd['password1']) 
        login(self.request, user)
        return result

class BuyerEnrollProductView(LoginRequiredMixin, FormView):
    product = None
    form_class = ProductEnrollForm 
    def form_valid(self, form):
        self.product = form.cleaned_data['product'] 
        self.product.buyers.add(self.request.user) 
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('buyer_product_detail',args=[self.product.id])

    
class BuyerProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'students/course/list.html' 
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(buyers__in=[self.request.user])

class BuyerProductDetailView(DetailView):
    model = Product
    template_name = 'students/course/detail.html'
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(buyers__in=[self.request.user])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # get product object
        product = self.get_object()
        if 'subcategory_id' in self.kwargs:
            # get current module
            product['subcategory'] = product.subcategories.get( id=self.kwargs['subcategory_id'])
        else:
            # get first module
            context['subcategory'] = product.subcategories.all()[0] 
            return context