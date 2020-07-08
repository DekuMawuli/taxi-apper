from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.


class Driver(models.Model):
    TITLE = (
        ("Mr.", "Mr."),
        ("Mrs.", "Mrs."),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(default="0000000000", max_length=100)
    vehicle_name = models.CharField(max_length=50)
    vehicle_number = models.CharField(default="0000000", max_length=20)
    title = models.CharField(max_length=10, choices=TITLE)
    current_location = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='images/', default="default.jpg")
    showcase_img = ImageSpecField(source='image', processors=[ResizeToFill(295, 135)], format="PNG", options={'quality':80})
    profile_image = ImageSpecField(source='image', processors=[ResizeToFill(540, 638)], format="PNG", options={'quality':80})
    disp_image = ImageSpecField(source='image', processors=[ResizeToFill(370, 356)], format="PNG", options={'quality':80})
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_title_display()} {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name_plural = "Drivers"


@receiver(sender=User, signal=post_save)
def user_saved(sender, created, instance, **kwargs):
    if created:
        Driver.objects.create(user=instance)
    else:
        instance.driver.save()


class Booking(models.Model):
    STATUS = (
        ("A", "Accepted"),
        ("R", "Rejected"),
        ("P", "Pending"),
    )
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    passengers = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    status = models.CharField(max_length=1, default="P", choices=STATUS)

    def __str__(self):
        return f"{self.full_name} books Driver {self.driver.get_title_display()} {self.driver.user.last_name}"
