from django.shortcuts import render

from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserCreateForm
from django.shortcuts import  redirect

# Create your views here.


class signup(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        if self.request.method=="POST":
            user = form.save()
            username = form.cleaned_data.get('username')
            UserProfile.objects.create(user=user,username=username)
            return redirect('home')






def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            # Added username after video because of error returning customer name if not added
            Customer.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)