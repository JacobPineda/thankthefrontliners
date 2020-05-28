from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Message

from .forms import MessageForm
# Create your views here.

def index(request):
  all_messages_list = Message.objects.all().order_by('-date_created')
  page = request.GET.get('page', 1)
  paginator = Paginator(all_messages_list, 15)

  try:
    messages = paginator.page(page)
  except PageNotAnInteger:
    messages = paginator.page(1)
  except EmptyPage:
    messages = []

  context = {
    'latest_messages_list': messages,
    'form': MessageForm()
  }
  return render(request, 'thanks/index.html', context)

def add(request):
  form = MessageForm(request.POST)
  if(form.is_valid()):
    message = Message(content=form.cleaned_data['content'], name=form.cleaned_data['name'], color=form.cleaned_data['color'])
    message.set_user()
    message.set_color()
    message.save()
  return redirect('/')
