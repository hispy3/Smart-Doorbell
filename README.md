# Smart-Doorbell

Project Goal

This project will create a smart doorbell notification system so that when a guest clicks on the
button, it makes a ring, a camera takes a picture and the microcontroller sends a notification with
some message to notify that a guest has arrived.


Project Approach

The project has the microcontroller as the brain of the notification system. A state machine is
used to control when the bell should ring and how often a picture is taken and a notification sent.
The microcontroller handles bundling a text message with the picture and sending them to a
android based app.
