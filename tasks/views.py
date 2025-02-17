from django.shortcuts import render
from django.http import HttpResponse

# Function to handle health check
def health_check(request):
    return render(request, 'base.html', context={'title': "Tasks", 'task': 'task'})

# Single Stream View
def stream_view(request):
    stream = {  # Single stream as a dictionary
        'url': 'http://195.196.36.242/mjpg/video.mjpg', 
        'location': 'Norrbotten, Sweden'
    }
    return render(request, 'tasks/index.html', context={'stream': stream, 'title': "Live Stream", 'task': 'task'})

# Multiple Streams View
def multiple_stream_view(request):
    streams = [  # Multiple streams as a list
        {'url': 'http://195.196.36.242/mjpg/video.mjpg', 'location': 'Norrbotten, Sweden'},
        {'url': 'http://75.112.36.194/mjpg/video.mjpg', 'location': 'Florida, US'},
        {'url': 'http://213.236.250.78/mjpg/video.mjpg', 'location': 'Oslo, Norway'},
        {'url': 'http://31.12.82.136/mjpg/video.mjpg', 'location': 'Umea, Sweden'}
    ]
    return render(request, 'tasks/index.html', context={'streams': streams, 'title': "Live Streams", 'task': 'task'})

# View for Checkbox
def checkbox_view(request):
     return render(request, 'tasks/index.html', {'title': "Checkbox", 'checkbox': 'checkbox', 'task': 'task'})

# View for Text Utils
def text_utils_view(request):
    text = ""
    result = ""
    
    if request.method == "POST":
        text = request.POST.get("text", "")
        text_util = request.POST.get("text_util", "")
        
        if text_util:
            result = text_utilities(text, text_util)
    
    return render(request, "tasks/index.html", context={'title': "Text Utilities", "text": text, "result": result, "text_utils": 'text_utils', 'task': 'task'})

# Logic for Text Utils View
def text_utilities(text, text_util):
    if text_util == "punc": # Remove Punctuation
        return ''.join([char for char in text if char not in ('''!()-[]{};:'"\,<>./?@#$%^&*_~''')])
    elif text_util == "uppercase": # Upper Case Text
        return text.upper()
    elif text_util == "capitalize": # Capitalize First Letter
        return text.capitalize()
    elif text_util == "remove_spaces": # Remove Extra Spaces
        return ' '.join(text.split()) 
    elif text_util == "char_count": # Count Characters
        return f"Character Count: {len(text)}"
    elif text_util == "bold": # Bold Text
        return f"<strong>{text}</strong>"
    elif text_util == "italic": # Italic Text
        return f"<em>{text}</em>"
    elif text_util == "underline": # Underline Text
        return f"<u>{text}</u>"
    elif text_util == "reverse": # Reverse Text
        return text[::-1]
    else: return text