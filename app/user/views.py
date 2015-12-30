# Create your views here.
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView, UpdateView, DetailView

from app.like.function import return_user_like_post
from app.post.models import Post
from app.user.models import Profile


class Index(TemplateView):
    template_name = 'user/timeline/time_line.html'
    # login = False
    #
    # def dispatch(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated():
    #         self.login = True
    #     else:
    #         self.login = False
    #
    # def get_context_data(self, **kwargs):
    #     ctx = super(Index, self).get_context_data(**kwargs)
    #     ctx['login'] = self.login
    #     if self.login:
    #         pass
    #     else:
    #         pass
    #     return ctx


IndexView = Index.as_view()


class Home(DetailView):
    model = User
    template_name = 'user/home/home.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        self.object = User.objects.get(username=self.kwargs['username'])
        return self.object

    def get_context_data(self, **kwargs):
        ctx = super(Home, self).get_context_data(**kwargs)
        ctx['posts'] = Post.objects.filter(profile__user=self.object)[:10]
        # ctx['posts'].total_like =    Post.objects.filter(profile__user=self.object).
        for post in ctx['posts']:
            post.total_like = post.get_total_like()
            post.users_like = return_user_like_post(post.pk)
        return ctx


HomeView = Home.as_view()


class UserLogin(FormView):
    form_class = AuthenticationForm
    template_name = 'user/user_login.html'

    def form_valid(self, form):
        user_form = form.get_user()
        login(self.request, user_form)
        return super(UserLogin, self).form_valid(form)

    def get_success_url(self):
        link = self.request.POST.get('next', '')
        if link:
            return link
        else:
            return reverse('user:index')


UserLoginView = UserLogin.as_view()


def UserLogoutView(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('user:index'))


class UserRegister(FormView):
    form_class = UserCreationForm
    template_name = 'user/user_register.html'

    def form_valid(self, form):
        form.instance.is_staff = False

        user = form.save()
        user_profile = Profile.objects.create(user=user)
        user_profile.save()
        # user_profile.save()
        return super(UserRegister, self).form_valid(form)

    def get_success_url(self):
        return reverse('user:user_login')


UserRegisterView = UserRegister.as_view()


class UserEditProfile(UpdateView):
    model = User
    template_name = 'user/user_edit_profile.html'
    fields = ['first_name', 'last_name', 'email']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object != request.user:
            raise PermissionDenied
        return super(UserEditProfile, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        self.object = User.objects.get(username=self.kwargs['username'])
        return self.object

    def get_success_url(self):
        return reverse('user:index')


UserEditProfileView = UserEditProfile.as_view()


class UserChangePass(UpdateView):
    model = User
    template_name = 'user/user_change_pass.html'
    form_class = PasswordChangeForm
    # fields = ['first_name', 'last_name', 'email']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object != request.user:
            raise PermissionDenied
        return super(UserChangePass, self).dispatch(request, *args, **kwargs)

    # def form_valid(self, form):
    def get_object(self, queryset=None):
        self.object = User.objects.get(username=self.kwargs['username'])
        return self.object

    def get_success_url(self):
        return reverse('user:user_login')


UserChangePassView = UserChangePass.as_view()
