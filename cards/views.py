from django.shortcuts import render, redirect
from .models import Card
import boto3


#create aws s3 client and  for the file storage
s3 = boto3.client(
    's3',
    aws_access_key_id='access key secret after'
    aws_secret_access_key='aws_key'
    region_name='us-east-1'
)
# s3 bucket name in aws3 where everything is stored
BUCKET = 'knowledge-cards'
#upload image file to the s3 and then gives back the file url
def upload_to_s3(file):
    s3.upload_fileobj(file, BUCKET, file.name)
    return f"https://{BUCKET}.s3.amazonaws.com/{file.name}"
#home page - showing all the knowledge cards that have been added
def home(request):
    cards = Card.objects.all()
    return render(request, 'home.html', {'cards': cards})

# creates a new knowledge card
def create_card(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
#uploads to s3
        image_url = upload_to_s3(image)

        #save card to the data base
        Card.objects.create(
            title=title,
            description=description,
            image_url=image_url
        )
        return redirect('/') #then returns back to home
#returns render if the page is requested is a get
    return render(request, 'create.html')    

#searches cards for the title or description because of the get
def search(request):
    query = request.GET.get('q', '')

    if query: # search for cards matching what we need
        results = Card.objects.filter(title__icontains=query) | \
                  Card.objects.filter(description__icontains=query)
    else:
        results = Card.objects.all()
#if nothing is found just show all cards
    return render(request, 'home.html', {'cards': results})
def delete_card(request, card_id):
    card = Card.objects.get(id=card_id)
# delete cards and remove from s3  with the id
# this is taking the image file name and leaving url
    image_key = card.image_url.split('.com/')[-1]
    s3.delete_object(Bucket=BUCKET, Key=image_key)
# then we want to get rid of it from the bucket and database
    card.delete()
    return redirect('/')

#image search
def image_search(request):
    results = []

    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        filename = uploaded_file.name.lower()
#gets the uploaded file
#finds card with similar image filename
        results = Card.objects.filter(image_url__icontains=filename)

    return render(request, 'image_search.html', {'cards': results})
