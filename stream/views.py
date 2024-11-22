from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def health_check(request):
    return HttpResponse('''
    <center><h2>Congrats! Django is working</h2></center>
    <p> The links you can visit are: 
    <ul style ="none">
        <li><a href="/stream/view">Watch Stream!</a></li>
        <li><a href="/streams">Watch Multiple Streams!</a></li>
    </ul>''')

def stream_view(request):
    return render(request, 'stream.html')