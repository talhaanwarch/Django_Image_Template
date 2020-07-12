from django.shortcuts import render
from .models import image_classification
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	print('here u go')
	images=image_classification.objects.all()
	url=images[len(images)-1].pic.url
	return render(request,'home.html',{'print':"every thing ok",'image':url})

def uploadImage(request):
	print('image handling')
	img=request.FILES['image']
	image=image_classification(pic=img)
	image.save()
	return HttpResponseRedirect('/')
	#return render(request,'home.html')
