from django.db import models


class SecurityDevice(models.Model):
    '''Represents a type of device that can be used in a security system'''

    title = models.CharField(max_length=128)
    desc = models.TextField(null=True)   # Long description of the purpose of this device

    manufact = models.CharField(max_length=128)
    model_num = models.CharField(max_length=30)

    device_type = models.CharField(max_length=30, choices=[
        ('base', 'base'),
        ('structure', 'structure'),
        ('sensor', 'sensor'),
        ('indicator', 'indicator'),
    ])

    manual = models.FileField(null=True, upload_to='uploads')
    picture = models.ImageField(null=True, upload_to='uploads')


class SecurityComponent(models.Model):
    '''Stores information about a single component in the security system'''

    title = models.CharField(max_length=128)
    purpose = models.TextField(null=True)   # Long description of the purpose of this component

    device = models.ForeignKey(SecurityDevice)

    requires_power = models.BooleanField(default=False)
    volts_required = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    mamps_required = models.IntegerField(null=True)

    supplies_power = models.BooleanField(default=False)
    volts_supplied = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    mamps_supplied = models.IntegerField(null=True)
