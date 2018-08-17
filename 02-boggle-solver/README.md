## Boggle Solver Challenge

[![Python Language](https://img.shields.io/badge/platform-Python-4280B1.svg)][1]
[![JavaScript Language](https://img.shields.io/badge/language-JavaScript-F4D03F.svg)][2]

### Context

> [Boggle][3] is a 4x4 word game with 16 dice. After the board is shaken, players have 3 minutes to write down all word 
they see on the board. Points are given in the following way:
> - 1 and 2 letter words → 0 points
> - 3 letter words → 1 point
> - 4 letter words → 2 points
> - 5 letter words → 3 points 
> - the longest possible word (16 letter word) → 14 points

> When you build a word, you can only use one letter once! In other words if you travel along the board and you used 
a letter, you cannot use it again for the same word. However, you **can** use it for a new word.
You can travel in any direction on the board, diagonal travel is allowed. And the person with the most points win.

> Challenge: write a Boggle solver that finds all possible words on a given board.

> Tasks: 
> - you should pick a fixed vocabulary (dictionary): Hasbro standard English dictionary
> - choose a dice distribution
> - extend the solver to a 3x3 and 5x5 board
> - add benchmarking to your program
> - be mindful of algorithmic performance
> - what is the **most** number of points possible in Boggle? That is, what is the holy grail of Boggle with a fixed dictionary?

> Submission guideline:

> Your code should return an object in the following format - where there are two key-value pairs:
> - the first pair has the "score" key, and the value should be an integer. 
> - the second par has the "words" key, and the value should be an **alphabetically sorted** list of words.

```python
result = {
    "score": 143,
    "words": [ "" , "", "", "", ... , ""]
}
```

### Language - Libraries - Tools

- [Python 3][1]
- [JavaScript][2]
- Any code/text editor ([atom][4]) or IDE ([PyCharm][5] or [WebStorm][6]) of your choice.

### Resources

- [Boggle dictionary][7]
- [Dice distribution - new version][8]

### Setup and Run Instructions

This folder contains two versions of the solution.
- One in the `python` subfolder:
    - `main.py`: program entry point to get the boggle solver started
    - `solver.py`: class module that implements a boggle game solver
    - `board.py`: module that randomly generates a boggle board
    - `dictionary.py`: module to implement the boggle dictionary using a trie
    - `trienode.py`: class that represents a trie node

The other in the `javascript` subfolder:
    - `boggle_solver.html`: HTML file to display results of the Boggle solver challenge
    - `boggle_solver.js`: JavaScript module that holds all the challenge code
    - `styles/main.css`: simple stylesheet to accompany the HTML file
    - `assets/boggle.jpg`: image file that serves as an icon on our webpage
    - `assets/favicon.ico`: favicon for our webpage 

Finally:
- `dictionary.txt`: the dictionary text file used for this project


**To run the program:**
- Download and unzip this `summer-of-code` project source code.
- From a command line window, navigate to the (newly unzipped) project root folder, and then into the 
`summer-of-code/02-boggle-solver` subfolder.
    - For the Python version:
        - navigate into the `python` subfolder,
        - launch the application by running `python main.py` in the console.

    - For the JavaScript version:
        - navigate into the `javascript` subfolder,
        - open the `boggle_solver.html` file in a web browser.


[1]: https://www.python.org/getit/
[2]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
[3]: https://en.wikipedia.org/wiki/Boggle
[4]: https://atom.io/
[5]: https://www.jetbrains.com/pycharm/download
[6]: https://www.jetbrains.com/webstorm/download
[7]: https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt
[8]: https://www.boardgamegeek.com/thread/300565/review-boggle-veteran-and-beware-different-version