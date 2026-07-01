from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')





def foundation(request, section=None):
    valid_sections = [
        "about-foundation",
        "focus-area",
        "impact-achievements",
        "join-mission",
        "voice-impact"
    ]

    if section and section not in valid_sections:
        raise Http404()
    
    context = {
        "active_section" : section
    }

    return render(request, 'foundation.html', context)




def blog(request, section=None):
    valid_sections = [
        "featured-article",
        "latest-articles",
        "trending-insights",
    ]

    if section and section not in valid_sections:
        raise Http404()
    
    context = {
        "active_section" : section
    }

    return render(request, 'blog.html', context)





def industries(request, section="industries_banner"):

    valid_section = [
        "industries_banner",
        "Industries-We-Serve",   
        "Industries",
        "Case-Studies",
        "Our-Impact",
    ]

    if section not in valid_section:
        raise Http404()
    
    context = {
        "active_section" : section,
    }
    return render(request, 'industries.html', context)





def terms(request):
    return render(request, 'terms.html')

def legal_disclaimer(request):
    return render(request, 'legal_disclaimer.html')

def thanks(request):
    return render(request, 'thanks.html')








# ==================================================
# POPUP DEMO REQUEST FORM
# ==================================================

from django.http import JsonResponse

from django.core.mail import send_mail

from django.conf import settings

from .models import DemoRequest


def save_demo_request(request):

    if request.method == "POST":

        try:

            # ==========================================
            # GET FORM DATA
            # ==========================================

            name = request.POST.get("name")

            email = request.POST.get("email")

            phone = request.POST.get("phone")

            company = request.POST.get("company")

            service = request.POST.get("service")

            message = request.POST.get("message")

            page_url = request.POST.get("page_url")


            # ==========================================
            # DATABASE SAVE
            # ==========================================

            DemoRequest.objects.create(

                name=name,

                email=email,

                phone=phone,

                company=company,

                service=service,

                message=message,

                page_url=page_url
            )


            # ==========================================
            # EMAIL SUBJECT
            # ==========================================

            subject = f"New Demo Request From {name}"


            # ==========================================
            # EMAIL MESSAGE
            # ==========================================

            email_message = f"""

            New Demo Request Received


            Full Name: {name}

            Email Address: {email}

            Phone Number: {phone}

            Company Name: {company}

            Selected Service: {service}

            Requirement:

            {message}


            Submitted From Page:

            {page_url}

            """


            # ==========================================
            # SEND EMAIL
            # ==========================================

            send_mail(

                subject,

                email_message,

                settings.EMAIL_HOST_USER,

                ['imukesh638899@gmail.com'],

                fail_silently=False,
            )


            # ==========================================
            # SUCCESS RESPONSE
            # ==========================================

            return JsonResponse({

                "status": "success",

                "message": "Demo Request Submitted Successfully"

            })


        except Exception as e:

            return JsonResponse({

                "status": "failed",

                "message": str(e)

            })


    return JsonResponse({

        "status": "failed",

        "message": "Invalid Request"

    })













from django.shortcuts import render
from django.http import Http404

def about(request, section="about_banner"):

    valid_sections = [
        "about_banner",
        "overview",
        "our-story",
        "vision",
        "mission",
        "achievements",
        "leadership",
        "csr",
    ]

    if section not in valid_sections:
        raise Http404()

    page_titles = {
        "overview": "About Us",
        "our-story": "Our Story",
        "vision": "Our Vision",
        "mission": "Our Mission",
        "achievements": "Achievements",
        "leadership": "Leadership Team",
        "csr": "CSR Activities",
    }

    context = {
        "active_section": section,
        "page_title": page_titles.get(section, "About"),
    }

    return render(request, "about.html", context)

































from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

from .models import Contact
from .models import PropertyInquiry

from .models import OfficeBooking


