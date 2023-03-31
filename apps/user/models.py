from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        print("_________________Called")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_mentor', False)
        extra_fields.setdefault('is_user', False)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(username, email, password, **extra_fields)



class MentorUser(AbstractUser):
    is_mentor = models.BooleanField(default=False, blank=True)
    is_user = models.BooleanField(default=False, blank=True)

    contact = models.CharField(max_length=25)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


    # for mentor user
    rating = models.IntegerField(default=5, blank=True)  #start from 1 to 5
    followers = models.IntegerField(default=0, blank=True)

    hourly_rate = models.IntegerField(default=0, blank=True)
    total_earning = models.IntegerField(default=0, blank=True)
    total_mentorship = models.IntegerField(default=0, blank=True)
    total_mentorship_hours = models.IntegerField(default=0, blank=True)
    currency = models.CharField(max_length=10, default='BDT')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'contact', 'username']

    objects = CustomUserManager()



class Education(models.Model):
    user_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE)

    institute = models.CharField(max_length=100) 
    degree = models.CharField(max_length=100)
    start_date = models.DateField(default=None, null=True, blank=True)
    currently_studying = models.BooleanField(default=False)
    end_date = models.DateField()
    description = models.TextField()
    achievement = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class WorkingExperience(models.Model):
    user_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField(default=None, null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    end_date = models.DateField(default=None, null=True, blank=True)
    description = models.TextField()
    achievement = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class MentorshipArea(models.Model):
    user_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Achievement(models.Model):
    user_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE)
    achievement = models.CharField(max_length=100)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Language(models.Model):
    user_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    mentor_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE, related_name='feedback_mentor_id')
    user_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE, related_name='feedback_user_id')
    feedback = models.TextField()
    rating = models.IntegerField(default=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Follow(models.Model):
    mentor_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE, related_name='follow_mentor_id')
    follower_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE, related_name='follow_follower_id')

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Meeting(models.Model):
    user_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE, related_name='meeting_user_id')
    mentor_id = models.ForeignKey(MentorUser, on_delete=models.CASCADE, related_name='meeting_mentor_id')
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_link = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Schedule(models.Model):
    pass


