# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from ragendja.template import render_to_response
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse

from getid.models import InterestedPerson
from getid.forms import InterestedPersonForm

from django.views.generic.create_update import create_object

def thanks(request):
    return render_to_response(request, 'getid/thanks.html')

def survey_thanks(request):
    return render_to_response(request, 'getid/survey_thanks.html')
    
def get_interested_email(request):
    return create_object(request, form_class=InterestedPersonForm,
        post_save_redirect=reverse('getid.views.thanks'))