def contact(request):

    if request.method == "POST":

        form_type = request.POST.get("form_type")


        # ==================================================
        # CONTACT FORM
        # ==================================================

        if form_type == "contact_form":

            name = request.POST.get('name')

            email = request.POST.get('email')

            phone = request.POST.get('phone')

            service = request.POST.get('service')

            message = request.POST.get('message')


            # DATABASE SAVE

            Contact.objects.create(

                name=name,

                email=email,

                phone=phone,

                service=service,

                message=message
            )


            # EMAIL SEND

            subject = f"New Contact Form Submission From {name}"


            email_message = f"""

            New Contact Form Submission


            Name: {name}

            Email: {email}

            Phone: {phone}

            Service: {service}

            Message:

            {message}

            """


            send_mail(

                subject,

                email_message,

                settings.EMAIL_HOST_USER,

                ['imukesh638899@gmail.com'],

                fail_silently=False,
            )


            return render(request, 'thanks.html', {

                'success': True

            })



        # ==================================================
        # PROPERTY INQUIRY FORM
        # ==================================================

        elif form_type == "property_inquiry":

            full_name = request.POST.get('full_name')

            contact_number = request.POST.get('contact_number')

            email = request.POST.get('email')

            bc_pc = request.POST.get('bc_pc')

            office_no = request.POST.get('office_no')

            preferred_location = request.POST.get('preferred_location')

            budget = request.POST.get('budget')

            amount = request.POST.get('amount')

            attend_by = request.POST.get('attend_by')

            brokerage_type = request.POST.get('brokerage_type')

            requirement = request.POST.get('requirement')


            # DATABASE SAVE

            PropertyInquiry.objects.create(

                full_name=full_name,

                contact_number=contact_number,

                email=email,

                bc_pc=bc_pc,

                office_no=office_no,

                preferred_location=preferred_location,

                budget=budget,

                amount=amount,

                attend_by=attend_by,

                brokerage_type=brokerage_type,

                requirement=requirement
            )


            # EMAIL SEND

            subject = f"New Property Inquiry From {full_name}"


            email_message = f"""

            New Property Inquiry Received


            Full Name: {full_name}

            Contact Number: {contact_number}

            Email: {email}

            BC / PC: {bc_pc}

            Office No: {office_no}

            Preferred Location: {preferred_location}

            Budget: {budget}

            Amount: {amount}

            Attend By: {attend_by}

            Brokerage Type: {brokerage_type}

            Requirement:

            {requirement}

            """


            send_mail(

                subject,

                email_message,

                settings.EMAIL_HOST_USER,

                ['imukesh638899@gmail.com'],

                fail_silently=False,
            )


            return render(request, 'thanks.html', {

                'property_success': True

            })



        # ==================================================
        # OFFICE BOOKING FORM
        # ==================================================

        elif form_type == "office_booking":

            booking_date = request.POST.get('booking_date')

            shifting_date = request.POST.get('shifting_date')

            client_name = request.POST.get('client_name')

            bc_pc = request.POST.get('bc_pc')

            office_no = request.POST.get('office_no')

            deal_amount = request.POST.get('deal_amount')

            token_amount = request.POST.get('token_amount')

            security_amount = request.POST.get('security_amount')

            deal_by = request.POST.get('deal_by')

            brokerage = request.POST.get('brokerage')

            cabin = request.POST.get('cabin')

            work_station = request.POST.get('work_station')

            maintenance = request.POST.get('maintenance')

            nature_of_work = request.POST.get('nature_of_work')

            gst = request.POST.get('gst')

            pending_amount = request.POST.get('pending_amount')


            # DATABASE SAVE

            OfficeBooking.objects.create(

                booking_date=booking_date,

                shifting_date=shifting_date,

                client_name=client_name,

                bc_pc=bc_pc,

                office_no=office_no,

                deal_amount=deal_amount,

                token_amount=token_amount,

                security_amount=security_amount,

                deal_by=deal_by,

                brokerage=brokerage,

                cabin=cabin,

                work_station=work_station,

                maintenance=maintenance,

                nature_of_work=nature_of_work,

                gst=gst,

                pending_amount=pending_amount
            )


            # EMAIL SEND

            subject = f"New Office Booking From {client_name}"


            email_message = f"""

            New Office Booking Received


            Booking Date: {booking_date}

            Shifting Date: {shifting_date}

            Client Name: {client_name}

            BC / PC: {bc_pc}

            Office No: {office_no}

            Deal Amount: {deal_amount}

            Token Amount: {token_amount}

            Security Amount: {security_amount}

            Deal By: {deal_by}

            Brokerage: {brokerage}

            Cabin: {cabin}

            Work Station: {work_station}

            Maintenance: {maintenance}

            Nature Of Work: {nature_of_work}

            GST: {gst}

            Pending Amount: {pending_amount}

            """


            send_mail(

                subject,

                email_message,

                settings.EMAIL_HOST_USER,

                ['imukesh638899@gmail.com'],

                fail_silently=False,
            )


            return render(request, 'thanks.html', {

                'booking_success': True

            })

        
        



    return render(request, 'contact.html')


















