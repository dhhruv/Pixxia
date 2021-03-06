<p align="center">
  <img src="https://user-images.githubusercontent.com/72680045/110060576-21bf2300-7d8c-11eb-81df-dafd64ee7b06.png">
  <h2 align="center" style="margin-top: -4px !important;">Complete Solution for Compression of JPG/PNG Files.</h2>
  <p align="center">
    <a href="https://github.com/dhhruv/Pixxia/blob/master/LICENSE">
      <img src="https://img.shields.io/github/license/dhhruv/Pixxia?color=informational">
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/python-v3.8-informational">
    </a>
    <a href="https://github.com/dhhruv/Pixxia">
    	<img src="https://img.shields.io/github/v/release/dhhruv/Pixxia">
    </a>
    <img src="https://img.shields.io/github/downloads/dhhruv/Pixxia/total?color=important">
  </p>
  <p align="center">
    <a href="https://github.com/dhhruv/Pixxia">
      <img src="http://ForTheBadge.com/images/badges/made-with-python.svg">
    </a>
  </p>
</p>

# Pixxia:

The above script uses lossy compression methods to reduce the document size of your JPG/PNG files. This is achieved by rounding up the (R,G,B) values from each pixel of it's unit digit in your image, therefore lesser number of bytes are required to store the information. Sometimes, there are major changes in the bytes stored well as sometimes there are minor changes so it depends entirely on the pixels of the image.

## Image Comparison:

<p align="center">
	<h4 align="left" style="margin-top: -4px !important;">Image 1:</h4>
	<img src="https://user-images.githubusercontent.com/72680045/110210445-c5f1b880-7eb7-11eb-9a11-b1943089cc07.png">
</p>

<p align="center">
	<h4 align="left" style="margin-top: -4px !important;">Image 2:</h4>
	<img src="https://user-images.githubusercontent.com/72680045/110210444-c427f500-7eb7-11eb-8dd7-72f73c58f5fe.png">
</p>

> For Images >= 6 MB you may see a great compression ratio as compared to the images which are smaller in size.

## Setup (Windows):

1. Install Python
2. Clone this repository
```
git clone https://github.com/dhhruv/Pixxia.git
```

3. Install, create and activate virtual environment.
For instance we create a virtual environment named 'venv'.
```
pip install virtualenv
python -m virtualenv venv
venv\Scripts\activate.bat
```

4. Install dependencies
```
pip install -r requirements.txt
```

<p align="center">
	<img src="https://user-images.githubusercontent.com/72680045/110210540-1d902400-7eb8-11eb-85e7-917f006069ec.PNG">
</p>
<br>


## How To Use !
1. Click SELECT INPUT FOLDER Button to select the INPUT FOLDER which contains all the Images to be Compressed/Optimized.
2. Click SELECT OUTPUT FOLDER Button to select the OUTPUT FOLDER which will contain all the the Compressed/Optimized Images.
3. Hit the COMPRESS Button and the INPUT FOLDER containing Supported Image Formats will be Compressed and saved in the OUTPUT FOLDER.
4. Click CLEAR Button to reset the input fields and status bar. (If needed)

> NOTE: Recommended to keep INPUT and OUTPUT Folder different for your ease to differentiate between Optimized and Unoptimized Images.

## Important Note:

-	**This Script goes through each pixel of every supported image in the INPUT folder so it'll take more time than usual to process the Image.**
-	**This Script is just a Prototype so results may be unexpected.**
-	**The Authors will not be responsible for any kind of loss of data so it is essential to have a Backup of Original Data placed in the Input Folder. Read the [LICENSE](https://github.com/dhhruv/Pixxia/blob/master/LICENSE) for more information.**

## Image Credits:
- [Unsplash](https://unsplash.com/)