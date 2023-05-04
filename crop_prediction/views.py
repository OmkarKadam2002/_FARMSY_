from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pickle,sklearn,warnings

loaded_model=pickle.load(open('C:\\Users\\Omkar Kadam\\Desktop\\CYP\\code\\crop_production\\trained_model_final_cyp.sav','rb'))

def cyp(input_data):
    data = np.asarray(input_data)
    prediction = loaded_model.predict(data)
    return prediction[0]

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def crop(request):
    return render(request,'crop_.html')

def yield_(request):
    return render(request,'yield_.html')

def predict_(request):
    if request.method == 'POST':
        n = request.POST['input1']
        p = request.POST['input2']
        k = request.POST['input3']
        ph = request.POST['input4']
        temp = request.POST['input5']
        hum = request.POST['input6']
        rain = request.POST['input7']
        nitrogen=float(n)
        phosphorus=float(p)
        potassium=float(k)
        soilph=float(ph)
        temperature=float(temp)
        humidity=float(hum)
        rainfall=float(rain)
        pred = cyp([[nitrogen, phosphorus, potassium, temperature, humidity, soilph, rainfall]])
        pred1=pred.upper()
        imgageurl='static\mothbeans.jpg'
        description='Mothbean (Vigna aconitifolia) is a small-seeded legume crop native to India. It is a hardy and drought-resistant crop that can grow in poor soil conditions. Cultivation of mothbeans involves sowing the seeds in well-drained soil during the summer monsoon season, preferably in rows, and providing appropriate irrigation and weed control measures. The crop takes about 60-75 days to mature and can be harvested when the pods turn brown and dry.They can also tolerate saline and alkaline soils.'
        link_='https://krishijagran.com/moth-bean-cultivation/'
        data = {'prediction': pred1,'image_url':imgageurl,'desc':description, 'link_':link_}
        return render(request,'predict_.html',context=data)