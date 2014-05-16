from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader
from appencuesta.models import Question

def index(request):
    latest_poll_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'encuesta/index.html', context)

#def index(request):
#    latest_poll_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('encuesta/index.html')
#    context = RequestContext(request, {
#        'latest_poll_list': latest_poll_list,
#    })
#    return HttpResponse(template.render(context))

#def index(request):
#    return HttpResponse("Hello, world. You're at the poll index.")

#def index(request):
#    latest_poll_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([p.question_text for p in latest_poll_list])
#    return HttpResponse(output)

def detail(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    return render(request, 'encuesta/detail.html', {'poll': poll})

#def detail(request, poll_id):
#    try:
#        poll = Question.objects.get(pk=poll_id)
#    except Question.DoesNotExist:
#        raise Http404
#    return render(request, 'encuesta/detail.html', {'poll': poll})



#def detail(request, poll_id):
#    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)