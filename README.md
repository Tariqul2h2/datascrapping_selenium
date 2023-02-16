# datascrapping_selenium
I tried to scrap data usng selenium


# Installation

Install all the dependencies

```
pip install -r requirements.txt
```

# Change the row number accordingly
if you want to run the script multiple times, change the row number accordingly
>ROW = 4



# Run the program
First you need to run the `extract_web.py` which will extract all the required data and save into a file where a folder will be created named `files` if it does not exist.

```
python extract_web.py
```
After completing the extraction, you need to write all the data into the Excel file, which takes
only few seconds.

```
python extract_fromfile.py
```

All your required data will be found the Excel file.


Now remove all the files. Each files contains only 15-20kbs, so files won't bother you.