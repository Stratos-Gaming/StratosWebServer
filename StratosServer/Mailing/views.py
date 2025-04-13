from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
# Create your views here.
def send_email_help_request(request):
    subject = "Stratos: Richiesta di assistenza per il tuo progetto"
    message = f"""Gentile utente,

Abbiamo ricevuto la tua richiesta di assistenza per il progetto.

Il nostro team ti contatterà al più presto per fornirti il supporto necessario.
Se hai bisogno di assistenza immediata, puoi rispondere direttamente a questa email.

Nel frattempo, puoi consultare:
- La nostra documentazione: [LINK_DOCUMENTAZIONE]
- Le FAQ: [LINK_FAQ]
- I tutorial video: [LINK_TUTORIAL]

Grazie per aver scelto Stratos Gaming.
Cordiali saluti,
Il team di Stratos
    """
    from_email = 'info@stratosgaming.it'  # sender is always the same
    recipient_list = [request.POST.get('email')]  # get receiver's email from the request
    
    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return HttpResponse("Notifica di assistenza inviata correttamente.")
    except Exception as e:
        return HttpResponse(f"Si è verificato un errore: {e}", status=500)
# utils.py


