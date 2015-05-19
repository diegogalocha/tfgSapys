import os
from django.contrib.auth.models import User

def populate():    
    add_user(username = "user1",
             password = "pass1")
            
def add_user(username,password):
    u = User.objects.get_or_create(username = username,password = password)[0]
    return u

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
    from django.contrib.auth.models import User
    populate()