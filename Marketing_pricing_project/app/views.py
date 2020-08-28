from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ProductTableForm
from .models import ProductTAble
# Create your views here.

def index(request):
  ptf=ProductTableForm
  pt=ProductTAble.objects.all()
  return render(request,"index.html",{"ptf":ptf,'pt':pt})

def prd_added(request):
    id=request.POST.get('prd_id')
    nm=request.POST.get('prd_name')
    qnty=request.POST.get('prd_qunty')
    mnfdt=request.POST.get('prd_manufdt')
    exdt=request.POST.get('prd_expdt')
    prc=request.POST.get('prd_price')
    ProductTAble(prd_id=id,prd_name=nm,prd_quntity=qnty,prd_manf_dt=mnfdt,prd_exp_dt=exdt,prd_price=prc).save()
    messages.success(request,"product added succesfully")
    return redirect('index')


def delete(request):
    del_no=request.GET.get('idno')
    ProductTAble.objects.filter(prd_id=del_no).delete()
    return redirect('index')


