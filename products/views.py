from .tasks import log_new_product
from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

class ProductCreateView(CreateView):
    model=Product
    form_class=ProductForm
    template_name=('products/create.html')
    success_url=reverse_lazy('product_create')
    context_object_name='products'

    def form_valid(self, form):
        response = super().form_valid(form)
        log_new_product.delay(self.object.name)
        return response
    
class ProductUpdateView(UpdateView):
    model=Product
    form_class=ProductForm
    template_name=('products/update.html')
    success_url=reverse_lazy('list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        log_new_product.delay(f"ОБНОВЛЕН: {self.object.name}")
        return response

class ProductDetailView(DetailView):
    model=Product
    template_name='products/detail.html'
    context_object_name='product'


class ProductDeleteView(DeleteView):
    model=Product
    template_name='products/delete.html'
    success_url=reverse_lazy('list')

    def form_valid(self, form):
        product_name = self.get_object().name 
        response = super().form_valid(form)
        log_new_product.delay(f"УДАЛЁН: {product_name}")
        return response
    

class ProductListView(ListView):
    model=Product
    template_name='products/list.html'
    context_object_name = 'products'

