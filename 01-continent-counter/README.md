## Continent Counter Challenge

[![Python Language](https://img.shields.io/badge/platform-Python-4280B1.svg)][1]
[![JavaScript Language](https://img.shields.io/badge/language-JavaScript-F4D03F.svg)][2]

### Context

> Calculate the **size of a continent** you are standing on in your 11 x 11 world in Civilization III.

> Tasks:
> - calculate the size of the continent you're standing on
> - calculate the sizes of all the continents in the world
> - write a random world generator
> - extensd the problem to a n x n size world
> - add benchmarking to your program
> - and pay great attention to performance
 
**Trimmed-down problem statement:** 

> Let’s say we have an 11 x 11 world (represented as an array of array... basically just a grid) and that we want to 
find the size of the continent in the middle (that is, the continent of which tile (5,5) is a part). 
We don't want to count any land tiles belonging to any of the other continents. 
Also, as in Civilization III, we'll say that tiles touching only at the corners are still considered to be on the same 
continent (since units could walk along diagonals).

### Language - Resources

- [Python 3][1]
- [JavaScript][2]
- Any code/text editor ([atom][3]) or IDE ([PyCharm][4] or [WebStorm][5]) of your choice.

### Resources

- [Civilization III][6]

### Setup and Run Instructions

This challenge contains two versions of the solution. 
- One in the `python` subfolder:
    - `continent_counter.py`: python module that holds and runs all the challenge code

- The other in the `javascript` subfolder:
    - `continent_counter.html`: HTML file to display results of the continent counter challenge
    - `continent_counter.js`: JavaScript module that holds all the challenge code
    - `styles/main.css`: simple stylesheet to accompany the HTML file
    - `assets/civilization.jpg`: image file that serves as an icon on our webpage
    - `assets/favicon.ico`: favicon for our webpage

**To run the program:**
- Download and unzip this `summer-of-code` project source code.
- From a command line window, navigate to the (newly unzipped) project root folder, and then into the 
`01-continent-counter` subfolder.
    - For the Python version:
        - navigate into the `python` subfolder,
        - launch the application by running `python continent_counter.py` in the console.

    - For the JavaScript version:
        - navigate into the `javascript` subfolder,
        - open the `continent_counter.html` file in a web browser.


[1]: https://www.python.org/getit/
[2]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
[3]: https://atom.io/
[4]: https://www.jetbrains.com/pycharm/download
[5]: https://www.jetbrains.com/webstorm/download
[6]: https://en.wikipedia.org/wiki/Civilization_III