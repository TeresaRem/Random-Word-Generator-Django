from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def random_word(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
    request.session['attempt'] += 1
    request.session['random_word'] = get_random_string(length=14)
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')
    
  
  




