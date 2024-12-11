from gc import get_objects
from lib2to3.fixes.fix_input import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from . models import Post,Comment
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .forms import CommentForm
from .forms import PostForm


class ProjectIndex(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class RegisterUserView(View):
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username already exists.')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email ID already exists.')
            return redirect('register')

        try:
            user = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error occurred: {e}')
            return redirect('register')


class LoginUserView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')


class LogoutUserView(View):
    def get(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('login')


class HomePageView(View):
    template_name = 'home.html'
    def get(self, request):
        posts = Post.objects.all().order_by("-created_on")
        context = {"posts": posts,}
        return render(request, self.template_name, context)


class UpdateUserView(View):
    template_name = 'update.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = request.user
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        if User.objects.filter(username=username).exclude(pk=user.pk).exists():
            messages.error(request, 'This username already exists.')
            return redirect('update')

        try:
            user.username = username
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            messages.success(request, 'Your details have been updated successfully!')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error occurred: {e}')
            return redirect('update')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'resetpassword.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = (
        "We've emailed you instructions for setting your password, "
        "if an account exists with the email you entered. You should receive them shortly. "
        "If you don't receive an email, please make sure you've entered the correct address,"
        " and check your spam folder."
    )
    success_url = reverse_lazy('login')


class PasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_message = "Your password has been reset successfully. You can now log in."
    success_url = reverse_lazy('login')
class CreateBlog(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'createblog.html'
    success_url = reverse_lazy('home')
# class CreateBlog(CreateView):
#     template_name = 'createblog.html'
#     model=Post
#     fields=['title','post_img','body','categories','author']
#     def get(self,request):
#         context={
#             "post":post,
#             "form":PostForm(),
#         }
#         return render(request, self.template_name, context)
#     def post(self, request):
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             form = PostForm()
#         return render(request, self.template_name, {'form': form})


class BlogComment(View):
    template_name = 'comment.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        context = {
            "post": post,
            "comments": comments,
            "form": CommentForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

        comments = post.comments.all()
        context = {
            "post": post,
            "comments": comments,
            "form": form,
        }
        return render(request, self.template_name, context)

