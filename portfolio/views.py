from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
def home(request):
	return render(request,"index.html")
def contact(request):
	if request.method == "POST":
		message_name = request.POST.get('name')
		message_subject = request.POST.get('subject')
		phone = request.POST.get('phone')
		message_email = request.POST['email']		 
		message = request.POST.get('message')
		sub=message_subject
		msg={'msg':message,'ph':phone,'namee':message_name}
		email=message_email
		from_user=settings.EMAIL_HOST_USER
		to=["vinsshaji2@gmail.com ", "vins.shaji3017@yahoo.com"]
		#send Mail
		send_mail(sub,msg['msg'],from_user,to,fail_silently=False)
		if message_name is not None:
			messages.info(request," Thanks! We received your mail and we will respond Soon as soon as possible")
			return redirect("home")
		else:
			messages.info(request,"please type the name")
			return redirect("home")

		

		return render(request,"index.html",{"message":message_name})
	else:

 		return render(request,"index.html",{})
	