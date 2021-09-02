from json import encoder
from django.contrib import auth, messages
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse,response,HttpResponse
import json
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
import base64
from cars.models import Insert_Data, Register
from django.views.generic import View
import csv
import xlwt
from datetime import datetime
from django.template.loader import render_to_string
from django.template.loader import get_template
import tempfile

# Create your views here.


def moter(request):
    return render(request, "moter.html")


def datatble(request):
    rooms = list(Register.objects.all().values())
    data = dict()
    data['rooms'] = rooms
    return JsonResponse(data)


def showalldata(request):
    data = {'success': False}
    if request.method == "POST":
        fn = request.POST.get('first_data')
        ln = request.POST.get('second_data')
        e = request.POST.get('email_data')
        con = request.POST.get('phone_data')
        c = request.POST.get('cntry_data')
        hby = request.POST['hobby_data']
        g = request.POST['gender_data']
        dob1 = request.POST.get('dob_data')
        # img1 = request.FILES'photo_field']["name"]
        img1 = request.FILES.get('photo_field')
        # print(fn)
        # print(img1)
        # print(g)
        # print(hby)
        b = request.POST.get('bio_data')
        # save inside  Reister table
        form1 = Register.objects.create(
            fname=fn, lname=ln, email=e, mobile=con, country=c, hobby=hby, gender=g, dob=dob1, image=img1, bio=b)
        form1.save()
        messages.info(request, 'Data saved successfully')
        data['success'] = True
        return JsonResponse({'status': 'Success'})
    else:
        return render(request, 'showalldata.html')


def reg(request):
    if request.method == "POST":
        fn = request.POST['first name']
        ln = request.POST['last name']
        e = request.POST['email']
        con = request.POST['num']
        c = request.POST['country']
        g = request.POST['gender']
        b = request.POST['bio']

        # save inside  Register table
        form1 = Register.objects.create(
            fname=fn, lname=ln, email=e, mobile=con, country=c, gender=g, bio=b)
        form1.save()
        messages.info(request, 'Data saved successfully')
        return redirect('/')
    else:
        return render(request, 'register.html')

    return render(request, 'register.html')


def datashow(request):
    sd = Register.objects.all()  # Collect all records from table
    return render(request, 'datashow.html', {'sd': sd})


def deletedata(request, id):
    print(id)
    items = Register.objects.filter(id=id)
    items.delete()
    return redirect('/table')


def editdata(request, id):
    edititem = Register.objects.get(id=id)
    # return redirect('/table')
    if request.method == 'POST':
        edititem.fname = request.POST['fst_nme']
        edititem.lname = request.POST['lst_nme']
        edititem.email = request.POST['mail']
        edititem.save()
   # edititem.fname = firstname
    return render(request, 'editdata.html', {'edt_itm': edititem})


def add_data(request):
    if request.method == 'POST':
        fullname = request.POST['full_name']
        uname = request.POST['user_name']
        email = request.POST['email']
        dob = request.POST['dob']
        pswrd = request.POST['password']
        adding_data = Insert_Data.objects.create(
            full_name=fullname, user_name=uname, email=email, date_of_birth=dob, password=pswrd)
        adding_data.save()
        messages.info(request, 'Huurry! Your data saved successfully')
        return render(request, "add_data.html")
    else:
        return render(request, "add_data.html")


def edit_user(request):
    id = request.POST.get('id')
    # print(id)
    edititem = Register.objects.get(id=id)
    # jo edititem k bad .fname,.lname -ye sb database ki field h firstname, lastname k variable m le kr k json wale code m bhej rahe h------
    my_img = edititem.image
    my_image = json.dumps(str(my_img))
    data = {
        'u_id': edititem.id,
        'firstname': edititem.fname,
        'lastname': edititem.lname,
        'email': edititem.email,
        'phone': edititem.mobile,
        'dob': edititem.dob,
        'city': edititem.country,
        'hobby': edititem.hobby,
        'gender': edititem.gender,
        'prsn_hobby': edititem.hobby,
        'prsn_img': my_image,
        'bio': edititem.bio,
    }
    # print(edititem.gender)
    # print(edititem.hobby)
    # print(edititem.country)
    # print(data.img_edit)
    # print(my_image)
    messages.info(request, 'Data get successfully')
    return JsonResponse(data)


def update_data(request):
    if request.method == "POST":

        u_id = request.POST.get('u_id')
        register = Register.objects.get(id=u_id)

        fn = request.POST['first_data']
        ln = request.POST['second_data']
        e = request.POST['email_data']
        con = request.POST['phone_data']
        c = request.POST.get('cntry_data')
        hby = request.POST['hobby_data']
        g = request.POST['gender_data']
        dob1 = request.POST['dob_data']
        img1 = request.FILES.get('photo_field')
        b = request.POST.get('bio_data')

        register.fname = fn
        register.lname = ln
        register.email = e
        register.mobile = con
        register.country = c
        register.hobby = hby
        register.gender = g
        register.dob = dob1
        register.image = img1
        register.bio = b
        register.save()
        messages.info(request, 'Data updated successfully')

        return JsonResponse({'status': 'success'})
    else:
        return render(request, 'showalldata.html')


def delete_user(request):
    u_id = request.POST.get('updte_id')
    print(u_id)
    user_data = Register.objects.get(id=u_id)
    user_data.delete()
    messages.info(request, 'Data deleted successfully')
    return JsonResponse({'status': 'success'})

# def delete_data_ajx(request, id):
#     data = dict()
#     room = Register.objects.get(id=id)
#     print(room)
#     if room:
#         room.delete()
#         data['message'] = "Data deleted!"
#     else:
#         data['message'] = "Error!"
#     return JsonResponse(data)

def tinymce_prac(request):
    return render(request, 'tiny.html')

"""export table data in CSV form"""
def export_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=export-csv.csv'
    writer = csv.writer(response, csv.excel)
    # response.write(u'\ufeff'.encode('utf8'))
    # writer = csv.writer(response)
    writer.writerow(['First Name','Last Name','Email','Phone No','City'])
    datas = Register.objects.all()

    for data in datas:
        writer.writerow([data.fname,data.lname,data.email,data.mobile,data.country])

    return response

"""export table data in Excel(.xls) form"""
def export_excel(request):
    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=export-excel.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Register',cell_overwrite_ok=True)
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['First Name','Last Name','Email','Phone No','City']
    for column_num in range(len(columns)):
        ws.write(row_num,column_num,columns[column_num],font_style)
    font_style = xlwt.XFStyle()
    rows = Register.objects.all().values_list('fname','lname','email','mobile','country')
    for row in rows:
        row_num+=1

        for column_num in range(len(row)):
            ws.write(row_num,column_num,str(row[column_num]),font_style)
    wb.save(response)
    return response

"""export table data in PDF form"""
def export_pdf(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename=export-PDF.pdf'
    response['Content-Transfer-Encoding']='binary'
    data = Register.objects.all()
    html_string = render_to_string('pdf-output.html',{'data':data})
    html = render_to_pdf(response,string = html_string)
    html.init_report()
    result = html.write_pdf()
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.open(output.name,'rb')
        response.write(output.read())

    return response()