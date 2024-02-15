from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.db import IntegrityError
from .forms import RegisterUserForm, LoginUserForm, UpdateUserForm, UpdatePasswordForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

# Inicio - Se encarga de mostrar el login para loguearse
def index(request):
    if request.user.is_authenticated:
        return redirect('blog')

    if request.method == 'GET':
        return render(request, 'index.html', {
            'form': LoginUserForm
        })
    else:
        requestPost = request.POST

        user = authenticate(request, username=requestPost['username'], password=requestPost['password'])

        if user is None:
            return render(request, 'index.html', {
                'form': LoginUserForm,
                'error': 'El usuario o la contraseña son incorrectas'
            })
        else:
            login(request, user)
            return redirect('blog')

# Registrar - Se encarga de crear un nuevo usuario y de loguearse
def signup(request):
    if request.user.is_authenticated:
        return redirect('blog')

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': RegisterUserForm
        })
    else:
        requestPost = request.POST

        if requestPost['password1'] != requestPost['password2']:
            return render(request, 'signup.html', {
                'form': RegisterUserForm,
                'error': 'Las contraseñas no coinciden'
            })
        
        try:
            form = RegisterUserForm(requestPost)

            if not form.is_valid():
                return render(request, 'signup.html', {
                    'form': RegisterUserForm,
                    'error': form.errors
                })

            form.save()
            user = authenticate(request, username=requestPost['username'], password=requestPost['password1'])
            login(request, user)

            form_profile = UserProfileForm()
            new_profile = form_profile.save(commit=False)
            new_profile.user = user
            new_profile.save()
            
            return redirect('blog')
            
        
        except IntegrityError:
            return render(request, 'signup.html', {
                'form': RegisterUserForm,
                'error': 'Ya existe el usuario'
            })
        except Exception as ex:
            return render(request, 'signup.html', {
                'form': RegisterUserForm,
                'error': ex
            })
        
# Cerrar Sesión - Se encarga de cerrar sesión del usuario
@login_required
def signout(request):
    logout(request)
    return redirect('index')

# Perfil - Se encarga de mostrar información personal del usuario
@login_required
def profile(request):
    if request.method == 'GET':
        form = UpdateUserForm(instance=request.user)
        return render(request, 'profile.html', {
            'form': form
        })
    else:
        form = UpdateUserForm(request.POST, instance=request.user)

        if not form.is_valid():
            return render(request, 'profile.html', {
                'form': form,
                'error': form.errors
            })
        
        try:
            form.save()
            return redirect('blog')
        
        except Exception as ex:
            return render(request, 'profile.html', {
                'form': form,
                'error': ex
            })

# Más información del usuario - Se encarga de mostrar la foto y la URL del usuario
@login_required
def photo_profile(request):
    if request.method == 'GET':
        try:
            form = UserProfileForm(instance=request.user.userprofile)
            return render(request, 'photo_profile.html', {
                'form': form
            })
        except:
            return render(request, 'photo_profile.html', {
                'form': UserProfileForm
            })
    else:
        try:
            form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        except:
            form = UserProfileForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'photo_profile.html', {
                'form': form,
                'error': form.errors
            })
        
        try:
            """ new_photo = form.save(commit=False)
            new_photo.user = request.user
            new_photo.save() """
            form.save()
            return redirect('blog')
        
        except Exception as ex:
            return render(request, 'photo_profile.html', {
                'form': form,
                'error': ex
            })

# Actualizar contraseña - Se encarga de modificar la contraseña actual
@login_required
def update_password(request):
    if request.method == 'GET':
        
        form = UpdatePasswordForm(user=request.user)
        return render(request, 'update_password.html', {
            'form': form
        })
    else:
        form = UpdatePasswordForm(user=request.user, data=request.POST)

        if not form.is_valid():
            return render(request, 'update_password.html', {
                'form': form,
                'error': form.errors
            })
            
        try:
            form.save()
            update_session_auth_hash(request, request.user)
            return HttpResponseRedirect(reverse('blog'))
        
        except Exception as ex:
            return render(request, 'update_password.html', {
                'form': form,
                'error': ex
            })
        
# Error 404 - En modo de producción se encarga de enseñar la pagina 404 por defecto cuando no se haya encontrado ninguna
def handling_404(request, exception):
    return render(request, '404.html', {})