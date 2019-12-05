from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Min
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


#Import models here
from catalog.models import TourPlayerModel, PlayerModel, TourModel, TourCoursesModel, PlayerRegisterModel
from catalog.forms import PlayerRegisterForm

# Create your views here.
def landingpage(request):
    """Landing page view containing all tours and countdown clock"""

# === 9. BAYOU BONANZA (New Orleans, Louisiana)===
# TOUR ADMIN - Bayou Bonanza
    bonanza = TourModel.objects.get(title="The Bayou Bonanza").title
    bonanza_location = TourModel.objects.get(title=bonanza).location
    bonanza_number = TourModel.objects.get(title=bonanza).tour_number
    bonanza_dates = TourModel.objects.get(title=bonanza).tour_dates

# TOUR DETAILS - Bayou Bonanza
    bonanza_players = TourPlayerModel.objects.filter(tour_title__title=bonanza).order_by('tour_playernumber')
    bonanza_courses = TourCoursesModel.objects.filter(tour_title__title=bonanza)
    bonanza_result = TourPlayerModel.objects.filter(tour_title__title=bonanza, tour_position__lte=6).order_by('tour_position')
    bonanza_organizer = TourPlayerModel.objects.filter(tour_title__title=bonanza, tour_organizer="Yes")
    bonanza_url = "https://bonanza.par6golf.com"

    try:
        bonanza_winner = TourPlayerModel.objects.get(tour_title__title=bonanza, tour_position__lte=1).tour_player
    except:
        bonanza_winner = "TBD"

# === 8. DUEL IN THE DESERT (Scottsdale, Arizona)===
# TOUR ADMIN - Duel in the Desert
    duel = TourModel.objects.get(title="The Duel in the Desert").title
    duel_location = TourModel.objects.get(title=duel).location
    duel_number = TourModel.objects.get(title=duel).tour_number
    duel_dates = TourModel.objects.get(title=duel).tour_dates

# TOUR DETAILS - Duel in the Desert
    duel_players = TourPlayerModel.objects.filter(tour_title__title=duel).order_by('tour_playernumber')
    duel_courses = TourCoursesModel.objects.filter(tour_title__title=duel)
    duel_result = TourPlayerModel.objects.filter(tour_title__title=duel, tour_position__lte=6).order_by('tour_position')
    duel_organizer = TourPlayerModel.objects.filter(tour_title__title=duel, tour_organizer="Yes")
    duel_url = "https://duel.par6golf.com"

    try:
        duel_winner = TourPlayerModel.objects.get(tour_title__title=duel, tour_position__lte=1).tour_player
    except:
        duel_winner = ""

# === 7. INDY 1200 (Indianapolis, Indiana)===
# TOUR ADMIN - indy
    try:
        indy = TourModel.objects.get(title="The Indy1200").title
    except:
        indy = ""
    indy_location = TourModel.objects.get(title=indy).location
    indy_number = TourModel.objects.get(title=indy).tour_number
    indy_dates = TourModel.objects.get(title=indy).tour_dates

# TOUR DETAILS - indy
    indy_players = TourPlayerModel.objects.filter(tour_title__title=indy).order_by('tour_playernumber')
    indy_courses = TourCoursesModel.objects.filter(tour_title__title=indy)
    indy_result = TourPlayerModel.objects.filter(tour_title__title=indy, tour_position__lte=6).order_by('tour_position')
    indy_organizer = TourPlayerModel.objects.filter(tour_title__title=indy, tour_organizer="Yes")
    try:
        indy_winner = TourPlayerModel.objects.get(tour_title__title=indy, tour_position__lte=1).tour_player
    except:
        indy_winner = ""
    indy_url = "https://golfapp1dev.herokuapp.com/login/leaderboard/"

# === 6. SAVANNAH SLAMMA (Savannah, Georgia)===
# TOUR ADMIN - Savannah Slamma
    slamma = TourModel.objects.get(title="The Savannah Slamma").title
    slamma_location = TourModel.objects.get(title=slamma).location
    slamma_number = TourModel.objects.get(title=slamma).tour_number
    slamma_dates = TourModel.objects.get(title=slamma).tour_dates

