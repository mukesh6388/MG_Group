from rest_framework import serializers
from .models import Job
from .models import JobCategory


# =========================================
# JOB CATEGORY SERIALIZER
# =========================================

class JobCategorySerializer(

    serializers.ModelSerializer
):

    class Meta:

        model = JobCategory

        fields = '__all__'





# =========================================
# JOB SERIALIZER
# =========================================

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job

        fields = '__all__'


