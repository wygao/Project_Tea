from blog.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django import forms

def index(req):
	category_list = Category.objects.all()
	up_category = [category for category in category_list if category.p_category is None]
	goods_list = Goods.objects.all()
	return render(req,'index.html',{'up_category':up_category,'goods_list':goods_list})

def disp_goods(req):
	category_list = Category.objects.all()
	up_category = [category for category in category_list if category.p_category is None]
	cid = req.GET.get('cid')
	sec_category = Category.objects.get(id=cid)
	goods_list = sec_category.goods_set.all()
	print goods_list
	return render(req,'disp_goods.html',{'up_category':up_category,'goods_list':goods_list})

class RegistUserForm(forms.ModelForm):
	class Meta:
		models = User
		fields = ('username','password')
class RegistProUserForm(forms.ModelForm):
	class Meta:
		models = ProUser
		fields = ('tel','addr','QQ')
def regist_user(req):
	if req.method == "POST":
		rf1 = RegistUserForm(req.POST)
		rf2 = RegistProUserForm(req,POST)
		if rf1.is_valid() and rf2.is_valid:
			rf1.instance.is_staff = True
			rf1.instance.set_password(rf1.cleaned.data['password'])
			rf1.save()
			rf2.instance.user = rf1.instance
			rf2.save()
			return HttpResponse("ok")
	else:
		rf1 = RegistUserForm()
		rf2 = RegistProUserForm()
	return render(req,'index.html',{'rf1':rf1,'rf2':rf2})
			



















	
