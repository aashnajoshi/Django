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

# View for single stream
def stream_view(request):
    return render(request, 'stream.html', {
        'streams': [{'url': 'http://195.196.36.242/mjpg/video.mjpg', 'location': 'Luleå, Norrbotten, Sweden'}]})

# New view for multiple streams
def multiple_stream_view(request):

    streams = [
        {'url': 'http://195.196.36.242/mjpg/video.mjpg', 'location': 'Luleå, Norrbotten, Sweden'},
        {'url': 'http://75.112.36.194/mjpg/video.mjpg', 'location': 'Sanford, Florida, US'},
        {'url': 'http://213.124.36.2/mjpg/video.mjpg', 'location': 'Voorhout, Netherlands, US'},
        {'url': 'http://216.14.224.50/mjpg/video.mjpg', 'location': 'Wye, Montana, US'},]
    return render(request, 'stream.html', {'streams': streams})