from django.shortcuts import render
from django.utils import timezone
from .models import Trunk_OTN
from .models import Trunk_DWDM
from .models import Trunk_SDH

# Create your views here.
def post_list(request):
	posts1 = Trunk_OTN.objects.filter(Published_date__lte=timezone.now()).order_by('Published_date')
	posts2 = Trunk_DWDM.objects.filter(Published_date__lte=timezone.now()).order_by('Published_date')
	posts3 = Trunk_SDH.objects.filter(Published_date__lte=timezone.now()).order_by('Published_date')
	return render(request, 'Trunks/post_list.html', {'posts1': posts1, 'posts2': posts2, 'posts3': posts3})