def office_form(request):

    if request.method == "POST":

        # ==========================================
        # GET FORM DATA
        # ==========================================

        booking_date = request.POST.get('booking_date')

        shifting_date = request.POST.get('shifting_date')

        client_name = request.POST.get('client_name')

        bc_pc = request.POST.get('bc_pc')

        office_no = request.POST.get('office_no')

        deal_amount = request.POST.get('deal_amount')

        token_amount = request.POST.get('token_amount')

        security_amount = request.POST.get('security_amount')

        deal_by = request.POST.get('deal_by')

        brokerage = request.POST.get('brokerage')

        cabin = request.POST.get('cabin')

        work_station = request.POST.get('work_station')

        maintenance = request.POST.get('maintenance')

        nature_of_work = request.POST.get('nature_of_work')

        gst = request.POST.get('gst')

        pending_amount = request.POST.get('pending_amount')


        # ==========================================
        # DATABASE SAVE
        # ==========================================

        OfficeBooking.objects.create(

            booking_date=booking_date,

            shifting_date=shifting_date,

            client_name=client_name,

            bc_pc=bc_pc,

            office_no=office_no,

            deal_amount=deal_amount,

            token_amount=token_amount,

            security_amount=security_amount,

            deal_by=deal_by,

            brokerage=brokerage,

            cabin=cabin,

            work_station=work_station,

            maintenance=maintenance,

            nature_of_work=nature_of_work,

            gst=gst,

            pending_amount=pending_amount
        )


        # ==========================================
        # EMAIL SUBJECT
        # ==========================================

        subject = f"New Office Booking From {client_name}"


        # ==========================================
        # EMAIL MESSAGE
        # ==========================================

        email_message = f"""

        New Office Booking Received


        Booking Date: {booking_date}

        Shifting Date: {shifting_date}

        Client Name: {client_name}

        BC / PC: {bc_pc}

        Office No: {office_no}

        Deal Amount: {deal_amount}

        Token Amount: {token_amount}

        Security Amount: {security_amount}

        Deal By: {deal_by}

        Brokerage: {brokerage}

        Cabin: {cabin}

        Work Station: {work_station}

        Maintenance: {maintenance}

        Nature Of Work: {nature_of_work}

        GST: {gst}

        Pending Amount: {pending_amount}

        """


        # ==========================================
        # SEND EMAIL
        # ==========================================

        send_mail(

            subject,

            email_message,

            settings.EMAIL_HOST_USER,

            ['imukesh638899@gmail.com'],

            fail_silently=False,
        )


        # ==========================================
        # SUCCESS PAGE
        # ==========================================

        return render(request, 'thanks.html', {

            'booking_success': True

        })


    return render(request, 'office_form.html')
















from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .models import Job
from .serializers import JobSerializer
from .models import JobCategory





# =========================================
# CAREER PAGE VIEW
# =========================================

# def career(request, section=None):

#     categories = JobCategory.objects.filter(
#         is_active=True
#     )

