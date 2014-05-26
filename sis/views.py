# Create your views here.

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q, F
from models import section

def get_section(request, sid):
	result = section.objects.filter(snum=sid)
	if result.count() == 0:
		html = "<html><body>There is no Section with number %s.</body></html>" % sid
	else:
		t = get_template('section.html')
		w = result.values()
		c = Context(w[0])
		html = t.render(c)
	return HttpResponse(html)
	
	
def search(request):
	error = False
	if 'cnum' in request.GET:
		cid = request.GET['cnum']
	if not cid:
		error = True
	else:
			sections = section.objects.filter(cnum__exact=cid).filter(enrollment__lt=F('capacity'))
			return render_to_response('search_results.html',{'sections': sections, 'query': cid})
return render_to_response('search_form.html', {'error': error})