# TOUR DETAILS - Savannah Slamma
    slamma_players = TourPlayerModel.objects.filter(tour_title__title=slamma).order_by('tour_playernumber')
    slamma_courses = TourCoursesModel.objects.filter(tour_title__title=slamma)
    slamma_result = TourPlayerModel.objects.filter(tour_title__title=slamma, tour_position__lte=6).order_by('tour_position')
    slamma_organizer = TourPlayerModel.objects.filter(tour_title__title=slamma, tour_organizer="Yes")
    slamma_url = "https://docs.google.com/spreadsheets/d/1t6PDOkvBo_hQ0U5VS9YaG194k-dvOn-vG2DqIKuEeAs/edit#gid=1448364988"

    try:
        slamma_winner = TourPlayerModel.objects.get(tour_title__title=slamma, tour_position__lte=1).tour_player
    except:
        slamma_winner = ""

# === 5. PIN SEEKING IN THE PINES (Pinehurst, North Carolina)===
# TOUR ADMIN - Pin Seeking in the Pines
    pines = TourModel.objects.get(title="Pin Seeking in the Pines").title
    pines_location = TourModel.objects.get(title=pines).location
    pines_number = TourModel.objects.get(title=pines).tour_number
    pines_dates = TourModel.objects.get(title=pines).tour_dates

# TOUR DETAILS - Pines
    pines_players = TourPlayerModel.objects.filter(tour_title__title=pines).order_by('tour_playernumber')
    pines_courses = TourCoursesModel.objects.filter(tour_title__title=pines)
    pines_result = TourPlayerModel.objects.filter(tour_title__title=pines, tour_position__lte=6).order_by('tour_position')
    pines_organizer = TourPlayerModel.objects.filter(tour_title__title=pines, tour_organizer="Yes")
    pines_url = "https://docs.google.com/spreadsheets/d/1H_WUn0V2Tqt6E8V_aKDgge27-Xxxo3itb_UL5kz5nys/edit#gid=1448364988"
    try:
        pines_winner = TourPlayerModel.objects.get(tour_title__title=pines, tour_position__lte=1).tour_player
    except:
        pines_winner = ""

# === 4. TENESSEE TUSSLE (Nashville, Tennessee)===
# TOUR ADMIN - Tussle
    tussle = TourModel.objects.get(title="The Tennessee Tussle").title
    tussle_location = TourModel.objects.get(title=tussle).location
    tussle_number = TourModel.objects.get(title=tussle).tour_number
    tussle_dates = TourModel.objects.get(title=tussle).tour_dates

# TOUR DETAILS - Tussle
    tussle_players = TourPlayerModel.objects.filter(tour_title__title=tussle).order_by('tour_playernumber')
    tussle_courses = TourCoursesModel.objects.filter(tour_title__title=tussle)
    tussle_result = TourPlayerModel.objects.filter(tour_title__title=tussle, tour_position__lte=6).order_by('tour_position')
    tussle_organizer = TourPlayerModel.objects.filter(tour_title__title=tussle, tour_organizer="Yes")
    tussle_url = "https://docs.google.com/spreadsheets/d/1SwDdvu7VxB0OE8-W8C7WmwpUqSmNhAegDVXRgb4jlsE/edit#gid=1448364988"
    try:
        tussle_winner = TourPlayerModel.objects.get(tour_title__title=tussle, tour_position__lte=1).tour_player
    except:
        tussle_winner = ""

# === 3.THE DALLAS DUST UP (Dallas, Texas)===
# TOUR ADMIN - Dust up
    dallas = TourModel.objects.get(title="The Dallas Dust up").title
    dallas_location = TourModel.objects.get(title=dallas).location
    dallas_number = TourModel.objects.get(title=dallas).tour_number
    dallas_dates = TourModel.objects.get(title=dallas).tour_dates

# TOUR DETAILS - Duel in the Desert
    dallas_players = TourPlayerModel.objects.filter(tour_title__title=dallas).order_by('tour_playernumber')
    dallas_courses = TourCoursesModel.objects.filter(tour_title__title=dallas)
    dallas_result = TourPlayerModel.objects.filter(tour_title__title=dallas, tour_position__lte=6).order_by('tour_position')
    dallas_organizer = TourPlayerModel.objects.filter(tour_title__title=dallas, tour_organizer="Yes")
    dallas_url = ""
    try:
        dallas_winner = TourPlayerModel.objects.get(tour_title__title=dallas, tour_position__lte=1).tour_player
    except:
        dallas_winner = ""

# === 2. SNAKEPIT CHALLENGE  (Charleston, South Carolina)===
# TOUR ADMIN - snakepit
    snakepit = TourModel.objects.get(title="The Snakepit Challenge").title
    snakepit_location = TourModel.objects.get(title=snakepit).location
    snakepit_number = TourModel.objects.get(title=snakepit).tour_number
    snakepit_dates = TourModel.objects.get(title=snakepit).tour_dates

