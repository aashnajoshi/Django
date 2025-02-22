from django.shortcuts import render
from django.http import HttpResponse

# Function to handle health check
def health_check(request):
    return render(request, 'base.html', context={'title': "Tasks", 'task': True})

# Single Stream View
def stream_view(request):
    stream = {  # Single stream as a dictionary
        'url': 'http://195.196.36.242/mjpg/video.mjpg', 'location': 'Norrbotten, Sweden'}
    return render(request, 'tasks/index.html', context={'stream': stream, 'title': "Live Stream", 'task': True})

# Multiple Streams View
def multiple_stream_view(request):
    streams = [  # Multiple streams as a list
        {'url': 'http://195.196.36.242/mjpg/video.mjpg', 'location': 'Norrbotten, Sweden'},
        {'url': 'http://75.112.36.194/mjpg/video.mjpg', 'location': 'Florida, US'},
        {'url': 'http://213.236.250.78/mjpg/video.mjpg', 'location': 'Oslo, Norway'},
        {'url': 'http://31.12.82.136/mjpg/video.mjpg', 'location': 'Umea, Sweden'},]
    return render(request, 'tasks/index.html', context={'streams': streams, 'title': "Live Streams", 'task': True})

# View for Checkbox
def checkbox_view(request):
     return render(request, 'tasks/index.html', {'title': "Checkbox", 'checkbox': True, 'task': True})

# View for Text Utils
def text_utils_view(request):
    text = request.POST.get("text", "")
    text_util = request.POST.get("text_util", "")
    result, task = ("", "")
    if request.method == "POST" and text_util:
        result, task = text_utilities(text, text_util)
    return render(request, "tasks/index.html", context={'title': "Text Utilities", 'text': text, 'result': result, 'task': task, 'text_utils': True})

# Logic for Text Utils View
def text_utilities(text, text_util):
    task_names = {
        "punc": "Removed all punctuation from the text",
        "uppercase": "Converted all text to uppercase",
        "capitalize": "Capitalized the first letter of the text",
        "remove_spaces": "Removed extra spaces from the text",
        "char_count": "Counted the total number of characters",
        "bold": "Converted the text to bold",
        "italic": "Converted the text to italic",
        "underline": "Underlined the text",
        "reverse": "Reversed the order of the text"
        }
    operations = {
        "punc": lambda text: (''.join(char for char in text if char not in ('''!()-[]{};:'"\,<>./?@#$%^&*_~''')), task_names["punc"]),
        "uppercase": lambda text: (text.upper(), task_names["uppercase"]),
        "capitalize": lambda text: (text.capitalize(), task_names["capitalize"]),
        "remove_spaces": lambda text: (' '.join(text.split()), task_names["remove_spaces"]),
        "char_count": lambda text: (f"Character Count: {len(text)}", task_names["char_count"]),
        "bold": lambda text: (f"<strong>{text}</strong>", task_names["bold"]),
        "italic": lambda text: (f"<em>{text}</em>", task_names["italic"]),
        "underline": lambda text: (f"<u>{text}</u>", task_names["underline"]),
        "reverse": lambda text: (text[::-1], task_names["reverse"]),
    }
    return operations.get(text_util, lambda text: (text, ""))(text)