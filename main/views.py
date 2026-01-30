from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import InquiryForm, ContactForm
from .models import Inquiry, ServiceInquiry

def index(request):
    # Handle Contact Form (CTA Section)
    contact_form = InquiryForm(request.POST or None)
    
    if request.method == "POST":
        # Check which form was submitted
        if 'contact_submit' in request.POST:
            if contact_form.is_valid():
                inquiry = contact_form.save()
                # Email content for contact form
                admin_message = f"""
New Inquiry Received:

Name: {inquiry.name}
Email: {inquiry.email}
Phone: {inquiry.phone}
Message:
{inquiry.message}
"""
                user_message = f"""
Hi {inquiry.name},

Thank you for reaching out! We have received your message and will get back to you soon.

Your Message:
{inquiry.message}
------------------------------------

Best regards,
R2 Electrical & Air Conditioning
"""
                try:
                    # Send email to admin
                    send_mail(
                        subject=f"New Inquiry from {inquiry.name}",
                        message=admin_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=settings.ADMIN_EMAIL,
                        fail_silently=False,
                    )

                    # Send confirmation email to user
                    send_mail(
                        subject="Thank you for contacting Electra!",
                        message=user_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[inquiry.email],
                        fail_silently=False,
                    )

                    messages.success(request, "Your message has been sent successfully!")
                    return redirect('index')
                except Exception as e:
                    print("Email error:", e)
                    messages.error(request, "Message saved, but failed to send email.")
            else:
                messages.error(request, "Please correct the errors in the contact form.")
        
        # Handle Carousel Form (Service Inquiry)
        elif 'carousel_submit' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            service = request.POST.get('service')
            message_text = request.POST.get('message')

            if name and email and phone and service and message_text:
                service_inquiry = ServiceInquiry.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    service=service,
                    message=message_text
                )

                # Email content for carousel form
                admin_message = f"""
New Service Inquiry:

Name: {service_inquiry.name}
Email: {service_inquiry.email}
Phone: {service_inquiry.phone}
Service: {service_inquiry.service}
Message:
{service_inquiry.message}
"""
                user_message = f"""
Hi {service_inquiry.name},

Thank you for requesting a service! We have received your request for '{service_inquiry.service}' and will contact you soon.

Your Message:
{service_inquiry.message}
------------------------------------

Best regards,
R2 Electrical & Air Conditioning
"""
                try:
                    # Email to admin
                    send_mail(
                        subject=f"New Service Inquiry from {service_inquiry.name}",
                        message=admin_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=settings.ADMIN_EMAIL,
                        fail_silently=False,
                    )
                    # Confirmation email to user
                    send_mail(
                        subject="Thank you for contacting Electra!",
                        message=user_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[service_inquiry.email],
                        fail_silently=False,
                    )
                    messages.success(request, "Your service request has been submitted successfully!")
                    return redirect('index')
                except Exception as e:
                    print("Email error:", e)
                    messages.error(request, "Request saved, but failed to send email.")
            else:
                messages.error(request, "Please fill in all fields in the service form.")

    return render(request, "main/index.html", {'form': contact_form})

# About Page
def about(request):
    return render(request, 'main/about.html')
    
def special(request):
    return render(request, 'main/special.html')
    
def product(request):
    return render(request, 'main/product.html')
    
def air_conditioner_installation(request):
    return render(request, 'main/air_conditioner.html')
    
def electrical_appliance_repair(request):
    return render(request, 'main/electrical_appliance_repair.html')
    
def new_switchboard_installation(request):
    return render(request, 'main/new_switchboard_installation.html')

def fan_supply_installation(request):
    return render(request, 'main/fan_supply_installation.html')

def new_powerpoints_installation(request):
    return render(request, 'main/new_powerpoints_installation.html')
    
def light_repair_installation(request):
    return render(request, 'main/light_repair_installation.html')

def shed_granny_power(request):
    return render(request, 'main/shed_granny_power.html')

def indoor_outdoor_installation(request):
    return render(request, 'main/indoor_outdoor_installation.html')
    
def emergency_call_outs(request):
    return render(request, 'main/emergency_call_outs.html')

def smoke_alarms(request):
    """View function for the Smoke Alarm Compliance page."""
    return render(request, 'main/smoke-alarms.html')

# Services Page
def service(request):
    return render(request, 'main/service.html')

# Projects Page
def project(request):
    return render(request, 'main/project.html')

# Contact Page
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()  # Save to DB

            # Prepare email to admin
            admin_message = f"""
            You received a new contact message:

            Name: {contact_instance.name}
            Email: {contact_instance.email}
            Phone: {contact_instance.phone}
            Subject: {contact_instance.subject}

            Message:
            {contact_instance.message}
            """

            # Prepare email to user
            user_message = f"""
            Hi {contact_instance.name},

            Thank you for contacting us! We have received your message:

            Subject: {contact_instance.subject}
            Message:
            {contact_instance.message}

            We will get back to you soon.

            Best regards,
            The Team
            """

            try:
                # Email to admin
                send_mail(
                    subject=f"New Contact Message from {contact_instance.name}",
                    message=admin_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=settings.ADMIN_EMAIL,
                    fail_silently=False,
                )

                # Email to user
                send_mail(
                    subject="Thank you for contacting us!",
                    message=user_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[contact_instance.email],
                    fail_silently=False,
                )

                messages.success(request, "Your message has been sent successfully!")
                return redirect('contact')
            except BadHeaderError:
                messages.error(request, "Invalid header found.")
            except Exception as e:
                print("Email error:", e)
                messages.error(request, "Something went wrong. Please try again.")
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})
