# -*- coding: utf-8 -*-
"""
Copyright (C) 2012 Fco. Javier Lucena Lucena (https://forja.rediris.es/users/franlu/)
Copyright (C) 2012 Serafín Vélez Barrera (https://forja.rediris.es/users/seravb/)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation; either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU Affero General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

from django.conf.urls.defaults import patterns, include, url
from pupils.settings import MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^usuario/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name="logout"),
    url(r'^usuario/', include('registration.backends.default.urls')),

    url(r'^pcontrol/diploma/$', 'pupils.users.views.diploima_pdf',name="diploima_pdf"),
    url(r'^pcontrol/tablon/', include('tablon.urls')),
    url(r'^pcontrol/inscripcion/$', 'pupils.users.views.inscribir_hijo', name="inscribir_hijo"),
    url(r'^pcontrol/$', 'pupils.users.views.panel', name="panel"),
    url(r'^pcontrol/uploadpdf/$', 'pupils.users.views.upload_pdf', name="upload_pdf"),
    
    url(r'^pcontrol/encuesta/(?P<idencuesta>\d+)/$', 'pupils.encuesta.views.encuesta_rellenar', name="encuesta_rellenar"),
    url(r'^pcontrol/encuesta/$', 'pupils.users.views.encuesta', name="encuesta"),
    url(r'^actividad/(?P<idactividad>\d+)/$', 'pupils.actividad.views.detalle', name="actividad_detalle"),
    url(r'^$', 'pupils.views.home', name='home'),
    
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #Media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
