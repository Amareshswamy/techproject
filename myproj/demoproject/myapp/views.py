from django.shortcuts import render
import mysql.connector

# Create your views here.

mydb=mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="college",
charset="utf8"
)

mycur = mydb.cursor()

def index(request):
    return render(request,'index.html')
    
def dashboard(request):
    return render(request,'dashboard.html')
    
def newstudent(request):
        return render(request,'newstudent.html')
              
        
def register(request):
            if request.method=="POST":
                reg = request.POST.get("reg")
                user = request.POST.get("name")
                father_name = request.POST.get("father name")
                contact = request.POST.get("contact")
                branch = request.POST.get("branch")
                gender = request.POST.get("gender")
                address= request.POST.get("address")
                sql= "insert into std_reg(reg,user,father_name,contact,branch,gender,address) values(%s,%s,%s,%s,%s,%s,%s)"
                val=(reg,user,father_name,contact,branch,gender,address)
                mycur.execute(sql,val)
                mydb.commit()
                return render(request,"index.html")


def deletestudent(request):
        return render(request,'deletestudent.html')  
        
def delete(request):
    if request.method=="POST":   
            reg = request.POST.get("reg")
            sql= "delete from std_reg where reg='"+reg+"'"
            mycur.execute(sql)
            mydb.commit()
            return render(request,"index.html")
            
def verify(request):
    if request.method=="POST":
        user=request.POST.get("username")
        psw=request.POST.get("password")
        sql="select * from std_reg where reg='"+user+"' and contact='"+psw+"'"
        mycur.execute(sql);
        if len(mycur.fetchall())>0:
            return render(request,"dashboard.html")
        else:
            return render(request,"index.html",{"status":"invalid username or password"})
        
            
def viewstudent(request):
    sql="select * from std_reg"
    mycur.execute(sql)
    result=mycur.fetchall()
    return render(request,"viewstudent.html",{"res":result})


def viewindividual(request):
     return render(request,'viewindividual.html')
     
                
def individual(request):
    return render(request,'individual.html')

def individual(request):  
        regs = request.POST.get("reg")
        sql="select * from std_reg where reg='"+regs+"'"
        mycur.execute(sql)
        result=mycur.fetchall()
        return render(request,"individual.html",{"res":result})
        
def update(request):
     return render(request,'update.html')
     
                
def showdetails(request):
    reg = request.POST.get("reg")
    sql="select * from std_reg where reg='"+reg+"'"
    mycur.execute(sql)
    result=mycur.fetchall()
    return render(request,'showdetails.html',{"res":result})

                
def updated_details(request):
     if request.method=="POST":
                reg = request.POST.get("reg")
                user = request.POST.get("name")
                father_name = request.POST.get("father name")
                contact = request.POST.get("contact")
                branch = request.POST.get("branch")
                gender = request.POST.get("gender")
                address= request.POST.get("address")
                sql="update std_reg set user='"+user+"',father_name='"+father_name+"',contact='"+contact+"',branch='"+branch+"',gender='"+gender+"',address='"+address+"' where reg='"+reg+"'"
                mycur.execute(sql)
                mydb.commit()
                return render(request,"dashboard.html")
               