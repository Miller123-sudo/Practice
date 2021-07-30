from webpages.models import Slider, Team
from django.shortcuts import render
from youtubers.models import Youtubers

# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    Teams = Team.objects.all()
    featured_youtubers = Youtubers.objects.order_by(
        '-created_date').filter(is_featured=True)
    last_onboard_youtubers = Youtubers.objects.all().order_by(
        '-created_date')
    data = {
        'sliders': sliders,
        'Teams': Teams,
        'featured_youtubers': featured_youtubers,
        'last_onboard_youtubers': last_onboard_youtubers
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')
