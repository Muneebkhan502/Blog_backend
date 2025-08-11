from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import post
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView



# Create your views here.
def home(request):
    context = {
        'posts' : post.objects.all()
    }
    return render(request,'blog/home.html', context)



class PostListView(ListView): #ye class based view hai is ma hum varaible ka use karty hai
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'  #Iska matlab ye hai ke jo object fetch hua hai, wo template me kis naam se aayega.
    ordering =['-date_posted']
    paginate_by = 4


class UserPostListView(ListView): 
    model = post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2
    

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(auther = user).order_by('-date_posted')
    
                                                                         
                                    #    <app_name>/<model_name>_detail.html
                            
class PostDetailView(DetailView): 
    model = post

    
class PostCreateView(LoginRequiredMixin, CreateView): 
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.auther = self.request.user # hmra auther wo hai jo currently login hai
        return super().form_valid(form) # parents k property use kr raha hai
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # UserPassesTestMixin >> to ensure                                                                      #upon only specific condition a user can                                                                         #access to some page like user can only                                                                        #update and delete his own post
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.auther = self.request.user # hmra auther wo hai jo currently login hai
        return super().form_valid(form) # parents k property use kr raha hai

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False

    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'title':about})