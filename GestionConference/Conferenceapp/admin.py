from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Gestion des conférences"
admin.site.site_title = "Administration des conférences"
admin.site.index_title = "Bienvenue dans l'administration des conférences"

# Inline pour les soumissions en mode Stacked (vertical)
class SubmissionStackedInline(admin.StackedInline):
    model = Submission
    readonly_fields = ('submission_id', 'submission_date', 'created_at', 'updated_at')
    extra = 0  # Ne pas afficher de formulaires vides par défaut
    max_num = 10  # Limiter le nombre d'inlines
    
    # Organisation en sections pour l'inline
    fieldsets = (
        ('Informations de base', {
            'fields': ('user_id', 'title', 'abstract', 'keyword')
        }),
        ('Fichier et statut', {
            'fields': ('paper', 'status', 'payed')
        }),
        ('Métadonnées', {
            'fields': ('submission_id', 'submission_date'),
            'classes': ('collapse',)
        }),
    )

# Inline pour les soumissions en mode Tabular (tableau)
class SubmissionTabularInline(admin.TabularInline):
    model = Submission
    fields = ('title', 'status', 'user_id', 'payed')
    readonly_fields = ('submission_id', 'submission_date')
    extra = 0
    max_num = 5

# Configuration personnalisée pour l'admin Conference
@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    # Affichage dans la liste
    list_display = ('name', 'theme', 'location', 'start_date', 'end_date', 'duration')
    
    # Filtres et recherche
    list_filter = ('theme', 'location', 'start_date')
    search_fields = ('name', 'description', 'location')
    
    # Organisation du formulaire en sections
    fieldsets = (
        ('Informations générales', {
            'fields': ('Conference_id','name', 'theme', 'description')
        }),
        ('Logistique', {
            'fields': ('location', 'start_date', 'end_date'),
            'classes': ('wide',)
        }),
    )
    readonly_fields = ('Conference_id',)
    
    # Améliorations visuelles
    ordering = ('start_date',)
    date_hierarchy = 'start_date'
    
    # Ajouter les inlines (utiliser SubmissionStackedInline par défaut)
    inlines = [SubmissionStackedInline]
    
    # Pour tester la version tabulaire, remplacez la ligne précédente par :
    # inlines = [SubmissionTabularInline]

# Configuration pour Submission
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('submission_id', 'title', 'user_id', 'conference_id', 'status', 'payed', 'submission_date')
    list_filter = ('status', 'payed', 'conference_id')
    search_fields = ('title', 'abstract', 'user_id__username', 'user_id__email')
    readonly_fields = ('submission_id', 'submission_date', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Informations de base', {
            'fields': ('user_id', 'conference_id', 'title', 'abstract', 'keyword')
        }),
        ('Fichier et statut', {
            'fields': ('paper', 'status', 'payed')
        }),
        ('Métadonnées', {
            'fields': ('submission_id', 'submission_date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

# Configuration pour Organizing_commiteee
@admin.register(Organizing_commiteee)
class OrganizingCommitteeAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'conference_id', 'role', 'date_joined')
    list_filter = ('role', 'conference_id', 'date_joined')
    search_fields = ('user_id__username', 'user_id__email', 'conference_id__name')

# Les modèles sont maintenant enregistrés automatiquement via les décorateurs @admin.register
