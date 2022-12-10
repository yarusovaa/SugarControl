from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Person, BloodMeasurement
import datetime
# Create your views here.
def index(request):
    if request.session.has_key('personId'):
        if request.method == "GET":
            return render(request, "html/index.html")
        else:
            date = request.POST.get("datetime")
            return HttpResponsePermanentRedirect("/tabel/"+format(date))
    else:
        return HttpResponsePermanentRedirect("/login/")


def output(request):
    if request.session.has_key('personId'):
        del request.session['personId']
    return HttpResponsePermanentRedirect("/login/")

def renderTabel(request, date):
    if  request.session.has_key('personId'):
        if request.method == "GET":
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            person = Person.objects.get(id = int(request.session['personId']))
            alert = 0 # 0 нет придупрежнения,  1 Высокий сахар,  -1  низкий сахар
            listMeasurementX = []
            for k in range(1, 8):
                Measurement = BloodMeasurement.objects.filter(Person = person, Date = date, TypeMeasurement = k)
                if len(Measurement) != 0:
                    value = Measurement[len(Measurement)-1].DataMeasurement
                    if value > 10:
                        alert = 1
                    elif value < 2.5:
                        alert = -1
                    listMeasurementX.append(value)
                else:
                    listMeasurementX.append(0)


            dataPage = {"listMeasurement":listMeasurementX, "Dates":date, "Person":person, "alert":alert}
            return render(request, "html/tabel.html", dataPage)

    else:
        return HttpResponsePermanentRedirect("/login/")

def addMeasurement(request, date, typeMeasurment):
    print("Хелло")
    if request.session.has_key('personId'):
            if request.method == "GET":
                return render(request, "html/addMeasurement.html",{"datatime":date, "typeMeasurment":typeMeasurment})
            else:
                GetDate = request.GET.get('date')
                print(GetDate)
                inputDatetime = request.POST.get("datetime")
                #print(inputDatetime)
                inputMeasurement = request.POST.get("dataMeasurement")
                print(inputMeasurement)
                typeMeasurement = int(request.POST.get("TypeMeasurement"))
                person = Person.objects.get(id = int(request.session['personId']))
                Measurement = BloodMeasurement.objects.filter(Person = person, Date = inputDatetime, TypeMeasurement = typeMeasurement)
                if len(Measurement) == 0:
                    BloodMeasurement.objects.create(Person = person, DataMeasurement = inputMeasurement, TypeMeasurement = typeMeasurement, Date = inputDatetime)
                elif len(Measurement) > 0:
                    Measurement.delete()
                    BloodMeasurement.objects.create(Person = person, DataMeasurement = inputMeasurement, TypeMeasurement = typeMeasurement, Date = inputDatetime)
                return HttpResponsePermanentRedirect("/tabel/"+date)
    else:
        return HttpResponsePermanentRedirect("/login/")

def login(request):
    if request.method == "GET":
        return render(request, "html/login.html",)
    else:
        login = request.POST.get("Login")
        password = request.POST.get("Password")
        try:
            person = Person.objects.get(Login = login, Password = password)
            request.session["personId"] = str(person.id)
            return HttpResponsePermanentRedirect("/")
        except ObjectDoesNotExist:
            render(request, "html/login.html",)
    return render(request, "html/login.html",)

def singUp(request):

    if request.method == "GET":
        return render(request, "html/registration.html",)
    else:
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        birthday = request.POST.get("birthday")
        login = request.POST.get("login")
        password = request.POST.get("password")
        twoPassword = request.POST.get("twoPassword")
        try:
            Person.objects.get(Login=login)
            return HttpResponsePermanentRedirect("/login/")
        except ObjectDoesNotExist:
            person = Person.objects.create(Name = name, Surname = surname, Birthday = birthday, Password = password, Login = login).id
            request.session['personId'] = str(person)
            return HttpResponsePermanentRedirect("")


