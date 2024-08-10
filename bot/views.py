from django.http import HttpResponse
import sys
from django.shortcuts import render
from .models import DataState, Word
from .madeline_installer import install_madeline

def initialize_data(request):
    if not DataState.objects.exists():
        data = DataState.objects.create()
        data.save()
    return render(request, 'initialize.html')

def save_word(request, word):
    word_obj = Word.objects.create(word=word)
    word_obj.save()
    return render(request, 'save_word.html', {'word': word})


def initialize(request):
    if sys.version_info < (3, 8):
        return HttpResponse("Python 3.8 or higher is required.", status=400)

    return HttpResponse("Environment is properly set up.")


def madeline_view(request):
    try:
        install_madeline()
        return HttpResponse("MadelineProto installed successfully!")
    except Exception as e:
        return HttpResponse(f"Installation failed: {e}")

