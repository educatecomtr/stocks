from django.views.generic import DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from project.models import Product
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from project.mixins import CheckDistributorObjectMixin


# ürün silme
class ProductDeleteView(CheckDistributorObjectMixin, SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "project/distributor/product/delete.html"
    success_url = reverse_lazy('project:distributor-list-product')
    success_message = "%(name)s başarıyla silindi."
    permission_required = ('project.manage_product',)
