# Instructions


Installation Instructions
-------------------------
In this course we will use Python 3.6 and Jupyter notebook. 
- Have these installed before the class if you plan to use your own laptop
- The lab does have desktops with these software installed


Install Python 3.6 and Jupyter:
------------------------------
If you already have Python 3.6 and Jupyter installed on your computer then you can skip the following download instructions.

Option 1:
--------
https://www.python.org/downloads/
http://jupyter.org/install


Option 2:
--------
Download Anaconda (https://www.anaconda.com/download/#macos)

Pick the appropriate operating system and choose Python, version 3.6. Once the installer is downloaded, execute it. This will install Anaconda and associated packages on your computer.

Depending on your operating system, open “Anaconda Navigator”

Jupyter notebook is a browser based tool to execute Python code. This is popular for teaching and learning. To launch Jupyter notebook, click on the launch button under the Jupyter logo. This will launch your default browser and open the homepage of Jupyter. 


Option 3:
--------
Install Docker

1. Make sure your hardware and software is supported by Docker CE (Community Edition, Free Software)

https://docs.docker.com/docker-for-mac/install/
https://docs.docker.com/docker-for-windows/install/


2. Download Docker

- Docker for Windows:
https://download.docker.com/win/stable/17513/Docker%20for%20Windows%20Installer.exe

- Docker for Mac:
https://download.docker.com/mac/stable/24312/Docker.dmg

3.  Open a shell (terminal or cmd) from your laptop to start a jupyter notebook container

4. $docker run -ti -p 8888:8888 --hostname localhost jupyter/minimal-notebook

5. Point your browser to the url that was  output from the last command
6. Open a terminal from **jupyter**. This is a terminal/shell into to the jupyter container.
- cd work
-  git clone https://github.com/rkripa/python-for-beginners.git

7. From the jupyter browser navigate to python-for-begineers/ucsc/week-1[a-b]
Click on the Lecture-1.ipynb or Lecture-2.ipynb  from **jupyter**



Download the jupyter notebooks from github:
------------------------------------------

Option 1:
--------
If you have git installed on your computer you can: 
$git clone https://github.com/rkripa/python-for-beginners.git


Option 2:
--------
Visit the github.com using the url:  https://github.com/rkripa/python-for-beginners

Press the green button which says "Clone or download".  Then click on the download ZIP file on your laptop and unzip its contents.
