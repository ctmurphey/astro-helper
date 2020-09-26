# astro-helper

This project is meant to be a tool for amatuer astronomers to find when to observe objects in the sky with a telescope. As it stands this will most likely stay a command-line program unless I dive deep into learning other programming languages. The equations for this come from the ASTR414 at the University of Illinois (thank you, Professor Shen). The earth coordinates of the user are obtained using the [IPinfo Library](https://github.com/ipinfo/). This means that a working internet connection is needed in order for these programs to work.

To get the optimal day, the day is simply calulated when \frac{\alpha}{360} = \frac{N_{day}}{365}, where \alpha is the objects J2000 right ascension and N_{day} is the day of the year from 1 to 365. This number is then converted into a day in the year. Since objects change barely 1^\circ/day but move 15^\circ/hr, I did not feel it was worth it to account for leap years.

In order to calculate the peak time for today, several versions of the current time need to be obtained. The first is simply the current time at the user's location, obtained via [datetime library's .now() method](https://docs.python.org/3/library/datetime.html#datetime.datetime.now). The other needed time is the [local sidereal time (LST)](https://en.wikipedia.org/wiki/Sidereal_time) (if you are curious what the current LST is, you can find it [here](https://www.localsiderealtime.com/)). After converting \alpha to hour angles, *HA*, by multiplying \alpha by \frac{24}{180}, obtaining the time until the zenith is as simple as *LST - HA*.

To calculate the rise and set of the object, it uses the equation *\Delta t = cos^{-1}(\delta \times \phi) \times \frac{12}{\pi}* where \delta is the objects declination and \phi is the observers latitude. \Delta t is the difference between the rising time and the peak time as well as the peak time and the setting time, so it is just added/subtracted from the peak time generated earlier to get the rise and set times.

## Version 1: full_helper.py
This is a command-line program that, once run, takes coordinates on a prompt and returns the optimal time to observe the object (when it peaks at midnight) as well as when the object will rise, peak, and set on the current day. If it is determined that the object will never be visible from the obtained location, then the program simply outputs that answer.

## Future versions
Since this project mostly has amatuer astronomers in mind, the next goal is to incorporate a search of various catalogs instead of relying on direct coordinate input. The first catalogs to be included will be the Caldwell and Messier Catalogs due to their relatively short length and focus on visibility with less powerful telescopes. If I still feel motivated enough after making this functionality work, I may try to get it to run outside of a command line. 

Since the catalogs obviously will not include every single sky object, I'll make different files with different names as not to lose functionality of earlier programs.
