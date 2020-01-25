from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from .models import contactdb
from .models import orderfromwebsite
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
import random

MERCHANT_KEY='H@YnLbyCrUlW8bE4'

def FirstCharCapital(items):
    lists = items.split(" ")
    catprods = ""
    # items=list(items)
    for i in range(len(lists)):
        items = list(lists[i])
        if (ord(items[0]) < 65 or ord(items[0]) > 90):
            items[0] = chr(ord(items[0]) - 32)
        val = ("".join(items))  # first letter can be capitalise using .title function
        catprods += val + " "
    catprods = "".join(catprods)
    return catprods
# Create your views here.
def index(request):
    allproducts=product.objects.all()
    n=len(allproducts)
    if (n % 4 == 0):
        slides = n // 4
    else:
        slides = (n // 4) + 1
    Category=product.objects.values("Category")
    ProdName=(product.objects.values("productname"))
    prodName={ items['productname'] for items in ProdName}
    ProdName=FirstCharCapital(str(prodName))
    lists={ item['Category'] for item in Category}
    databases=[]
    for items in lists:
        element=product.objects.filter(Category=items)
        n=len(element)
        if (n % 4 == 0):
            no_slides = n // 4
        else:
            no_slides = ( n // 4 )+ 1
        catprods=FirstCharCapital(items);
        databases.append([range(1,n),element,catprods])
    params={'allprods':databases,'product':allproducts,'nslides':slides,'range':range(0,slides),'length':len(databases)}
    # databases={'catlen':length,'category':lists,'total_slides':slides,'range':range(1,slides),'product':products,'val':range(1,n)}
    return render(request,'index.html',params)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def cart(request):
    return render(request,'cart.html')
def tracker(request):
    return render(request,'tracker.html')
def search(request):
    return render(request,'search.html')
def productview(request,myid):
    prodViewDetails={product.objects.filter(id=myid)}
    myCart={prodViewDetails[0] for prodViewDetails in prodViewDetails}
    return render(request,'productview.html',{"cartProduct":myCart})
def checkoutPage(request,checkoutId):
    prodViewDetails={product.objects.filter(id=checkoutId)}
    # myCart={prodViewDetails[0] for prodViewDetails in prodViewDetails}

    myCart=allproducts=product.objects.all()
    return render(request,'checkout.html',{"cartProduct":myCart})
def billingpage(request,billingid):
    prodViewDetails={product.objects.filter(id=billingid)}
    myCart={prodViewDetails[0] for prodViewDetails in prodViewDetails}
    return render(request,'billing.html',{"cartProduct":myCart})

def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        email = request.POST.get("email")
        checkbox = request.POST.get("checkbox")
        comment = request.POST.get("desc")
        if(checkbox=="on"):
            checkbox=1
        else:
            checkbox=0
        contactsweget=contactdb(Name=name,Phone=phone,Email=email,Address=address,CheckBox=checkbox,Comment=comment)
        contactsweget.save()
    return render(request,"contact.html")

def handlepaymentmode(request):
    if(request.method=="POST"):
        price=request.POST.get("price")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        phone_number=request.POST.get("phone_number")
        email=request.POST.get("email")
        state=request.POST.get("state")
        city=request.POST.get("city")
        code=request.POST.get("code")
        local=request.POST.get("local")
        w=[]
        rd=random.randint(1,4000)
        if rd not in w:
            w.append(rd)
        orderId=w[len(w)-1]
        customeroredered = orderfromwebsite(orderId=orderId,price=price,first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,state=state,city=city,code=code,local=local,)
        customeroredered.save()
        data_dict = {
            'MID': 'hoIoYf23662428021793',
            'ORDER_ID': "LXI"+str(orderId),
            'TXN_AMOUNT': str(price),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/paytmsentposturl'
        }
        data_dict['CHECKSUMHASH']=Checksum.generate_checksum(data_dict,MERCHANT_KEY)
        return render(request,"paytmhit.html",{'params':data_dict})


@csrf_exempt
def paytmsentposturl(request):
    # post request hitted here by paytm
    data=request.POST
    print(data)
    return_response_by_paytm={}
    for i in data.keys():
        return_response_by_paytm[i]=data[i]
        if i=='CHECKSUMHASH':
            checksum=data[i]
    verify = Checksum.verify_checksum(return_response_by_paytm, MERCHANT_KEY,checksum)
    if(verify):
        if return_response_by_paytm['RESPCODE']=='01':
            print("order successful")
        else:
            print("order not successful!")
    else:
        print("OOPS")
    return render(request,"paytmsatuspage.html",{'paytmresponse':return_response_by_paytm});