# Django Conference Management System

Un système de gestion de conférences développé avec Django 5.2.

## Fonctionnalités

- **Gestion des utilisateurs** : Système d'authentification personnalisé
- **Gestion des conférences** : Création et administration des conférences
- **Gestion des soumissions** : Soumission et validation des articles (PDF uniquement)
- **Gestion des sessions** : Organisation des sessions de conférence
- **Comité d'organisation** : Gestion des rôles et responsabilités
- **Interface d'administration** : Interface admin Django personnalisée

## Modèles de données

### User (userapp)
- ID utilisateur auto-généré
- Informations personnelles (nom, prénom, email, etc.)
- Système d'authentification Django personnalisé

### Conference (Conferenceapp)
- Informations de la conférence (nom, thème, lieu, dates)
- Validation des dates et durée automatique
- Thèmes disponibles : Computer Science & AI, Computer Science, Social Sciences

### Submission (Conferenceapp)
- Soumissions d'articles liées aux conférences
- Validation des mots-clés (max 10)
- Support fichiers PDF uniquement
- Limitation : 3 soumissions par utilisateur par jour

### Session (Sessionapp)
- Sessions de conférence avec validation des horaires
- Gestion des salles (format alphanumérique)

### Organizing Committee (Conferenceapp)
- Gestion des rôles : Chair, Co-Chair, Member
- Association utilisateurs-conférences

## Validations implémentées

1. **Validation des mots-clés** : Maximum 10 mots-clés séparés par des virgules
2. **Validation des fichiers** : Seuls les fichiers PDF sont acceptés
3. **Validation des dates** : Date de fin > date de début pour les conférences
4. **Validation des salles** : Format alphanumérique pour les salles
5. **Validation des soumissions** : Limite de 3 soumissions par utilisateur par jour
6. **Validation des sessions** : Heure de fin > heure de début
7. **Validation des conférences futures** : Les soumissions ne peuvent être faites que pour des conférences à venir
8. **Validation de l'email** : Format email valide pour les utilisateurs

## Technologies utilisées

- **Django 5.2** : Framework web Python
- **Python 3.13** : Langage de programmation
- **SQLite** : Base de données (développement)
- **Django Admin** : Interface d'administration personnalisée

## Installation et configuration

1. Clonez le repository :
```bash
git clone https://github.com/molka-makri/Django_Project.git
cd Django_Project
```

2. Créez un environnement virtuel :
```bash
python -m venv env
env\Scripts\activate  # Windows
# ou source env/bin/activate  # Linux/Mac
```

3. Installez les dépendances :
```bash
pip install django
```

4. Effectuez les migrations :
```bash
cd GestionConference
python manage.py makemigrations
python manage.py migrate
```

5. Créez un superutilisateur :
```bash
python manage.py createsuperuser
```

6. Lancez le serveur de développement :
```bash
python manage.py runserver
```

7. Accédez à l'application :
- Interface principale : http://127.0.0.1:8000/
- Interface d'administration : http://127.0.0.1:8000/admin/

## Structure du projet

```
Django_Project/
├── GestionConference/          # Projet principal Django
│   ├── manage.py              # Script de gestion Django
│   ├── GestionConference/     # Configuration du projet
│   │   ├── settings.py        # Paramètres Django
│   │   ├── urls.py           # URLs principales
│   │   └── wsgi.py           # Configuration WSGI
│   ├── Conferenceapp/         # Application gestion conférences
│   │   ├── models.py         # Modèles Conference, Submission, etc.
│   │   ├── admin.py          # Configuration admin personnalisée
│   │   ├── apps.py           # Configuration de l'app
│   │   └── migrations/       # Migrations de base de données
│   ├── Sessionapp/           # Application gestion sessions
│   │   ├── models.py         # Modèle Session
│   │   ├── admin.py          # Configuration admin
│   │   └── migrations/       # Migrations
│   └── userapp/              # Application gestion utilisateurs
│       ├── models.py         # Modèle User personnalisé
│       ├── admin.py          # Configuration admin
│       └── migrations/       # Migrations
├── env/                      # Environnement virtuel (non versionné)
├── .gitignore               # Fichiers à ignorer par Git
└── README.md                # Documentation du projet
```

## Auteur

**Molka Makri** - Projet Django pour la gestion de conférences

## Licence

Ce projet est développé dans un cadre éducatif.