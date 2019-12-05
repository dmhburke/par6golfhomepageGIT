from django.contrib import admin

# Register your models here.
from catalog.models import TourModel, PlayerModel, TourPlayerModel, TourCoursesModel, PlayerRegisterModel, PlayerStatsModel

# Define new admin class - TOURS
class TourModelAdmin(admin.ModelAdmin):
     list_display = ('title',)
     ordering = ('-tour_number',)

# Register admin class
admin.site.register(TourModel, TourModelAdmin)

# Define new admin class - TOURS
class PlayerModelAdmin(admin.ModelAdmin):
     list_display = ('name','tour_number', 'high_finish')
     ordering = ('-tour_number', 'high_finish', 'name',)

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

# Define new admin class - PLAYER REGISTER
class PlayerRegisterModelAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'tour_status', 'comments')

# Register admin class
admin.site.register(PlayerRegisterModel, PlayerRegisterModelAdmin)

# Define new admin class - PLAYER STATS
class PlayerStatsModelAdmin(admin.ModelAdmin):
    list_display = ('player_name',)

# Register admin class
admin.site.register(PlayerStatsModel, PlayerStatsModelAdmin)
