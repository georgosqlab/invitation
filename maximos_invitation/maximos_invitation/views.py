from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json


def main_page(request):
    # Get language from URL parameter (?lang=en or ?lang=el)
    lang = request.GET.get('lang', 'en')

    # Define translations
    translations = {
        'en': {
            'baptism': 'Baptism',
            'date': 'August 2nd 2025',
            'celebration': 'A day of faith and celebration',
            'maximos': 'Maximos',
            'home': 'Home',
            'rsvp': 'RSVP',
            'invitation': 'Invitation',
            'location': 'Location',
            'rsvp_title': 'WE HOPE YOU CAN JOIN US!',
            'rsvp_subtitle': 'Kindly respond by June 30, 2025',
            'rsvp_stats': 'Celebration Countdown',
            'days': 'Days',
            'hours': 'Hours',
            'minutes': 'Minutes',
            'seconds': 'Seconds',
            'rsvp_question': 'WILL YOU JOIN US?',
            'rsvp_prompt': "We'd love to celebrate with you!",
            'name_label': 'Your Name(s)',
            'email_label': 'Email',
            'guests_label': 'Number of Guests',
            'select_option': 'Choose...',
            'attendance_label': 'Attendance',
            'attending': 'Accept',
            'declining': 'Decline',
            'message_label': 'Message (Optional)',
            'rsvp_closing': 'Georgos, Kiki & Maximos',
            'intro': 'Hi! My name is Maximos,',
            'text':'I’m a little bundle of joy with a big smile and lots of giggles. I love exploring the world '
                   'around me and making everyone laugh. I’m so excited to celebrate my baptism and I can’t '
                   'wait to share this special day with all the people I love!',
            'ceremony': 'Ceremony',
            'celebration': 'Celebration',
            'get_directions': 'Get Directions',
        },
        'el': {
            'baptism': 'Βάπτιση',
            'date': '2 Αυγούστου 2025',
            'celebration': 'Μια μέρα πίστης και γιορτής',
            'maximos': 'Μάξιμος',
            'home': 'Αρχική',
            'rsvp': 'Επιβεβαίωση',
            'invitation': 'Πρόσκληση',
            'location': 'Τοποθεσία',
            'rsvp_title': 'ΕΛΠΙΖΟΥΜΕ ΝΑ ΜΠΟΡΕΣΕΤΕ ΝΑ ΕΡΘΕΤΕ!',
            'rsvp_subtitle': 'Παρακαλώ απαντήστε έως 30 Ιουνίου 2025',
            'rsvp_stats': 'Αντίστροφη Μέτρηση',
            'days': 'Μέρες',
            'hours': 'Ώρες',
            'minutes': 'Λεπτά',
            'seconds': 'Δευτερόλεπτα',
            'rsvp_question': 'ΘΑ ΕΡΘΕΤΕ;',
            'rsvp_prompt': 'Θα χαρούμε να γιορτάσουμε μαζί σας!',
            'name_label': 'Ονοματεπώνυμο',
            'email_label': 'Email',
            'guests_label': 'Αριθμός Ατόμων',
            'select_option': 'Επιλέξτε...',
            'attendance_label': 'Παρουσία',
            'attending': 'Αποδοχή',
            'declining': 'Απόρριψη',
            'message_label': 'Μήνυμα (Προαιρετικό)',
            'rsvp_closing': 'Γιώργος, Κική & Μάξιμος',
            'intro': 'Γεια χαρά! Είμαι ο Μάξιμος,',
            'text': 'Είμαι ένα μικρός μπόμπιρας χαράς με ένα πλατύ χαμόγελο και μου αρέσει να εξερευνώ τον κόσμο '
                   'γύρω μου και να κάνω τους πάντες να γελούν. Είμαι τόσο ενθουσιασμένος που γιορτάζω τη βάπτισή μου και δεν μπορώ να '
                   'περιμένω να μοιραστώ αυτή την ξεχωριστή μέρα με όλους τους ανθρώπους που αγαπώ!',
            'ceremony': 'Τελετή',
            'celebration': 'Εορτασμός',
            'get_directions': 'Τοποθεσία',
        }
    }

    context = {
        'lang': lang,
        't': translations[lang]  # Pass translations to template
    }
    return render(request, 'maximos_invitation/main.html', context)


@require_POST
def handle_rsvp(request):
    try:
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        guests = data.get('guests')
        attendance = data.get('attendance')
        message = data.get('message', '')

        # Here you would typically save the RSVP to your database
        # Example:
        # Rsvp.objects.create(
        #     name=name,
        #     email=email,
        #     guests=guests,
        #     attending=(attendance == 'yes'),
        #     message=message
        # )

        return JsonResponse({
            'success': True,
            'message': 'Thank you for your RSVP! We look forward to seeing you.'
            if attendance == 'yes'
            else 'We will miss you! Thank you for letting us know.'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'There was an error processing your RSVP. Please try again.'
        })