from django.shortcuts import render, redirect
from .models import Card
import boto3



s3 = boto3.client(
    's3',
    aws_access_key_id='access key secret after'
    aws_secret_access_key='aws_key'
    region_name='us-east-1'
)

BUCKET = 'knowledge-cards'

def upload_to_s3(file):
    s3.upload_fileobj(file, BUCKET, file.name)
    return f"https://{BUCKET}.s3.amazonaws.com/{file.name}"

def home(request):
    cards = Card.objects.all()
    return render(request, 'home.html', {'cards': cards})


def create_card(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']

        image_url = upload_to_s3(image)

        
        Card.objects.create(
            title=title,
            description=description,
            image_url=image_url
        )
        return redirect('/')

    return render(request, 'create.html')    


def search(request):
    query = request.GET.get('q', '')

    if query:
        results = Card.objects.filter(title__icontains=query) | \
                  Card.objects.filter(description__icontains=query)
    else:
        results = Card.objects.all()

    return render(request, 'home.html', {'cards': results})
def delete_card(request, card_id):
    card = Card.objects.get(id=card_id)

    image_key = card.image_url.split('.com/')[-1]
    s3.delete_object(Bucket=BUCKET, Key=image_key)

    card.delete()
    return redirect('/')


def image_search(request):
    results = []

    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        filename = uploaded_file.name.lower()

        results = Card.objects.filter(image_url__icontains=filename)

    return render(request, 'image_search.html', {'cards': results})