#     current_section = None

#     if section:

#         for category in categories:

#             slug = (
#                 category.name
#                 .lower()
#                 .replace('&', '')
#                 .replace(' ', '-')
#             )

#             if slug == section:

#                 current_section = category

#                 break

#     context = {

#         'categories': categories,

#         'current_section': current_section,

#         'current_slug': section
#     }

#     return render(
#         request,
#         'career.html',
#         context
#     )

from django.http import Http404

from .models import JobCategory

from .models import Job

def career(request, section="Open-Positions"):



    valid_sections = [

        "banner",

        "Why-Join-Us",

        "Our-Work-Culture",

        "Open-Positions",

        "Employee-Experiences",

        "Hiring-Process",

        "Benefits-Perks",
    ]



    if section not in valid_sections:

        raise Http404()



    categories = JobCategory.objects.filter(
        is_active=True
    )



    context = {

        "categories": categories,

        "active_section": section,
    }



    return render(

        request,

        "career.html",

        context
    )



# =========================================
# REST API
# =========================================
@api_view(['GET', 'POST'])
def jobs_api(request):

    # =========================================
    # GET REQUEST
    # =========================================

    if request.method == 'GET':

        jobs = Job.objects.filter(
            is_active=True
        ).order_by('-created_at')



        search = request.GET.get('search')

        location = request.GET.get('location')

        department = request.GET.get('department')

        job_type = request.GET.get('job_type')



        if search:

            jobs = jobs.filter(
                title__icontains=search
            )



        if location:

            jobs = jobs.filter(
                location__icontains=location
            )



        if department:

            jobs = jobs.filter(
                department__icontains=department
            )



        if job_type:

            jobs = jobs.filter(
                job_type__icontains=job_type
            )



        serializer = JobSerializer(
            jobs,
            many=True
        )

        return Response(serializer.data)



    # =========================================
    # POST REQUEST
    # =========================================

    elif request.method == 'POST':

        serializer = JobSerializer(
            data=request.data
        )



        if serializer.is_valid():

            serializer.save()

            return Response(

                serializer.data,

                status=201
            )



        return Response(

            serializer.errors,

            status=400
        )
    
















from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage

from .models import JobApplication
from .models import Job



def career_form(request, job_id):
    job = get_object_or_404(
        Job,
        id=job_id
    )


    # ==========================================
    # FORM SUBMIT
    # ==========================================

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        experience = request.POST.get('experience')
        location = request.POST.get('location')
        expected_ctc = request.POST.get('expected_ctc')
        skills = request.POST.get('skills')
        resume = request.POST.get('resume')

        # ==========================================
        # DATABASE SAVE
        # ==========================================


        application = JobApplication.objects.create(
            job = job,
            full_name = full_name,
            email = email,
            phone = phone,
            experience = experience,
            location = location,
            expected_ctc = expected_ctc,
            skills = skills,
            resume = resume
        )


        # ==========================================
        # EMAIL SUBJECT
        # ==========================================

        subject = (
            f"New Job Aplication"
            f"for {job.title}"
        )

        # ==========================================
        # EMAIL MESSAGE
        # ==========================================

        message = f"""
        New Career Application Received

        Job Title: {job.title}

        category: {job.category.name}

        Application Name: {full_name}

        Email : {email}

        Phone : {phone}

        Experience : {experience}

        Current Location : {location}

        Expected CTC : {expected_ctc}

        Skills : {skills}

        """


        # ==========================================
        # EMAIL WITH RESUME
        # ==========================================

        email_message = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['imukesh638899@gmail.com']
        )

        if resume:
            email_message.attach(
                resume.name,
                resume.read(),
                resume.content_type
            )

        email_message.send(
            fail_silently=False
        )

        return render(request, 'thanks.html',
                      {
                          'career_success' : True
                      })
    
    context = {
        'job' : job
    }


    return render(
        request, 'career_form.html', context
    )








    return render(request, 'career_form.html')
