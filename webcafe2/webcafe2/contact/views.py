from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    #creamos la plantilla vacia
    contact_form= ContactForm()

    #detectamos si se envio por post algun dato, y se si envio un dato rellenas la platilla con esa info
    if request.method == "POST":
        contact_form= ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviamos el correo y redireccionamos 
            email = EmailMessage(
                "La Cafeteria: Nuevo mensaje de contacto",
                "De {} <{}> \n\n Escribio:\n\n{} " .format(name, email, content),
                "no-contestar@inbox.smtp.mailtrap.io ",
                ["diazvinuelagonzalo@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                #todo ha ido bien redirecionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no ha ido bien redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
            
            
            return redirect(reverse('contact')+"?ok")

        

    return render(request, "contact/contact.html", {'form': contact_form})