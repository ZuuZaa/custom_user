from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import Account
from .forms import RegistrationForm


class RegistrationView(CreateView):
    template_name = 'account/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url


class ProfileView(UpdateView):
    model = Account
    fields = ['name', 'phone', 'date_of_birth', 'picture']
    template_name = 'account/profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user







# from blog.models import BlogPost



# def registration_view(request):
# 	context = {}
# 	if request.POST:
# 		form = RegistrationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			email = form.cleaned_data.get('email')
# 			raw_password = form.cleaned_data.get('password1')
# 			account = authenticate(email=email, password=raw_password)
# 			login(request, account)
# 			return redirect('home')
# 		else:
# 			context['registration_form'] = form

# 	else:
# 		form = RegistrationForm()
# 		context['registration_form'] = form
# 	return render(request, 'account/register.html', context)


# def logout_view(request):
# 	logout(request)
# 	return redirect('/')


# def login_view(request):

# 	context = {}

# 	user = request.user
# 	if user.is_authenticated: 
# 		return redirect("home")

# 	if request.POST:
# 		form = AccountAuthenticationForm(request.POST)
# 		if form.is_valid():
# 			email = request.POST['email']
# 			password = request.POST['password']
# 			user = authenticate(email=email, password=password)

# 			if user:
# 				login(request, user)
# 				return redirect("home")

# 	else:
# 		form = AccountAuthenticationForm()

# 	context['login_form'] = form

# 	# print(form)
# 	return render(request, "account/login.html", context)


# def account_view(request):

# 	if not request.user.is_authenticated:
# 			return redirect("login")

# 	context = {}
# 	if request.POST:
# 		form = AccountUpdateForm(request.POST, instance=request.user)
# 		if form.is_valid():
# 			form.initial = {
# 					"email": request.POST['email'],
# 					"username": request.POST['username'],
# 			}
# 			form.save()
# 			context['success_message'] = "Updated"
# 	else:
# 		form = AccountUpdateForm(

# 			initial={
# 					"email": request.user.email, 
# 					"username": request.user.username,
# 				}
# 			)

# 	context['account_form'] = form

# 	blog_posts = BlogPost.objects.filter(author=request.user)
# 	context['blog_posts'] = blog_posts

# 	return render(request, "account/account.html", context)


# def must_authenticate_view(request):
# 	return render(request, 'account/must_authenticate.html', {})