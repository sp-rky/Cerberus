# **Cerberus Build Logs**

Basically just my ramblings while I build Cerberus. I'm sure this will be good to look back on as the project evolves and matures.

## **13/10/24:**

Today was the first real day of working on Cerberus, aside from last weekend where I basically just figured out what I wanted to build. I've decided to focus on building the battery charging system first, seeing as that will be the most challenging part of the build, and also the part that I know the least about. I know the basics of battery charging, but I've never really gone into the specifics before. 

The plan is to have about 500Wh of capacity made up of about 100 18650 LiFePO<sup>4</sup> cells, wired in a 3S configuration. I'm likely going to build this into the lid because I will have a lot of extra space in there behind the screens. I'm thinking about making the cells swappable so that changing out dead cells is an easier task.

Because I want to be able to charge the battery pack from a wide variety of voltages, I've decided to go the route of building my own semi custom charging circuit. I initially was ready to go full custom - building my own buck-boost converter and controlling the whole thing with a microcontroller - but electronic circuits make my head hurt and I can never make them work, so I decided to use an off the shelf buck-boost converter based around a SC8701 buck-boost controller. I'm stil going to control the charger using a microcontroller (likely a RPi Pico, purely just because I've never had a chance to use one and I've always wanted to), but not having to design a complex power control circuit is going to remove a lot of the headache. Ideally Cerberus will be able to charge off of an inbuilt solar panel as well, so I'm going to program a MPPT charging algorithm into it. 

I wish that I was able to sketch, because I want to draw the image that I have for Cerberus so that I have a reference to go back on, but unfortunately I have the drawing skills of a blind toddler. Maybe a 3D mockup isn't a bad idea when I've started to finalise the parts. 

I've got some cool ideas for how I want to connect the two halve's electronics - getting power to the bottom half of the case is obviously necessary, and I'm leaning towards having the main computer built into the lower half so that connecting peripherals and other devices is easier, so I'm going to have to figure out how to get video for the main screen and the SPI data for the E-Ink display up into the top half. 

## **21/10/24**
I didn't get a chance to finish my train of thought during my last log. I'll finish it here instead: I have a few ideas about the connection between the two halves - HDMI can be done neatly using a flat cable and a couple of well placed connectors, the SPI bus and other miscellaneous signals can travel along a rainbow ribbon cable, and power can be shared between the two halves using a pair of microphone connectors (like [this](https://www.jaycar.com.au/2-pin-line-male-microphone-connector/p/PP2015)), and a curly silicon cable (like the type used in mechboard builds) to connect the two halves. While having the battery connection being removable serves little purpose, I think it's going to look awesome, so I'm doing it.

Otherwise, I haven't really done anything since the last log. It's been a hell of a week, and no parts have arrived yet. I'm just about to start work on the e-ink driver code for the chatbot screen - I have no idea what it will look like currently, but I really need to work on something now before I get too depressed today - that way I'll feel like I'm actually doing something instead of writing a log lol. 

## **24/10/24**
I never ended up working on the e-ink driver code - I figured I'd stick to the keyboard and battery system for now, as I'll have to build everything else around those two parts. 

I've got a bit of an idea as to how I want to do the keyboard: I will custom design a TKL keyboard PCB, populate it with hotswap connections, and find some good silent tactile switches and low profile keycaps to use with it. I also am probably going to build a seperate numpad, which will be removable (with a small rechargable battery, probably about 500mAh), and contain a semi-long range transmitter for remote control. The power and data connections will plug into sockets hidden under the numpad. 

In other news, the first batch of components for the battery charging system arrived yesterday. I spent the afternoon tinkering with the SC8701 buck-boost converter (god I need a better workspace). So far I've got voltage control understood - that should be easy to program in. As for reading the VBAT, VIN, and current sensors, along with controlling the current, I have yet to sort that out. Either way, I've decided to go with the Raspberry Pi Pico as the microcontroller of choice, purely because it just seems *so* easy to program. Python truly is such a fun programming language, and getting to write microcontroller code in it feels like making a deal with Satan himself. Maybe that's why it's called Python in the first place. I'm going to make an attempt at starting it. 