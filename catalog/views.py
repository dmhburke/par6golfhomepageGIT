from django.shortcuts import render


#Import models here
from catalog.models import TourPlayerModel, TourModel, TourCoursesModel

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
        bonanza_winner = ""

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
    indy_url = "https://www.par6golf.com"

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
    slamma_url = ""

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

# TOUR DETAILS - Duel in the Desert
    pines_players = TourPlayerModel.objects.filter(tour_title__title=pines).order_by('tour_playernumber')
    pines_courses = TourCoursesModel.objects.filter(tour_title__title=pines)
    pines_result = TourPlayerModel.objects.filter(tour_title__title=pines, tour_position__lte=6).order_by('tour_position')
    pines_organizer = TourPlayerModel.objects.filter(tour_title__title=pines, tour_organizer="Yes")
    pines_url = ""
    try:
        pines_winner = TourPlayerModel.objects.get(tour_title__title=pines, tour_position__lte=1).tour_player
    except:
        pines_winner = ""

# === 4. TENESSEE TUSSLE (Nashville, Tennessee)===
# TOUR ADMIN - Pin Seeking in the Pines
    tussle = TourModel.objects.get(title="The Tennessee Tussle").title
    tussle_location = TourModel.objects.get(title=tussle).location
    tussle_number = TourModel.objects.get(title=tussle).tour_number
    tussle_dates = TourModel.objects.get(title=tussle).tour_dates

# TOUR DETAILS - Duel in the Desert
    tussle_players = TourPlayerModel.objects.filter(tour_title__title=tussle).order_by('tour_playernumber')
    tussle_courses = TourCoursesModel.objects.filter(tour_title__title=tussle)
    tussle_result = TourPlayerModel.objects.filter(tour_title__title=tussle, tour_position__lte=6).order_by('tour_position')
    tussle_organizer = TourPlayerModel.objects.filter(tour_title__title=tussle, tour_organizer="Yes")
    tussle_url = ""
    try:
        tussle_winner = TourPlayerModel.objects.get(tour_title__title=tussle, tour_position__lte=1).tour_player
    except:
        tussle_winner = ""

# === 3.THE COWBOY CLASSIC (Dallas, Texas)===
# TOUR ADMIN - Cowboy Classic
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

# === FOR NEW TOUR, COPY AND REPLACE CODE <<>> ===
# TOUR ADMIN - <<Tour Name>>
    # try:
        # <<tour shortname>> = TourModel.objects.get(title="<<tour FullName>>").title
    # except:
        # <<tour shortname>> = ""
    # <<tour shortname>>_location = TourModel.objects.get(title=<<tour shortname>>).location
    # <<tour shortname>>_number = TourModel.objects.get(title=<<tour shortname>>).tour_number
    # <<tour shortname>>_dates = TourModel.objects.get(title=<<tour shortname>>).tour_dates

# TOUR DETAILS - Duel in the Desert
    # <<tour shortname>>_players = TourPlayerModel.objects.filter(tour_title__title=<<tour shortname>>)
    # <<tour shortname>>_courses = TourCoursesModel.objects.filter(tour_title__title=<<tour shortname>>)
    # <<tour shortname>>_result = TourPlayerModel.objects.filter(tour_title__title=<<tour shortname>>, tour_position__lte=6).order_by('tour_position')
    # <<tour shortname>>_organizer = TourPlayerModel.objects.filter(tour_title__title=<<tour shortname>>, tour_organizer="Yes")
    # try:
    #     <<tour shortname>>_winner = TourPlayerModel.objects.get(tour_title__title=slamma, tour_position__lte=1).tour_player
    # except:
    #     <<tour shortname>>_winner = "TBD"


def XXcountdowntest1(request):

    context={}
    return render(request,'XXcountdowntest1.html', context=context)
