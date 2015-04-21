The Video Preview Utility (for lack of a better name) utilizes the “Video Thumbnails Maker” tool to generate a sheet of
evenly space thumbnail preview images for all video files in a directory. It copies all of those images to a subdirectory,
creates an HTML file with all of the preview images and generates a log of all videos successfully processed
and any videos where an error occurred. It’s a heck of a lot quicker to scroll down a HTML page looking for anything of
interest than it is to click around in hundreds of videos.

Setup:
Note: These instructions cover Windows and assume Python 2.7.x is installed. No third party libraries were used.

Step 1 is to download and install Video Thumbnails Maker from http://www.suu-design.com/downloads.html. As I write this
it’s the third program from the top on that page.

Step 2 is to add the directory where it installs to into your system’s path. The directory where it installed on my
laptop was “C:\Users\Matt\AppData\Local\Video Thumbnails Maker”. Once you add it to your path and restart your machine it
should be setup but you can check by opening up a command prompt and typing “VideoThumbnailsMaker.exe”. If the program starts then
it’s in your path and our script will be able to find it no matter which directory you run it from.

Step 3 is to start Video Thumbnails Maker (this is the only time we will use it graphically), click on “environment” and deselect
the “VTX (Video Thumbnails File)” Box. Leaving it selected wouldn’t hurt anything but it would place VTX files into
your videos directory which aren’t needed.

Once these steps are done you should be ready to run the script. Download videoPreviewUtility.py, place it into
a directory with your video files and run it. It will create a subdirectory with a name of the current date and time.
It will then attempt to generate a video preview image for every .mov, .mp4, .avi and .wmv file in the directory.
Adding additional file types or extension names should be as easy as adding another OR option on what is currently line
number 24. As mentioned earlier, in addition to the preview images themselves it also generates an HTML report with all
of the video previews and a log file with all successfully previewed videos and any which weren’t able to be previewed.
