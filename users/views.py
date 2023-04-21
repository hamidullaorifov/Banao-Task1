from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.urls import reverse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# class SignUpView(CreateView):
#     form_class = UserRegisterForm
#     success_url = reverse_lazy('login')
#     template_name = 'users/signup.html'
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse('dashboard'))
        else:
            return render(request,'users/signup.html',{'form':form})
        
    return render(request,'users/signup.html')

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
            ...
        else:
            context = {'error':'Invalid username or password.'}
    return render(request, 'users/login.html', context)
        

@login_required(login_url='/login/')
def dashboard_view(request):
    return render(request,'users/dashboard.html')
