from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, mixins, get_user_model
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .filters import ExamFilter

# Create your views here.

class home(View):
    def get(self, request: HttpRequest):
        return render(request, template_name='home.html')


# class loginPage(View):
#     def get(self,request: HttpRequest):
#         form = UserCreationForm()
#         context = {'form':form}
#         return render(request, template_name='loginPage.html')


class registerPage(CreateView):
    model = get_user_model()
    form_class = registerForm
    template_name = 'registerPage.html'
    success_url = reverse_lazy("thinkify:homeNext")

    # context_object_name = 'registerForm'

    def form_valid(self, form):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        print(username,password)
        user = form.save(commit=True)
        # user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        if user is None:
            self.form_invalid(form)
        login(request=self.request, user=user)
        return redirect(to=self.success_url)


# class registerPage(View):
#     def get(self,request: HttpRequest):
#         form = registerForm()
#         context = {'registerForm': form}
#         return render(request, template_name='registerPage.html',context=context)
#
#     def post(self,request):
#         form = registerForm(request.POST)
#         if not form.is_valid:
#             context = {'form':form}
#             return render(request, template_name='registerPage.html',context=context)
#
#         else:
#             user = User(username = form.username,password = form.password)
#             user.save()
#             login(request=request,user = user)
#             return redirect(to=reverse_lazy("thinkify:homeNext"))

class homeNext(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='homeNext.html')


# class exams(View):
#     def get(self, request: HttpRequest):
#         return render(request, template_name='exams.html')


# class scholarship(View):
#     def get(self, request: HttpRequest):
#         return render(request, template_name='scholarship.html')


class LoginPage(LoginView):
    template_name = 'loginPage.html'
    authentication_form = UserLogin
    success_url = reverse_lazy("thinkify:homeNext")
    redirect_authenticated_user = True
    # username = self.request.POST.get("username")
    # password = self.request.POST.get("password")
    # print(username, password)


    def get_default_redirect_url(self):

        return self.success_url

    # def form_valid(self, form):
    #     user = form.get_user()
    #     #user = authenticate(request=self.request,username=form.cleaned_data['username'], password= form.cleaned_data['password'])
    #     print(user)
    #     if user is None:
    #         messages.error(self.request,"Failure improper pass")
    #         self.form_invalid(form)
    #     login(self.request,user)
    #     self.success_url = reverse_lazy("thinkify:homeNext")
    #     print(self.success_url)
    #     return redirect(to=self.success_url)



class Logout(LogoutView):
    next_page = reverse_lazy("thinkify:Home")



# def exams(request):
#     examval = exams.all()
#     myFilter = ExamFilter(request.GET, queryset=)
#     context = {'myFilter':myFilter}
#     return render(request,'exams.html',context)


# def loginPage(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         print(username,password)
#         user = authenticate(username='username',password='password')
#         if user is None:
#             context = {"error":"Invalid username or password"}
#             return render(request,"loginPage.html")
#         login(request,user)
#         return(redirect(to="homeNext"))


def exams(request):
    domain = request.GET.get('domain')
    exams = Exams.objects.all()
    if domain:
        exams = exams.filter(domain__icontains=domain)
    context = {
        'form': DomainFilter(),'exams': exams
    }
    return render(request,'exams.html',context)

def scholarship(request):
    Scholarship_exam = request.GET.get('Scholarship_exam')
    scholarships = Scholarship.objects.all()
    if Scholarship_exam:
        scholarships = scholarships.filter(Scholarship_exam__icontains=Scholarship_exam)
    context = {
        'form': ScholarFilter(), 'scholarships': scholarships
    }
    return render(request, 'scholarship.html', context)

class resources(View):
    def get(self, request: HttpRequest):
        return render(request, template_name='resources.html')

def persona(request):
    return render(request, 'persona.html')


# def listing(request):
#     if request.method=='POST':
#         genderr=request.POST.get('Exams')
#
#     exam_list = Exams.objects.all()
#     domain =
#     if domain:
#         exams = exam_list.filter(domain__icontains=domain)
#     context = {
#         'form': DomainFilter(), 'exam_list': exam_list
#     }
#     return render(request, 'listing.html', context)

