import requests
from decouple import config
from faker import Faker
from django.shortcuts import render
from .models import PastLife


def index(request):
    if request.method == 'GET':
        return render(request, 'JobinthePastLife/index.html')
    else:
        person_name = request.POST.get('name')
        person_birthday = request.POST.get('birthday') + request.POST.get('birthtime')
        # '1994-12-1206:10'
        person = PastLife.objects.filter(name=person_name).filter(birthday=person_birthday).first()
        # first()는 queryset에 element가 있으면 첫번째 항목을, 없으면 None을 반환한다.
        if not person:
            person = PastLife()
            person.name = person_name
            date = request.POST.get('birthday')
            time = request.POST.get('birthtime')
            person.birthday = date + time
            seed = sum(map(int, date.split('-') + time.split(':')))
            fake = Faker('ko_KR')
            fake.seed(seed)
            person.job = fake.job()
            person.save()
        # 1. url 설정
        api_key = config('GIPHY_API_KEY')
        url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q=%EC%8B%A0%EB%82%A8&lang=ko'
        # 2. 요청 보내기
        response = requests.get(url).json()
        try:
            image_url = response['data'][0].get('images').get('original').get('url')
        except:
            image_url = None
        context = {
            'person': person,
            'image_url': image_url
        }
        return render(request, 'JobinthePastLife/result.html', context)