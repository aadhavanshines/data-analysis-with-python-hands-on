# Data Analysis with Python, Hands-On: Code and Data

[![Check every listing](https://github.com/aadhavanshines/data-analysis-with-python-hands-on/actions/workflows/check.yml/badge.svg)](https://github.com/aadhavanshines/data-analysis-with-python-hands-on/actions/workflows/check.yml)

All the programs, datasets and exercise solutions from the book ***Data Analysis with Python, Hands-On: Clean, Explore, Visualize and Report on Real Data, from Spreadsheets to SQL, with Six Projects, Exercises and Every Example Tested*** by Aadhavan Muthurengan, arranged by chapter.

Every program here was run on Python 3.12, 3.13, 3.14 and 3.15, and its output compared with the output printed in the book. The expected output of each program is stored next to it, so you can check your own runs. The same check runs on GitHub after every change, on all four versions, and its results are public on the [Actions tab](https://github.com/aadhavanshines/data-analysis-with-python-hands-on/actions).

## Getting started

1. Install Python 3.12 or newer from [python.org](https://www.python.org/downloads/).
2. Download this repository: the green **Code** button, then **Download ZIP** (and unzip it), or `git clone https://github.com/aadhavanshines/data-analysis-with-python-hands-on`.
3. In the repository folder, create a virtual environment and install the exact library versions the book was tested with:

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

4. Go to a chapter's folder and run a program, for example:

```
cd code/ch01
python first_look.py
```

On macOS and Linux, type `python3` instead of `python` until you activate the virtual environment.

The datasets are already in `code/data/`, so you can start straight away. To make them yourself, as Chapter 2 describes, run `python make_data.py` inside `code/data`: it writes exactly the same files.

Type the programs yourself first if you can: you'll learn more, and the files here are there to check against.

## Chapters

| Chapter | Topic | Programs | Exercise solutions |
| --- | --- | --- | --- |
| 1 | [What Data Analysis Is](code/ch01/) | 1 |  |
| 2 | [Setting Up and the Book's Data](code/ch02/) | 2 |  |
| 3 | [NumPy Essentials](code/ch03/) | 3 | 2 |
| 4 | [Series and DataFrames](code/ch04/) | 3 | 2 |
| 5 | [Loading and Saving Data](code/ch05/) | 4 | 2 |
| 6 | [Selecting and Filtering](code/ch06/) | 3 | 2 |
| 7 | [Cleaning Messy Data](code/ch07/) | 4 | 2 |
| 8 | [Transforming Columns](code/ch08/) | 3 | 2 |
| 9 | [Grouping and Aggregating](code/ch09/) | 3 | 2 |
| 10 | [Combining Tables](code/ch10/) | 3 | 2 |
| 11 | [Reshaping Data](code/ch11/) | 2 | 2 |
| 12 | [Dates and Time Series](code/ch12/) | 3 | 2 |
| 13 | [Working With Text](code/ch13/) | 2 | 2 |
| 14 | [Charts With matplotlib](code/ch14/) | 4 | 1 |
| 15 | [Choosing Honest Charts](code/ch15/) | 2 |  |
| 16 | [Describing Data With Statistics](code/ch16/) | 3 | 2 |
| 17 | [Comparing Groups and A/B Tests](code/ch17/) | 3 | 1 |
| 18 | [SQL for Analysts](code/ch18/) | 1 | 2 |
| 19 | [Reports, Automation and Testing Your Analysis](code/ch19/) | 3 |  |
| 20 | [Using AI Assistants for Analysis, Safely](code/ch20/) | 2 |  |
| 21 | [Project: Retail Sales Review](code/ch21/) | 4 |  |
| 22 | [Project: Customer Survey](code/ch22/) | 3 |  |
| 23 | [Project: Website A/B Test](code/ch23/) | 3 |  |
| 24 | [Project: Stock Price Study](code/ch24/) | 3 |  |
| 25 | [Project: Air Quality and Clinic Visits](code/ch25/) | 3 |  |
| 26 | [Project: Household Budget](code/ch26/) | 3 |  |
| 27 | [Bigger Data and Faster Code](code/ch27/) | 3 | 1 |
| Appendix F | [The data generator and the datasets](code/data/) | `make_data.py` | |

Charts are saved as PNG files in the folder you run the program from.

## What the files are

| File | Contents |
| --- | --- |
| `name.py` | A program from the book |
| `name.out` | Its output, exactly as printed in the book |
| `name.cmd` | The command used instead of `python name.py` (Chapter 19 runs its tests with pytest) |
| `name.skip` | Not run by itself: `metrics.py` in Chapter 19 is a module the other programs import |
| `solution_*.py` | Worked solutions to the chapter's exercises, also printed in Appendix A |
| `code/data/*.csv` | The ten datasets, made by `make_data.py` |

## Check everything yourself

With the virtual environment active, from the repository folder:

```
python tests/check_data.py       # regenerate the datasets and compare them byte for byte
python tests/run_listings.py     # run every program and compare its output with the .out file
```

Each program runs in a temporary copy of its chapter folder, so the checks never change your files.

If your output differs from the book's in the last digit of a number, check that you installed the versions in `requirements.txt`; newer library versions occasionally round or word things differently.

## About the data

All companies, people, products, cities, stocks and figures in the datasets are fictional, generated with a fixed random seed (2026). Any resemblance to real persons or businesses is coincidental.

## License

The code is released under the [MIT License](LICENSE): use it, change it and share it freely. The book's text is not part of this repository and remains under copyright.
