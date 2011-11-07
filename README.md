Distrix Web Push Demo
=====================

This project demonstrates a method for pushing information from a Distrix system to a web browser.  The demo consists of a Distrix agent with an embedded web server ("WebApp") and an agent that creates notification events ("NotificationGenerator"). The WebApp agent serves a web page containing a button the user can push to begin listening for events.  When the button is pushed, the jQuery javascript library is used to send an AJAX request to the server in the WebApp agent. The WebApp agent receives the request and blocks on a condition variable.  Meanwhile, the WebApp agent is also subscribed to Notification objects.  When the NotificationGenerator agent is run, it creates and publishes a Notification object.  When the WebApp receives a proxy to this object, it signals the condition variable, which causes the AJAX request to complete with the contents of the Notification object.  The jQuery response handler then inserts this content into the web page.

Requirements
------------

 * Distrix System Builder and Core Services (http://www.sparkintegration.com)
 * Python (http://www.python.org)
 * CherryPy (http://cherrypy.org/)

Usage
-----

 1. Install all requirements from above, including Distrix. Install the Distrix python client (cd DISTRIX_INSTALL_DIR/Python/Client; python setup.py install).
 2. Start the Distrix server ("/Distrix/Apps/Server" on Linux/OS X)
 3. Navigate to the WebApp directory and run "python WebApp.py"
 4. Open a browser and navigate to "http://localhost:8080"
 5. Click the "Start listening..." button
 6. With the WebApp agent still running, navigate to the NotificationGenerator directory and run "python NotificationGenerator.py 'My First Notification' 'Hello World'"
 7. Note that the text from the previous command appears in the web browser window
 8. Subsequent invocations of the NotificationGenerator.py agent will replace the text in the web browser with the new text passed as arguments
