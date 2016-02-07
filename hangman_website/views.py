from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .utils import Hangman


class HangmanView(generic.View):

    # Get method rendering either the welcome page or the game page
    @staticmethod
    def get(request, *args, **kwargs):
        if 'hangman_session' in request.session:
            response = render(request, 'hangman_website/game.html', request.session['hangman_session'])
            return response
        else:
            request.session.flush()
            return render(request, 'hangman_website/index.html', {})

    # This is used to modify the session, and redirect to get to avoid form re-submission
    @staticmethod
    def post(request, *args, **kwargs):
        if 'hangman_session' in request.session:
            value = request.session['hangman_session']
            if request.POST.get('letter', False):
                letter = request.POST['letter'].lower()
                value = Hangman.hangman_test(value, letter)
                request.session['hangman_session'] = value
                return HttpResponseRedirect(reverse('hangman_website:index'))
            else:
                value['error'] = 'You reached this page without a letter'
                return HttpResponseRedirect(reverse('hangman_website:index'))
        else:
            value = Hangman().create_game()
            request.session['hangman_session'] = value
            return HttpResponseRedirect(reverse('hangman_website:index'))


# Added a reset function to play again
def reset_game(request, *args, **kwargs):
    if 'hangman_session' in request.session:
        request.session.flush()
        value = Hangman().create_game()
        request.session['hangman_session'] = value
        return HttpResponseRedirect(reverse('hangman_website:index'))