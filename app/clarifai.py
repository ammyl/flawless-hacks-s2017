from clarifai import rest
from clarifai.rest import ClarifaiApp

app = ClarifaiApp('n8T3KjDLHHs9FaaJLJAdNVsnrkyOQG1nhZxOiD-S', 'oi0cv4LkBZo66KPmxtW9BStyGALRiiLQrA7eD2BO')
app.tag_urls(['https://samples.clarifai.com/metro-north.jpg'])