from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import test
from .models import result

# Create your views here.
def covid(request):
	return render(request,'covid.html')


def home(request):
	return render(request,'home.html')

def owner(request):
	return render(request,'owner.html')	

def register(request):
	if request.method=='POST':
		name=request.POST.get('name')
		age=request.POST.get('age')
		
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		
		data=test(Name=name,Age=age,Email=email,Phone=phone)
		data.save()
		return render(request,'ct.html')
	return render(request,'register.html')

def precautions(request):
	return render(request,'precautions.html')	
		
def symptoms(request):
	return render(request,'symptoms.html')	

def ct(request):
	if request.method=="POST":
		

		db=request.POST.get('dbsb')
		cpp=request.POST.get('cpp')
		lsm=request.POST.get('lsm')
		f=request.POST.get('f')
		dc=request.POST.get('dc')
		t=request.POST.get('t')
		ap=request.POST.get('ap')
		st=request.POST.get('st')
		d=request.POST.get('d')
		c=request.POST.get('c')
		h=request.POST.get('h')
		lts=request.POST.get('lts')
		r=request.POST.get('r')
		obj=test.objects.last()
		



		data=result(Name=obj.Name,Email=obj.Email,Phone=obj.Phone,difficult_breathing=db,chestpain=cpp,loss_of_speech=lsm,fever=f,dry_cough=dc,tiredness=t,aches_and_pains=ap,sore_throat=st,diarrhoea=d,conjunctivitis=c,headaches=h,loss_of_taste=lts,rash_on_skin=r)
		data.save()

		



		ser=[db,cpp,lsm]
		mcs=[f,dc,t]
		lcs=[ap,st,d,c,h,lts,r]
		
		if ('YES' in ser):
			#return HttpResponse('go to hospital')
			return render(request,'hos.html')
		elif ('YES' in mcs):
			#return HttpResponse('go to quarantinee')
			return render(request,'quar.html')
		elif ('YES' in lcs):
			#return HttpResponse('take care')
			return render(request,'care.html')	

		'''if db=="YES" or cpp=='YES' or lsm=='YES':
			return HttpResponse('go to hospital')
		elif f=='YES' or dc=='YES' or t=='YES':
			return HttpResponse('go to quarantinee')
		else:
			return HttpResponse('take care')'''
				
		
	return render(request,'ct.html')	
