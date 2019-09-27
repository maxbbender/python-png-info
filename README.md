# python-png-info
A Python script to grab some information about a PNG file located at a URL

### Set Up

Install Python/Set up Virtual Environment for Python 3.X and run

```
pip install -r requirements.txt
```

### Parameters

There are two environment variables you can set to override defaults 

###### IMAGE_URL

**Default** `https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png`

```
export IMAGE_URL=https://logos-download.com/wp-content/uploads/2018/07/Marvel_logo_red.png
```

###### TARGET_FILE

**Default** `header.txt`

```
export TARGET_FILE=a-different-header.txt
```

## Usage

Once your variables are set to your liking run `python main.py` to print out the header info to your console as well as generate a text file containing the output

#### Problem Description

> Write a script that will:
>
> Display the request header in a terminal window for https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
> Save the header information into a text file named header.txt
> Upload the linked image from step 1, header.txt file, and your script to an S3 bucket
> Then:
> 
> 1.       Provide a link to your S3 bucket so the files can be downloaded.
>
> 2.       Provide instructions on how to run your script.

