from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from .models import Post, Tour, TourImage, TourForm
from django import forms


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    search_fields = ('title', 'content')

class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1

class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageInline]
    list_display = ('title', 'short_description', 'created_at')  # Usunięto meeting_place i tour_description
    search_fields = ('title',)
    fields = ('title', 'short_description', 'description', 'route', 'price', 'duration', 'starting_point', 'image', 'organizational_details')  # tour_description zamienione na description
    form = TourForm
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()},
    }

class TourAdminForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'  # Lub wylistuj konkretne pola, jeśli nie chcesz edytować wszystkich

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Używamy CKEditor dla organizational_details oraz route (sekcja: "Что вас ожидает")
        self.fields['organizational_details'].widget = CKEditorWidget()
        self.fields['route'].widget = CKEditorWidget()  # Jeśli chcesz formatować marzrutę

class TourAdmin(admin.ModelAdmin):
    form = TourAdminForm
    inlines = [TourImageInline]
    # Pola, które mają być widoczne w liście widoku w adminie
    list_display = ('title', 'short_description', 'price', 'duration', 'starting_point')
    # Pola dostępne w widoku edycji
    fields = (
        'title',
        'short_description',
        'description',
        'route',  # Секция: "Что вас ожидает"
        'price',
        'duration',
        'starting_point',  # Możliwość dodawania linków
        'image',  # Główne zdjęcie
        'organizational_details',  # Szczegóły organizacyjne z CKEditor
    )
    search_fields = ('title', 'description', 'route')  # Zaktualizuj według potrzeb

    # Konfiguracja dla CKEditor
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()},
    }

admin.site.register(Tour, TourAdmin)
admin.site.register(Post, PostAdmin)