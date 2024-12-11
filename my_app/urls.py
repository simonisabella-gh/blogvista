
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    #path('',views.ProjectIndex.as_view()),
    path("RegisterView/",views.RegisterUserView.as_view(),name='register'),
    path("",views.LoginUserView.as_view(),name='login'),
    path("HomeView/",views.HomePageView.as_view(),name='home'),
    path("LogoutView/",views.LogoutUserView.as_view(),name='logout'),
    path("UpdateView/",views.UpdateUserView.as_view(),name='update'),
    path("ResetpasswordView/",views.ResetPasswordView.as_view(),name='resetpassword'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path("CreateBlogView/", views.CreateBlog.as_view(), name='createblog'),
    path("CommentView/<int:pk>/",views.BlogComment.as_view(),name='blogcomment'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)