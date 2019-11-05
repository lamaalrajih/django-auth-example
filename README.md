# django-auth-example

This app doesn't do very much except for count the number of users and has a protected 'secret page' view + class as view, the latter of which anonymous users aren't allowed to see.

The only issue with this is that Django won't mint new urls/tokens for resetting emails :/
