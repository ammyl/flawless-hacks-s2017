from clarifai import rest
from clarifai.rest import ClarifaiApp

def tags(url):
    app = ClarifaiApp('n8T3KjDLHHs9FaaJLJAdNVsnrkyOQG1nhZxOiD-S', 'oi0cv4LkBZo66KPmxtW9BStyGALRiiLQrA7eD2BO')
    print(app.models.get('general-v1.3').predict_by_filename(str(url)))
