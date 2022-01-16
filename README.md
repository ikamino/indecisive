# indecisive

Indecisive is a program that helps users pick and choose where to eat, based on location and restaurant name*. 

Built for NWHacks 2022

# Build
Built on Python 3.9.7 and based off mainly using Google's Places API to find landmarks tagged restaurant (or within that scope) nearest to the location that the user inputs**. Currently, restaurants are shown to user sorted in order of distance to location. Location is found and inputted through coordinates using geopy libraries - namely Nominatim. (Captures IP for HTTP verification).

*Future scalability is set-up within dictionaries to allow for actual recommendations for users, based on restaurant rating, gender, how they feel etc.

**Preferences can be set up later on to be recorded, allowing for preference/address retention. 

# Installation
Google Places API key is **needed**. Workability from there should be a non-issue given libraries for googlemaps and geopy library installs. All the code that gets run is inside the Model folder. 

*Everything below is just made up of notes and thoughts* 
# Tests
The files in the tests folders aren't necessarily tests as in unit tests - mainly experimental functions that we could pass into larger classes. We just throught it would intersesting to see how the different files came together. (Although they're basically copy pasted into the running code.)

# Unused
The unused folder is the result of broken dreams - ideas that weren't brought into fruiton but have the ability to work with what we currently have to either make our code more readable and easier to follow, or just completely new features all together (Such as outright recommendations based on user preference. That one sounds fun).