# def listing(request):
#     if request.method=='GET':
#         return render(request,template_name='perspage.html')
#     elif request.method=='POST':
#         domain = Configure(request.POST)
#         domain.full_clean()
#         context={}
#         # exams.objects.all().filter(domain=domain.cleaned_data['domain'])
#         # domain.is_valid()
#         # domain.cleaned_data
#         exam_list = Exams.objects.all()
#         if domain.is_valid():
#             dominee=request.POST.get('domain_type')
#             if dominee:
#                 exam_list = exam_list.filter(domain__icontains=domain)
#             context = {
#                 'form': Configure, 'exam_list': exam_list
#             }
#         filter(request,context)
#
#
#
# def perspage(request):
#
#     if request.method=='GET':
#         return render(request,template_name='perspage.html')
#     elif request.method=='POST':
#         domain = Configure(request.POST)
#         domain.full_clean()
#         context={}
#         # exams.objects.all().filter(domain=domain.cleaned_data['domain'])
#         # domain.is_valid()
#         # domain.cleaned_data
#         exam_list = Exams.objects.all()
#         if domain.is_valid():
#             dominee=request.POST.get('domain_type')
#             if dominee:
#                 exam_list = exam_list.filter(domain__icontains=domain)
#             context = {
#                 'form': Configure, 'exam_list': exam_list
#             }
#         filter(request,context)
#
#
#
# def filter(request,context):
#     return render(request, 'filter.html', context)

# from .forms import Configure  # Import your form class here

# def perspage(request):
#     form = Configure(request.POST or None)  # Initialize the form here
#
#     if request.method == 'POST':
#         if form.is_valid():
#             dominee = form.cleaned_data['domain_type']
#             exam_list = Exams.objects.all()
#             context = {}
#             if dominee:
#                 exam_list = exam_list.filter(domain__icontains=dominee)
#
#             context = {'form': form, 'exam_list': exam_list}
#             return render(request,'filter.html',context)
#
#     return render(request, template_name='perspage.html', context={'form': form})
#
# def filter(request, context):
#     return render(request, 'filter.html', context)
class Personalisation(View,mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, 'perspage.html', {'form': Configure()})


class Filter(View,mixins.LoginRequiredMixin):
    def get(self,request:  HttpRequest):
        qs=persdomain.objects.all().filter(user=request.user)
        if qs:
            dom_obj=qs.get()
            domain_type=dom_obj.domain_name
            exam_list = Exams.objects.all()

            if domain_type:
                exam_list = exam_list.filter(domain__contains=domain_type)
                pers_obj = persdomain(user=request.user, domain_name=domain_type)
                pers_obj.save()

            context = {
                'exam_list': exam_list
            }
            return render(request, 'filter.html', context)
        else:
            return redirect(to=reverse_lazy('thinkify:perspage'),request=request)

    def post(self, request: HttpRequest):
        # form = Configure(request.POST) qs = persdomain.objects.all.filter(user=req.user)  if qs: dom=qs.get domname=dom.domain_name else: redirect(to=reverse_lazy('thinkify:perspage',request)
        domain_type = request.POST['Exams']
        print(domain_type)
        # if form.is_valid():
        #     domain_type = form.cleaned_data['domain_type']
        exam_list = Exams.objects.all()

        if domain_type:
            exam_list = exam_list.filter(domain__contains=domain_type)
            pers_obj=persdomain(user=request.user,domain_name=domain_type)
            pers_obj.save()


        context = {
            'exam_list': exam_list
        }
        return render(request, 'filter.html', context)

def newhome(request):
    return render(request, 'newhome.html')

#
#
# def process_checkbox(request):
#     if request.method == 'POST':
#         # Assuming you have a form named 'GeeksForm'
#         form = GeeksForm(request.POST)
#
#         if form.is_valid():
#             # 'geeks_field' is the name of the field in your form
#             selected_values = form.cleaned_data.get('geeks_field')
#
#             # Now 'selected_values' contains the selected checkboxes' values
#             # You can process the selected values here
#
#             context = {'selected_values': selected_values}
#             return render(request, 'result.html', context)
#
#     else:
#         form = GeeksForm()
#
#     context = {'form': form}
#     return render(request, 'checkbox_form.html', context)

#
# def per_content(request):
#     return render(request, 'per_content.html')

#def perspage(request): return render(request, 'perspage.html')
# redirect(to=reverse_lazy('thinkify:perspage',request)


# class Filter(View):
#     def post(self,request):
#         # form = Configure(request.POST) qs = persdomain.objects.all.filter(user=req.user)  if qs: dom=qs.get domname=dom.domain_name else: redirect(to=reverse_lazy('thinkify:perspage',request)
#         domain_type = request.POST['Exams']
#         print(domain_type)
#         # if form.is_valid():
#         #     domain_type = form.cleaned_data['domain_type']
#         exam_list = Exams.objects.all()

        # if domain_type:
        #     exam_list = exam_list.filter(domain__contains=domain_type)
        #     pers_obj=persdomain(user=request.user,domain_name=domain_type)
        #     pers_obj.save()


        # context = {
        #     'exam_list': exam_list
        # }
        # return render(request, 'filter.html', context)









