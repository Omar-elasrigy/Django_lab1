from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list(req):
    list=[]
    trainee1={'id':1,'name':'Omar Elasrigy','track_id':5}
    trainee2={'id':2,'name':'Ayman Ahmed','track_id':7}
    trainee3={'id':3,'name':'Karim Wael','track_id':3}
    list.append(trainee1)
    list.append(trainee2)
    list.append(trainee3)
    context={}
    context['trainees']=list
    return render (req,'trainee/list.html',context)
    

def update_trainee(req,id):
    print(req.GET)
    return render (req,'trainee/update.html',{'id':id})

def delete_trainee(req,id):
    return render (req,'trainee/delete.html',{'id':id})
def show_details_trainee(req,id):
    return render (req,'trainee/showDetails.html',{'id':id})
def create(req):
    return render (req,'trainee/create.html')


