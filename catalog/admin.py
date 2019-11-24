from django.contrib import admin

# Register your models here.
from catalog.models import TourModel, PlayerModel, TourPlayerModel, TourCoursesModel

# Define new admin class - TOURS
class TourModelAdmin(admin.ModelAdmin):
     list_display = ('title',)
     ordering = ('-tour_number',)

# Register admin class
admin.site.register(TourModel, TourModelAdmin)

# Define new admin class - TOURS
class PlayerModelAdmin(admin.ModelAdmin):
     list_display = ('name',)
     # ordering = ('-total', 'number',)

# Register admin class
admin.site.register(PlayerModel, PlayerModelAdmin)

# Define new admin class - TOURS
class TourPlayerModelAdmin(admin.ModelAdmin):
     list_display = ('tour_title', 'tour_player','tour_position')

# Register admin class
admin.site.register(TourPlayerModel, TourPlayerModelAdmin)

# Define new admin class - TOURS
class TourCoursesModelAdmin(admin.ModelAdmin):
    list_display = ('tour_title', 'tour_course')

# Register admin class
admin.site.register(TourCoursesModel, TourCoursesModelAdmin)
