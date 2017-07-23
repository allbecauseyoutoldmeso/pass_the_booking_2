## Pass the Booking

### Instructions:

* To get set up, navigate into this directory and run:        
  ```source myvenv/bin/acvitate```        
  ```pip install -r requirements.txt```

* To run my tests:  
  ```./manage.py test```

* To auto populate data and run app locally:     
  ```python manage.py loaddata autopopulate.json```   
  ```python manage.py runserver```   
  and visit:   
  ***http://127.0.0.1:8000/***

### About my app:
* Only logged in users can add or edit clients, properties and bookings.  To sign up and log in click the 'Sign up' link at the top any page.
* For each model there is a list page, a detail page, and a form page.
* I have linked these pages up in a way that I hope is easily navigable.
* Constraints:        
  Bookings can only be registered if all the dates between the selected check-in and check-out are available for the chosen property.       
  Bookings can only be registered if the check-in date is after today.     
  Bookings can only be registered if the check-in date is earlier than the check-out date.         

### Original Challenge:

Premise        

The goal is to make a simple version of our own core tech product, which is a web app used
by the company to manage our workload.
Call the project PassTheBooking and upload to your Github account.         

App Overview            

Use Django, and a little Bootstrap on the front-end. The focus of the test is to demonstrate
how well you can wire together the app, not on a beautiful crisp design. There is lots to do,
so lean on Django’s default settings, and its time-saving features such as generic views and
forms if you can. For the database, PostgreSQL works much better than MySQL, but it is
probably best to save extra time by using SQLite.
Django is a Model-View-Controller web framework. Confusingly, Django calls its controllers
‘views’, and its views ‘templates’. Its real strength is mapping database tables to python
objects in the models, passing them into a view which is assigned to a URL, and then
depicting the information in the template. The work below focuses on this core practice.     

Models       

The app should have the following models:     

Client – holding information about the client’s personal details.     

Property – holding information about property details, e.g. address, number of bedrooms,
etc. A property must be connected to a client, and a client may have many properties.    

Booking – holding information about the reservation, e.g. date of check-in, check-out, guest
information, etc. A booking must be connected to a property, and a property may have
many bookings.

[User – Django comes complete with an existing User model, used for authentication, which
you should use instead of trying to re-invent the wheel.]   

Interface     

The app should have a homepage, giving the user any useful overview information you can
think of. Beyond that we should be able to access the rest of our pages, which may be
through a standard menu bar or any other method of your devising. However, I recommend
fleshing-out the homepage last.
Most importantly, there must be pages for the records of each of the models.
For example, /bookings/4 should be a page displaying the information associated with a
booking, whose id is 4.
If you have the time, also try to develop your own form page for each of the models. For
example, /bookings/4/edit would be a page with a form allowing the user to edit that
booking record.
Don’t spend any time customizing the Django admin interface. The point of the above work
is to make our own interface through which real users will interact with the app – only the
devs will ever go back there!        

Data       

Please write code (I recommend putting it in a file of its own) that will automatically
populate data. This will help you develop, and help me assess your work.
For example, imagine we had only a single model called Client, with a single field ‘name’.
A data-generating file might look like this:    

```
from .models import Client
names = [‘Alice’,’Ben’,’Chloe’,’Donald’]     
def gen_clients(names)       
for e in names:       
client = Client.objects.create(name=e)      
print client   
return   
```   

Bonus Points
- Tests
- A login / logout page
- Develop pages with tables displaying all the objects for each model
- Use a requirements file for your packages
- Deploy the app!
