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

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    return HttpResponse("Bienvenido a PUPILS CAMPUS APP")


def working(request):
    return render_to_response('working.html',context_instance=RequestContext(request))
def hora_actual (request) 
    now = datetime.now()
    html="Son las %s.", %now
    return HttpResponse(html)

