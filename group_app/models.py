from django.db import models

# Create your models here.



class DemoRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=200)
    service = models.CharField(max_length=50)
    message = models.TextField()

    page_url = models.CharField(max_length=500)   # 👈 important
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.page_url}"
    
















class Contact(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    service = models.CharField(max_length=100)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    






















from django.db import models


class PropertyInquiry(models.Model):

    BC_PC_CHOICES = (
        ('BC', 'BC'),
        ('PC', 'PC'),
        ('Both', 'Both'),
    )

    BROKERAGE_CHOICES = (
        ('Brokerage', 'Brokerage'),
        ('Direct', 'Direct'),
        ('Both', 'Both'),
    )

    full_name = models.CharField(max_length=200)

    contact_number = models.CharField(max_length=20)

    email = models.EmailField()

    bc_pc = models.CharField(
        max_length=20,
        choices=BC_PC_CHOICES
    )

    office_no = models.CharField(max_length=100)

    preferred_location = models.CharField(max_length=200)

    budget = models.CharField(max_length=100)

    amount = models.CharField(max_length=100)

    attend_by = models.CharField(max_length=100)

    brokerage_type = models.CharField(
        max_length=20,
        choices=BROKERAGE_CHOICES
    )

    requirement = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name






















class OfficeBooking(models.Model):

    BC_PC_CHOICES = (
        ('BC', 'BC'),
        ('PC', 'PC'),
        ('Both', 'Both'),
    )

    GST_CHOICES = (
        ('Included', 'Included'),
        ('Excluded', 'Excluded'),
        ('Not Applicable', 'Not Applicable'),
    )


    booking_date = models.DateField()

    shifting_date = models.DateField()

    client_name = models.CharField(max_length=200)

    bc_pc = models.CharField(
        max_length=20,
        choices=BC_PC_CHOICES
    )

    office_no = models.CharField(max_length=100)

    deal_amount = models.CharField(max_length=100)

    token_amount = models.CharField(max_length=100)

    security_amount = models.CharField(max_length=100)

    deal_by = models.CharField(max_length=100)

    brokerage = models.CharField(max_length=100)

    cabin = models.CharField(max_length=100)

    work_station = models.CharField(max_length=100)

    maintenance = models.CharField(max_length=100)

    nature_of_work = models.CharField(max_length=200)

    gst = models.CharField(
        max_length=50,
        choices=GST_CHOICES
    )

    pending_amount = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.client_name
    






















class JobCategory(models.Model):

    name = models.CharField(
        max_length=200
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.name
    


class Job(models.Model):

    category = models.ForeignKey(

        JobCategory,

        on_delete=models.CASCADE,

        related_name='jobs',
        null=True,
        blank=True
    )

    JOB_TYPES = (
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
    )
    

    title = models.CharField(max_length=200)

    department = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    experience = models.CharField(max_length=100)

    salary = models.CharField(max_length=100)

    job_type = models.CharField(max_length=100, choices=JOB_TYPES)

    description = models.TextField()

    is_urgent = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    







class JobApplication(models.Model):

    job = models.ForeignKey(

        Job,

        on_delete=models.CASCADE,

        related_name='applications'
    )

    full_name = models.CharField(
        max_length=200
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20
    )

    experience = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=200
    )

    expected_ctc = models.CharField(
        max_length=100
    )

    skills = models.TextField()

    resume = models.FileField(
        upload_to='job_resumes/'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.full_name