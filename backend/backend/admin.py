from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    # Text to put at the end of eachpage's <title>.
    site_title = 'Orbits'

    # Text to put in each page's <h1> (and above login form).
    site_header = 'Orbits Admin'

    # Text to put at the top of the admin index page.
    index_title = 'Admin Panel'
    
    

admin_site = MyAdminSite()