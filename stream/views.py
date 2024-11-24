from django.shortcuts import render
from django.http import HttpResponse

# Function to handle health check
def health_check(request):
    return HttpResponse('''
    <center><h2>Congrats! Django is working</h2></center>
    <p> The links you can visit are: 
    <ul style ="none">
        <li><a href="/stream/view">Watch Stream!</a></li>
        <li><a href="/stream/multiple">Watch Multiple Streams!</a></li>
    </ul>''')

# View for Single Stream
def stream_view(request):
    return render(request, 'stream.html', {'streams': [{'url': 'http://195.196.36.242/mjpg/video.mjpg', 'location':'Norrbotten, Sweden'}]})

# View for Multiple Streams
def multiple_stream_view(request):
    streams = [
        {'url':'http://195.196.36.242/mjpg/video.mjpg', 'location':'Norrbotten, Sweden'},
        {'url':'http://75.112.36.194/mjpg/video.mjpg', 'location':'Florida, US'},
        {'url':'http://213.236.250.78/mjpg/video.mjpg', 'location':'Oslo, Norway'},
        {'url':'http://31.12.82.136/mjpg/video.mjpg', 'location':'Umea, Sweden'},]
    return render(request, 'stream.html', {'streams': streams})