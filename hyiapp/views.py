from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def main(request):
    logging.info('')
    return HttpResponse("Zdorova")

def about(request):
    return HttpResponse('Che nado?')