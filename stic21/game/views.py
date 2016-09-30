from django.shortcuts import render

# Create your views here.
def home (request):

    return render (request,"init.html")

def begin_game (request):

    request.session['count'] = 21
    return render (request,"begin_game.html")

def game (request, count):
    
    count = int(count)
    if count>3 or count<1:
        return render (request,"hak.html")
    else:
        
        guess = request.session['count'] - count 
        our_step = 4 - count
        request.session['count'] -= (our_step+count)

        if request.session['count'] == 1:
            return render (request,"loose.html", {"guess":guess, "our_step":our_step, "count":request.session['count']})
        else:
            return render (request,"game.html", {"guess":guess, "our_step":our_step, "count":request.session['count']})
  
    
    