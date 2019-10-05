from django.db import models
from django.core.validators import URLValidator
from django.core.validators import MinLengthValidator

def get_upload_static_image(instance, filename):
    return 'static_images/{0}'.format(filename)

class Upload_Image(models.Model):
    class Meta:
        verbose_name_plural = 'Upload Image'

    image = models.ImageField(upload_to=get_upload_static_image,
                                default='',
                                blank=False)
    def __str__(self):

        return '{a}'.format(a=self.image)


def get_amazing_places_image(instance, filename):
    return 'static_images/{0}'.format(filename)

class Amazing_Places(models.Model):
    class Meta:
        verbose_name_plural = 'Amazing Places'

    image = models.ImageField(upload_to=get_amazing_places_image,
                                default='',
                                blank=False)
    title = models.CharField(max_length=50,
                               default='',
                               validators=[MinLengthValidator(3)])
    description = models.CharField(max_length=500,
                              default='',
                              validators=[MinLengthValidator(3)],blank=False)
    link = models.CharField(max_length=500,
                                default='',
                                validators=[URLValidator()])
    def __str__(self):

        return '{a}'.format(a=self.title)


class Amazing_Photos(models.Model):
    class Meta:
        verbose_name_plural = 'Amazing Photos'

    image = models.ImageField(upload_to=get_amazing_places_image,
                                default='',
                                blank=False)
    title = models.CharField(max_length=50,
                               default='',
                               validators=[MinLengthValidator(3)])
    description = models.CharField(max_length=500,
                              default='',
                              validators=[MinLengthValidator(3)],blank=False)
    link = models.CharField(max_length=500,
                                default='',
                                validators=[URLValidator()])
    def __str__(self):

        return '{a}'.format(a=self.title)


class Shedule_Ride(models.Model):
    class Meta:
        verbose_name_plural = 'Shedule Ride'

    full_name = models.CharField(max_length=30,
                               default='',
                               validators=[MinLengthValidator(4)])
    email = models.EmailField()
    group_members = models.CharField(max_length=2,
                               default='',
                               validators=[MinLengthValidator(1)])
    message = models.CharField(max_length=250,
                               default='',
                               blank=True)



    def __str__(self):
        return '{} contacting CodeForCoder'.format(self.full_name).capitalize()
