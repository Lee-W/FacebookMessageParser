# Facebook Message Parser
Parse your facebook chatting history archive from HTML to JSON.

## Description
Follow the [Downloading Your Info](https://www.facebook.com/help/131112897028467#) instruction by Facebook, and you can download all your facebook info.  

However, there might exist chatting history that is too large for the browser to display.  
Thus, by parsing it into JSON format, you can render using other mechanism or do further analysis.

## Setup

### Prerequisite
- Python3

### Install dependency

```sh
pip install -r requirements.txt
```


## Usage

```sh
python parser.py [-o OUTPUT_FILE] input_file
```

- input_file
    - message html file to parse
- output_file
    - output filename (default is the name +'.json')  


## Todo
- Parse the whole directory

## AUTHORS
[Lee-W](https://github.com/Lee-W)