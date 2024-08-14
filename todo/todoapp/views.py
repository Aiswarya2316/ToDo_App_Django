from django.shortcuts import render,redirect

# Create your views here.
def index(req):
    return render(req,'index.html')

td=[]
def insert(req):
    if req.method=="POST":
        name=req.POST['name']
        age=req.POST['age']
        mark=req.POST['mark']
        ID=req.POST['ID']
        discription=req.POST['discription']
        td.append({'nm':name , 'ag':age , 'mk':mark ,'ID':ID , 'dis':discription})
        print(td)
        return render(req,'insert.html',{'data':td})
    else:       
        return render(req,'insert.html',{'data':td})  

def display(req):
    return render(req,'display.html',{'data':td})    

def edit(req,std):
    std1={}
    pos=0
    for i in td:
        if i['nm']==std:
            std1=i
            pos=td.index(i)
    if req.method=="POST":
        name=req.POST['name']
        age=req.POST['age']
        mark=req.POST['mark']
        td[pos]={'nm':name , 'ag':age , 'mk':mark}
        return redirect(insert)
    else:   
         return render(req,'edit.html',{'data':std1})     

def delete(req,name):
    for i in td:
        if i['nm']==name:
            td.remove(i)
            return redirect(insert)
    return render
