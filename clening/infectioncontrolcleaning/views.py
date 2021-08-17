from django.shortcuts import render, redirect
from .models import BookOrder, Post, Time_id, Order_Ac
from django.views import generic

# Create your views here.
# infectioncontrolcleaning



def infectioncontrolcleaning(request):
    if request.method=='POST':
        print(request)
        postcode = request.POST['q']
        name = request.POST['Name']
        email = request.POST['Email']
        Ph = request.POST['Phone']
        flat_bulding_name = request.POST['flat']
        street_name = request.POST['street']
        service_details = request.POST['service_details']
        infection = request.POST['cleaning']
        appointment_timing_date = request.POST['appointment']
        total_price = request.POST['totalpricesssss']
        user_description = request.POST['note_first']
        note_final = request.POST['note_final']
        
        print(postcode)
        datafrom = BookOrder(postcode=postcode, name=name, email=email, user_description=user_description, note_final=note_final, Ph=Ph,service_details=service_details,infection=infection, flat_bulding_name=flat_bulding_name, street_name=street_name,appointment_timing_date=appointment_timing_date, total_price=total_price)
        datafrom.save()
        return redirect('book')
    else:
        product=Post.objects.all()
        time_list = Time_id.objects.all()
        order_list = Order_Ac.objects.all()
        context={
            "post_list":product,
            "time_list":time_list,
            "order_list": order_list,
        }
    return render(request, 'infectioncontrolcleaning.html',context)