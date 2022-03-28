from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView, View

from.forms import StudentRegistration
from.models import User

#
# class StudentAddView(TemplateView):
#     template_name = 'addandshow.html'
#     try:
#         def get_context_data(self, *args,**kwargs):
#             context = super().get_context_data(*args,**kwargs)
#             form = StudentRegistration()
#             stu = Student.objects.all()
#             context = {'stu':stu,'form':form}
#             return context
#     except:
#         print("Record Not to Be created")

# class Based view for add and retrieve
class UserAddView(TemplateView):
    template_name = 'addandshow.html'
    try:
        def get_context_data(self,*args, **kwargs):
            context = super().get_context_data(**kwargs)
            form = StudentRegistration()
            stud = User.objects.all()
            context = {'stud':stud,'form':form}
            return context
    except:
        print("this is error")
    finally:
        print("This code is working very well")

    def post(self,request):
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')





class UserUpdateView(View):
    def get(self,request,id):
        student = User.objects.get(pk = id)
        form = StudentRegistration(instance=student)
        return render(request,'update.html',{'form':form})

    def post(self,request,id):
        stundet = User.objects.get(pk = id)
        form = StudentRegistration(request.POST,instance=stundet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')


# class Based view for deleteing record
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk = del_id).delete()

        return super().get_redirect_url(*args,**kwargs)


