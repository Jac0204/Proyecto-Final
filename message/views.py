from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import MessageForm
from .models import Message

# Create your views here.
# Mensajería - Se encarga de mostrar el chat de todos los usuarios
def message(request):
    if request.method == 'GET':
        users = User.objects.all()
        messages = Message.objects.all()
        form = MessageForm()

        return render(request, 'message.html', {
            'users': users,
            'messages': messages,
            'form': form
        })
    else:
        users = User.objects.all()
        messages = Message.objects.all()
        form = MessageForm(request.POST)

        if not form.is_valid():
            return render(request, 'message.html', {
                'users': users,
                'messages': messages,
                'form': form,
                'error': form.errors
            })
        
        try:
            new_message = form.save(commit=False)
            new_message.usuario = request.user
            new_message.save()

            return redirect('message')
        except Exception as ex:
            return render(request, 'message.html', {
                'users': users,
                'messages': messages,
                'form': form,
                'error': ex
            })