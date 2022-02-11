# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from faktury.models import Faktura

class FakturaListView(ListView):
    model = Faktura
    template_name = 'faktury/faktury_list.html'

# Create your views here.
