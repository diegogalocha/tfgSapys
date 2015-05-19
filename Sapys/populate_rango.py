import os
from django.contrib.auth.models import User

def populate():    
    add_user(username = "user2",
             password = "pbkdf2_sha256$10000$6qVV6yvQXDNU$72YJHRHSDszGi9Fxq7vfKo7723TJdv96niQnzk6xDcs=")
            
def add_user(username,password):
    u = User.objects.get_or_create(username = username,password = password)[0]
    return u

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
    from django.contrib.auth.models import User
    populate()