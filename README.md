CLI app to comapre and plot laptimes between the two drivers.

Instructions:
- clone the repo to the desired folder <br>
- open cmd/terminal <br>
- run "python f1.py \<type\> \<driver1\> \<driver2\> \<season\> \<race\>" <br>

Type can either be **vs** or **diff**. <br>
**vs** plots lap times of both drivers. <br>
**diff** plots the difference between the lap times (driver1 - driver2). <br>

Season should be the year of the season in question and race should be the race number. <br>
You can use **current** for the current season and **last** for the last race. <br>
After you run the app you should get pyplot GUI to see the graph and a .png file saved in the folder. <br>
<br>
The names should be the same as in "http://ergast.com/mrd/" as the app gets the data from there. <br>
The rule of the thumb is surname or name_surname if there are multiple drivers with the same name.<br>

Examples:
- python f1.py diff max_verstappen alonso 2022 last




  
