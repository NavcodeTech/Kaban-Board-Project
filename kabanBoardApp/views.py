from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from .models import *

def newcard(request):
    if request.method == 'POST':
        if 'data' in request.POST:
            cardno = request.POST.get('cardno')
            taskname = request.POST.get('taskn')
            taskid = request.POST.get('taskid')
            department = request.POST.get('department')
            team = request.POST.get('team')
            addinfo = request.POST.get('addinfo')
            expecttime = request.POST.get('expecttime')
            duedate = request.POST.get('duedate')

            cardInfo=CardInfo.objects.create(cardno=cardno,taskname=taskname,taskid=taskid,department=department,
                                         team=team,addinfo=addinfo,expecttime=expecttime,duedate=duedate)
            cardInfo.save()
            return render(request, 'kabanBoardApp/newcard.html')
        else:
            return render(request, 'kabanBoardApp/newcard.html')
    else:
        return render(request, 'kabanBoardApp/newcard.html')


def home(request):
    cards = CardInfo.objects.all()
    progress = ProgressInfo.objects.all()
    complete = CompleteInfo.objects.all()
    if request.method == 'POST':
        if 'progress' in request.POST:
            cardno = request.POST.get('cardno')
            taskid = request.POST.get('taskid')
            taskname = request.POST.get('taskname')
            progresscard = ProgressInfo.objects.create(cardno=cardno,taskid=taskid,taskname=taskname)
            progresscard.save()
            card = CardInfo.objects.filter(taskname=taskname)
            card.delete()
            cards = CardInfo.objects.all()
            progress = ProgressInfo.objects.all()
            complete = CompleteInfo.objects.all()

            return render(request, 'kabanBoardApp/home.html',{'progress':progress,'cards':cards,'complete':complete})
        if 'complete' in request.POST:
                cardno = request.POST.get('cardno')
                taskid = request.POST.get('taskid')
                taskname = request.POST.get('taskname')
                completecard = CompleteInfo.objects.create(cardno=cardno, taskid=taskid, taskname=taskname)
                completecard.save()
                card = ProgressInfo.objects.filter(taskname=taskname)
                card.delete()
                cards = CardInfo.objects.all()
                progress = ProgressInfo.objects.all()
                complete = CompleteInfo.objects.all()
                return render(request, 'kabanBoardApp/home.html',
                          {'progress': progress, 'cards': cards, 'complete': complete})
        if 'delete' in request.POST:
                cardno = request.POST.get('cardno')
                taskid = request.POST.get('taskid')
                taskname = request.POST.get('taskname')
                card = CompleteInfo.objects.filter(taskname=taskname)
                card.delete()
                cards = CardInfo.objects.all()
                progress = ProgressInfo.objects.all()
                complete = CompleteInfo.objects.all()
                return render(request, 'kabanBoardApp/home.html',
                          {'progress': progress, 'cards': cards, 'complete': complete})
        else:
            return render(request, 'kabanBoardApp/home.html',
                          {'progress': progress, 'cards': cards, 'complete': complete})
    else:
        return render(request, 'kabanBoardApp/home.html',
                      {'progress': progress, 'cards': cards, 'complete': complete})
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password, sep=" ")
        user = authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            print("LoggedIn successfully")
            return redirect('home')
        else:
            print("Invalid credentials")
            messages.info(request, "Invalid Password/Username")
            return redirect('login')
    else:
        return render(request, 'kabanBoardApp/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')