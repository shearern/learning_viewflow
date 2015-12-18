Learning
========


Basic Bootstrap Steps
---------------------

 1. Create the Project
 
        django-admin start-admin startproject mysite
    
 2. Create an App
 
        python manage.py startapp ss_zones
    
 3. Add your app to project/settings.py (just the module name)
    And configure DB if you don't want to use sqlite3
 
        INSTALLED_APPS = (
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'ss_zones',
        ) 
    
 4. Start the model file (app/models.py)
   
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
        
            manual = models.FileField(null=True)
            picture = models.ImageField(null=True)
    
    
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
            
 5. Migrate the model to the database
 
        python manage.py makemigrations
        python manage.py migrate --list
        python manage.py migrate
      
 6. Set super user password
 
        python manage.py createsuperuser
        
 7. Optionally register your new tables with the admin tool by editing app/admin.py
 
        from django.contrib import admin
        
        from .models import SecurityDevice
        from .models import SecurityComponent
        
        admin.site.register(SecurityDevice)
        admin.site.register(SecurityComponent) 
        
 8. Test login
 
         python manage.py runserver 8040
         
         browse to http://127.0.0.1:8040/admin
         
        
Loading a Shell with Django
---------------------------

        python manage.py shell