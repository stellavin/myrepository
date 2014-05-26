

from django.conf.urls.defaults import *
from database1.views import get_fname, get_cname
from database1.sis.views import get_section, search


urlpatterns = patterns('',
	(r'^facultyname/(.{3,9})/$', get_fname),
	(r'^coursename/(.{3,9})/$', get_cname),
	(r'^sectioninfo/(.{3,9})/$', get_section),
	(r'^searchSection/$', search),
)
