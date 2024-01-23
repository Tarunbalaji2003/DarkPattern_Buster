from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
from pythonfile import test

templates = Jinja2Templates(directory="templates")
app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
def front(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post("/code")
def code(request:Request,title:str=Form(...),img:str=Form(...),price:str=Form(...),delprice:str=Form(...),des:str=Form(...),pid:str=Form(...)):
    records = get_content_review(pid)
    result = test(des)
    print(result)
    return templates.TemplateResponse("detail.html", {"request": request,"img":img,"title":title,"price":price,"delprice":delprice,"des":des,"id":pid,"records":records})
    

@app.get("/report/{id}")
def report(request:Request,id:int):
    return templates.TemplateResponse("Report.html", {"request": request,"id":id})


@app.post("/report-submit")
def report(request:Request,name:str=Form(...),emailid:str=Form(...),msgContent:str=Form(...),pid:str=Form(...)):
    print(name,msgContent,emailid,pid)
    connector_push(name,msgContent,emailid,pid)
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/review/{id}")
def report(request:Request,id:int):
    return templates.TemplateResponse("Review.html", {"request": request,"id":id})


@app.post("/review-submit")
def report(request:Request,name:str=Form(...),msgContent:str=Form(...),pid:str=Form(...)):
    print(name,msgContent,pid)
    connector_push_review(name,msgContent,pid)
    return templates.TemplateResponse("index.html", {"request": request})


def connector_push(name,msgContent,emailid,pid):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dinesh",
    database="dark_pattern")
    mycursor = mydb.cursor()
    print("Connection Estabilished")
    mycursor.execute("INSERT INTO report values(%d,'%s','%s','%s')" %(int(pid),name,emailid,msgContent))
    mydb.commit()
    mydb.close()

def connector_push_review(name,msgContent,pid):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dinesh",
    database="dark_pattern")
    mycursor = mydb.cursor()
    print("Connection Estabilished")
    mycursor.execute("INSERT INTO review values(%d,'%s','%s')" %(int(pid),name,msgContent))
    mydb.commit()
    mydb.close()  

def get_content_review(pid):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dinesh",
    database="dark_pattern")
    mycursor = mydb.cursor()
    print("Connection Estabilished")
    mycursor.execute("SELECT * FROM review WHERE pid=%d" %(int(pid)))
    record = mycursor.fetchall()
    mydb.close()
    return record



