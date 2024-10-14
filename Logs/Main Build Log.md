# **Cerberus Build Logs**

Basically just my ramblings while I build Cerberus. I'm sure this will be good to look back on as the project evolves and matures.

## **13/10/24:**

Today was the first real day of working on Cerberus, aside from last weekend where I basically just figured out what I wanted to build. I've decided to focus on building the battery charging system first, seeing as that will be the most challenging part of the build, and also the part that I know the least about. I know the basics of battery charging, but I've never really gone into the specifics before. 

The plan is to have about 500Wh of capacity made up of about 100 18650 LiFePO<sup>4</sup> cells, wired in a 3S configuration. I'm likely going to build this into the lid because I will have a lot of extra space in there behind the screens. I'm thinking about making the cells swappable so that changing out dead cells is an easier task.

Because I want to be able to charge the battery pack from a wide variety of voltages, I've decided to go the route of building my own semi custom charging circuit. I initially was ready to go full custom - building my own buck-boost converter and controlling the whole thing with a microcontroller - but electronic circuits make my head hurt and I can never make them work, so I decided to use an off the shelf buck-boost converter based around a SC8701 buck-boost controller. I'm stil going to control the charger using a microcontroller (likely a RPi Pico, purely just because I've never had a chance to use one and I've always wanted to), but not having to design a complex power control circuit is going to remove a lot of the headache. Ideally Cerberus will be able to charge off of an inbuilt solar panel as well, so I'm going to program a MPPT charging algorithm into it. 

I wish that I was able to sketch, because I want to draw the image that I have for Cerberus so that I have a reference to go back on, but unfortunately I have the drawing skills of a blind toddler. Maybe a 3D mockup isn't a bad idea when I've started to finalise the parts. 

I've got some cool ideas for how I want to connect the two halve's electronics - getting power to the bottom half of the case is obviously necessary, and I'm leaning towards having the main computer built into the lower half so that connecting peripherals and other devices is easier, so I'm going to have to figure out how to get video for the main screen and the SPI data for the E-Ink display up into the top half. 
