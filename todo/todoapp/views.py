from django.shortcuts import render

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