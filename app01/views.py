from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Avg
from app01 import models
# Create your views here.
NOWNAME = "未开始"

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        if NOWNAME == '未开始':
            return render(request,'notStart.html')
        score = request.POST.get('ratescore')
        selfgroup = request.POST.get('selfgroup')
        try:
            score = int(score)
        except Exception as e:
            return render(request,'valueerror.html')
        if score not in range(0,101):
            return render(request,'valueerror.html')
        if selfgroup == '1':
            obj = models.GroupScore.objects.create(
                name = NOWNAME,
                score = score
            )
        else:
            obj = models.AllScore.objects.create(
                name = NOWNAME,
                score = score
            )
        return render(request,'sucess.html')

def admin(request):
    if request.method == 'GET':
        objs = models.Names.objects.all().order_by('-e_score')
        return render(request,'admin.html',{'objs':objs})

def current_name(request):
    return HttpResponse(NOWNAME)

def startreply(request,id):
    global NOWNAME
    if request.method == 'GET':
        obj = models.Names.objects.get(id = id)
        if obj.status == "答辩中":
            return redirect('/admin/')
        models.Names.objects.filter(id = id).update(status="答辩中")
        NOWNAME = obj.name
        return redirect('/admin/')

def endreply(request):
    if request.method == 'GET':
        gruop_count = models.GroupScore.objects.filter(name=NOWNAME).count()
        all_count = models.AllScore.objects.filter(name=NOWNAME).count()
        count = gruop_count+all_count
        return render(request, 'endconform.html', {'all_count':count, 'username':NOWNAME})

def conform_end(request):
    global NOWNAME
    if request.method == 'GET':
        g_score = models.GroupScore.objects.filter(name=NOWNAME).values('name').annotate(a=Avg('score')).values('a')
        try:
            g_score = g_score[0]['a']
        except:
            g_score = 0
        a_score = models.AllScore.objects.filter(name=NOWNAME).values('name').annotate(a=Avg('score')).values('a')
        try:
            a_score = a_score[0]['a']
        except:
            a_score = 0
        e_score =  (g_score+a_score) / 2
        models.Names.objects.filter(name=NOWNAME).update(
            g_score = g_score,
            a_score = a_score,
            e_score = e_score,
            status="答辩完成",
        )
        NOWNAME = "未开始"
        return redirect('/admin/')