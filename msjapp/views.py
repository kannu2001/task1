from django.shortcuts import render, HttpResponse,redirect
from msjapp.models import FormData

# Create your views here.
def sendmsg(request):
    #print("method is:",request.method)
    if request.method=="GET":
       return render(request,'sendmessage.html')
    else:
        n=request.POST['uname']
        #print(n)
        mb=request.POST['umobile']
        #print(mb)
        mail=request.POST['uemail']
        #print(mail)
        msg=request.POST['umsg']
        #print(msg)
        m=FormData.objects.create(name=n,mobile=mb,email=mail,msg=msg)
        m.save()
        #return HttpResponse("data fetched...")
        return redirect('/dashboard')

    

def dashboard(request):
    m=FormData.objects.all()
    print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)

def delete(request,rid):
    m=FormData.objects.filter(id=rid)
    #print(m)
    m.delete()
    return redirect('/dashboard')

def edit(request,rid):
    if request.method=="GET":
       m=FormData.objects.filter(id=rid)
       context={}
       context['data']=m
       return render(request,'edit.html',context)
    else:
        un=request.POST['uname']
        umb=request.POST['umobile']
        umail=request.POST['uemail']
        umsg=request.POST['umsg']
        #m=SendMsg.objects.update(name=un,email=umail,mobile=umb,msg=umsg)
        m=FormData.objects.filter(id=rid)
        m.update(name=un,email=umail,mobile=umb,msg=umsg)
        return redirect('/dashboard')