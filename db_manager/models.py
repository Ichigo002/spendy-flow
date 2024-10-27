from django.db import models as m
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

### USER

class UserProfile(m.Model):
    user = m.OneToOneField(User, on_delete=m.CASCADE)  # Link to the User model
    # Add custom fields here
    currency_sign = m.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    

# Signals to create and save the UserProfile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

### CATEGORIES

class income_categories(m.Model):
    user_id = m.ForeignKey(User, on_delete=m.CASCADE)
    title = m.CharField(verbose_name="Title", max_length=255)
    color = m.CharField(verbose_name="Color of income's bg", max_length=255)

class expense_categories(m.Model):
    user_id = m.ForeignKey(User, on_delete=m.CASCADE)
    title = m.CharField(verbose_name="Title", max_length=255)
    color = m.CharField(verbose_name="Color of expense's bg", max_length=255)

### ONE-TIME

class one_time_incomes(m.Model):
    #date, id == provided by built-in django system

    user_id = m.ForeignKey(User, on_delete=m.CASCADE)
    reason = m.CharField(verbose_name="Reason", max_length=255)
    amount = m.FloatField("Amount")
    income_category_id = m.ForeignKey(income_categories, on_delete=m.SET_NULL, null=True)

class one_time_expenses(m.Model):
    #date, id == provided by built-in django system

    user_id = m.ForeignKey(User, on_delete=m.CASCADE)
    reason = m.CharField(verbose_name="Reason", max_length=255)
    amount = m.FloatField("Amount")
    expense_category_id = m.ForeignKey(expense_categories, on_delete=m.SET_NULL, null=True)

### SUBSCRIPTIONS

class subscription_periods(m.Model):
    name = m.CharField(verbose_name="Name", max_length=255)
    written_value = m.CharField(verbose_name="Wrriten value", max_length=255)

class subscriptions(m.Model):
    user_id = m.ForeignKey(User, on_delete=m.CASCADE)
    title = m.CharField(verbose_name="Title", max_length=255)
    description = m.TextField(null = True)
    price = m.FloatField(verbose_name="Price")
    subscription_period = m.ForeignKey(subscription_periods, on_delete=m.SET_NULL, null=True)
    custom_period = m.SmallIntegerField(verbose_name="Custom period in days")

