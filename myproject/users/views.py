from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":    #Agar user ne form submit kiya hai 
                                    #(update button press kiya hai), toh ye block chalega.
                                    #Nahi toh else block chalega (sirf page open hoga form ke saath).
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request,f'Dear Mr {username} Your Account Has Been Created Try To Login!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request,"users/register.html",{'form': form})
    
@login_required 
def profile(request):
    if request.method == "POST":                                    #request.post >> ye form submit krta hai yani update krta hai
        u_form = UserUpdateForm(request.POST, instance = request.user)  # ye actually old/current user apko show kriga jo ap update krna chahty hai
        p_form = ProfileUpdateForm(request.POST, 
                                request.FILES,                      # ye files sy picutre upload krta hai
                                instance = request.user.profile) # old profile ya current profile jo hai osko show kriga
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Account Has Been Updated!')
            return redirect('Profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile) 
    

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,'users/profile.html', context)