# TOUR DETAILS - Duel in the Desert
    snakepit_players = TourPlayerModel.objects.filter(tour_title__title=snakepit).order_by('tour_playernumber')
    snakepit_courses = TourCoursesModel.objects.filter(tour_title__title=snakepit)
    snakepit_result = TourPlayerModel.objects.filter(tour_title__title=snakepit, tour_position__lte=6).order_by('tour_position')
    snakepit_organizer = TourPlayerModel.objects.filter(tour_title__title=snakepit, tour_organizer="Yes")
    snakepit_url = ""
    try:
        snakepit_winner = TourPlayerModel.objects.get(tour_title__title=snakepit, tour_position__lte=1).tour_player
    except:
        snakepit_winner = ""
# === 1. TOUR OF ORIGIN (Tampa, Florida) ===
    # TOUR ADMIN - Origin
    origin = TourModel.objects.get(title="The Tour of Origin").title
    origin_location = TourModel.objects.get(title=origin).location
    origin_number = TourModel.objects.get(title=origin).tour_number
    origin_dates = TourModel.objects.get(title=origin).tour_dates

    # TOUR DETAILS - Origin
    origin_players = TourPlayerModel.objects.filter(tour_title__title=origin).order_by('tour_playernumber')
    origin_courses = TourCoursesModel.objects.filter(tour_title__title=origin)
    origin_result = TourPlayerModel.objects.filter(tour_title__title=origin, tour_position__lte=6).order_by('tour_position')
    origin_organizer = TourPlayerModel.objects.filter(tour_title__title=origin, tour_organizer="Yes")
    origin_url = ""
    try:
        origin_winner = TourPlayerModel.objects.get(tour_title__title=origin, tour_position__lte=1).tour_player
    except:
        origin_winner = ""


    context = {
    # Bayou Bonanza
    'bonanza': bonanza,
    'bonanza_location': bonanza_location,
    'bonanza_number': bonanza_number,
    'bonanza_dates': bonanza_dates,
    'bonanza_winner': bonanza_winner,
    'bonanza_players': bonanza_players,
    'bonanza_courses': bonanza_courses,
    'bonanza_result': bonanza_result,
    'bonanza_organizer': bonanza_organizer,
    'bonanza_url': bonanza_url,
    # Duel in the Desert
    'duel': duel,
    'duel_location': duel_location,
    'duel_number': duel_number,
    'duel_dates': duel_dates,
    'duel_winner': duel_winner,
    'duel_players': duel_players,
    'duel_courses': duel_courses,
    'duel_result': duel_result,
    'duel_organizer': duel_organizer,
    'duel_url': duel_url,
    # Indy1200
    'indy': indy,
    'indy_location': indy_location,
    'indy_number': indy_number,
    'indy_dates': indy_dates,
    'indy_winner': indy_winner,
    'indy_players': indy_players,
    'indy_courses': indy_courses,
    'indy_result': indy_result,
    'indy_organizer': indy_organizer,
    'indy_url': indy_url,
    #Savannah Slamma
    'slamma': slamma,
    'slamma_location': slamma_location,
    'slamma_number': slamma_number,
    'slamma_dates': slamma_dates,
    'slamma_winner': slamma_winner,
    'slamma_players': slamma_players,
    'slamma_courses': slamma_courses,
    'slamma_result': slamma_result,
    'slamma_organizer': slamma_organizer,
    'slamma_url': slamma_url,
    # Pin seeking in the Pines
    'pines': pines,
    'pines_location': pines_location,
    'pines_number': pines_number,
    'pines_dates': pines_dates,
    'pines_winner': pines_winner,
    'pines_players': pines_players,
    'pines_courses': pines_courses,
    'pines_result': pines_result,
    'pines_organizer': pines_organizer,
    'pines_url': pines_url,
    # Tennessee Tussle
    'tussle': tussle,
    'tussle_location': tussle_location,
    'tussle_number': tussle_number,
    'tussle_dates': tussle_dates,
    'tussle_winner': tussle_winner,
    'tussle_players': tussle_players,
    'tussle_courses': tussle_courses,
    'tussle_result': tussle_result,
    'tussle_organizer': tussle_organizer,
    'tussle_url': tussle_url,
    # The Cowboy Classic
    'dallas': dallas,
    'dallas_location': dallas_location,
    'dallas_number': dallas_number,
    'dallas_dates': dallas_dates,
    'dallas_winner': dallas_winner,
    'dallas_players': dallas_players,
    'dallas_courses': dallas_courses,
    'dallas_result': dallas_result,
    'dallas_organizer': dallas_organizer,
    'dallas_url': dallas_url,
    # The Snakepit Challenge
    'snakepit': snakepit,
    'snakepit_location': snakepit_location,
    'snakepit_number': snakepit_number,
    'snakepit_dates': snakepit_dates,
    'snakepit_winner': snakepit_winner,
    'snakepit_players': snakepit_players,
    'snakepit_courses': snakepit_courses,
    'snakepit_result': snakepit_result,
    'snakepit_organizer': snakepit_organizer,
    'snakepit_url': snakepit_url,
    # The Tour Of Origin
    'origin': origin,
    'origin_location': origin_location,
    'origin_number': origin_number,
    'origin_dates': origin_dates,
    'origin_winner': origin_winner,
    'origin_players': origin_players,
    'origin_courses': origin_courses,
    'origin_result': origin_result,
    'origin_organizer': origin_organizer,
    'origin_url': origin_url,
    }

    return render(request,'landingpage.html',context=context)

