from django.shortcuts import render, redirect
from clothrepair.models import Consultation, UserInfo, Question, PriceInfo, Image
from django import forms

# Create your views here.


class ConsulationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ["name", "phoneNumber"]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["name", "phone", "question"]

class PriceForm(forms.ModelForm):
    class Meta:
        model = PriceInfo
        fields = ["priceName", "priceDescrip", "price"]

class ImageForm(forms.ModelForm):
    class Meta:
        modal = Image
        fields = ["nameImg", "image"]

def landingPage(request):
    if request.method == "GET":
        form = ConsulationForm()
        return render(request, 'index.html', {"form": form})

    form = ConsulationForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('landingPage')
    else:
        print(form.errors)

    if request.method == "GET":
        form = QuestionForm()
        return render(request, 'index.html', {"form": form})

    form = QuestionForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('landingPage')
    else:
        print(form.errors)

    datas = PriceInfo.objects.all()
    context = {
        'datas': datas
    }

    return render(request, 'index.html', context)

def infoDelete(request):
    nid = request.GET.get("nid")
    Consultation.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/infoList/")

def quesDelete(request):
    nid = request.GET.get("nid")
    Question.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/quesList/")

def priceDelete(request):
    nid = request.GET.get("nid")
    PriceInfo.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/priceList/")


def loginPage(request):
    return render(request, "login.html")


def registerPage(request):
    return render(request, "register.html")


def infoLists(request):
    consultations_list = Consultation.objects.all()
    return render(request, "info_list.html", {'consultations_list': consultations_list})

def quesLists(request):
    question_list = Question.objects.all()
    return render(request, "ques_list.html", {'question_list': question_list})

def priceLists(request):
    price_list = PriceInfo.objects.all()
    return render(request, "price_list.html", {'price_list':price_list})

def addPrice(request):
    if request.method == "GET":
        form = PriceForm()
        return render(request,'add_price.html',{"form":form})

    form = PriceForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('/priceList/')
    else:
        print(form.errors)

def editPrice(request, nid):

    if request.method == "GET":
        row_object=PriceInfo.objects.filter(id=nid).first()
        return render(request,'price_edit.html', {"row_object":row_object})
    priceName=request.POST.get("priceName")
    priceDescrip=request.POST.get("priceDescrip")
    price=request.POST.get("price")
    PriceInfo.objects.filter(id=nid).update(priceName=priceName, priceDescrip=priceDescrip,price=price)
    return redirect("/priceList")

def imageList(request):
    img_list=Image.objects.all()
    return render(request,'image_list.html',{"img_list":img_list})

def addImage(request):
    form=ImageForm()
    if request.method=="POST":
        form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        redirect('/imageList/')
    else:
        print(form.errors)

    return render(request,'add_img.html',{"form":form})