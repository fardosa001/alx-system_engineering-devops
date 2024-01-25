0x1A-application_server

# Task 0.

Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.

Install the net-tools package on your server: sudo apt install -y net-tools

Git clone your AirBnB_clone_v2 on your web-01 server.

Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.

Your Flask application object must be named app (This will allow us to run and check your code).

## Task 2

Requirements:

Install Gunicorn and any other libraries required by your application.

The Flask application object should be called app. (This will allow us to run and check your code)

You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point.

In order to check your code, the checker will bind a Gunicorn instance to port 6000, so make sure nothing is listening on that port.