def players(request):

    active_players = PlayerModel.objects.all().order_by('name')
    mgmt_committee = PlayerModel.objects.filter(mgmt_committee="YES").order_by('-tour_number', 'high_finish', 'name')
    touring_party = PlayerModel.objects.filter(mgmt_committee="NO").order_by('-tour_number', 'high_finish', 'name')

    # tour_number = TourPlayerModel.objects.filter(tour_player__name="Daniel Burke").count()
    # high_finish = list(TourPlayerModel.objects.filter(tour_player__name="Daniel Burke").aggregate(Min('tour_position')).values())[0]

    context = {
        'active_players': active_players,
        'mgmt_committee': mgmt_committee,
        'touring_party': touring_party,
        # 'tour_number': tour_number,
        # 'high_finish': high_finish,
    }

    return render(request, 'players.html', context=context)


def register(request):
    """View that controls how players register for next tour"""

    #Email notification details (triggered on form submit)
    subject = 'Bayou Bonanza | New player registration'
    message1 = ' has registered as '
    message2 = '. To see page, click www.par6golf.com/registersuccess. To go to admin, click www.par6golf.com/admin.'
    email_from = settings.EMAIL_HOST_USER
    email_to = ['dmhburke@gmail.com',]

    # Form details to record registration
    if request.method == 'POST':
        form = PlayerRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            name = post.player_name.name
            status = post.tour_status
            post.save()
            send_mail(subject, name + message1 + status + message2, email_from, email_to) #, fail_silently=False
            return redirect('registersuccess') #or whatever the url
    else:
        form = PlayerRegisterForm()

    #calculation of remaining slots left for next tour
    next_tour_name = "The Bayou Bonanza"
    total_tour_spots = 12

    locked_in_spots = TourPlayerModel.objects.filter(tour_title__title=next_tour_name).count()
    remaining_spots = total_tour_spots - locked_in_spots
    context = {
        'form': form,
        'remaining_spots': remaining_spots,
    }

    return render(request, 'register.html', context=context)

def registersuccess(request):
    """"""
    latest_entry = PlayerRegisterModel.objects.last()
    latest_entry_name = latest_entry.player_name
    latest_entry_response_raw = latest_entry.tour_status

    def convert_response(entry):
        switch_options = {
            "YES": "Lock me in",
            "MAYBE": "Keep me informed",
            "NO": "Out"
        }
        return switch_options.get(entry, "Invalid response")

    latest_entry_response = convert_response(latest_entry_response_raw)
    latest_entry_image = PlayerModel.objects.get(name=latest_entry_name).image

    def get_emoji(value):
        switch_options = {
        "YES": "https://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-12/256/thumbs-up.png",
        "NO": "https://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-12/256/thumbs-down.png",
        "MAYBE": "https://i.pinimg.com/originals/d6/06/3c/d6063c4b824cae58b5de19cf1ccf315f.png"
        }

        return switch_options.get(value, "")

    response_emoji = get_emoji(latest_entry_response_raw)

    context = {
        'latest_entry_name': latest_entry_name,
        'latest_entry_response': latest_entry_response,
        'latest_entry_image': latest_entry_image,
        'response_emoji': response_emoji,
        # 'test': test,
    }

    return render(request, 'registersuccess.html', context=context)



def XXcountdowntest1(request):

    context={}
    return render(request,'XXcountdowntest1.html', context=context)
