import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from .forms import ImageUploadForm
from .models import Image



def send_to_model(image_list):
    # =======================
    # image_list is a list of image names. eg. ['image-00000.dcm', 'image-00001.dcm', 'image-00002.dcm']
    # PREDICT HERE
    
    # =======================
    print(image_list)

def get_image_files():
    images_folder = os.path.join(os.path.join(settings.BASE_DIR,'static'), 'cta-images/dicom')
    print(images_folder)
    files = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]
    return files

def index(request):

    images = []
    result = ''
    
    if request.method == 'POST':
        data = request.POST
        
        # If this the upload image part
        if 'uploadForm' in data:
            images = request.FILES.getlist('images')
            
        # Else, this is the submission of images for prediction
        else:
            # SEND LIST OF IMAGE NAMES TO MODEL
            # send_to_model(data['submitImage'])
            images = data.getlist('submitImage')
            send_to_model(data.getlist('submitImage'))
            result = 'result.jpg'
        
    context = {
        'segment': 'index',
        'images': images,
        # 'image_files': image_files,
        'result': result
    }
            
    return render(request, 'pages/index.html', context)
