## VideoPreviewUtility v2015_0418
## Python 2.7
## @matt0177

import os
import subprocess
import time
import shutil

#Initial Variables
successCounter = 0
program = 'VideoThumbnailsMaker.exe'
currentTime = (time.strftime("%m_%d_%Y_%H_%M_%S"))
print "Starting at: %s" % (currentTime)
os.makedirs(currentTime) #Create Output Directory
logFileName = ".\\" + currentTime + "\\" + currentTime + "_LogFile.txt"
logOutput = open(logFileName, 'w')
reportFileName = ".\\" + currentTime + "\\" + currentTime + "_Report.html"
reportOutput = open(reportFileName, 'w')
reportOutput.write("<html><h1> Report for %s</h1>"%(currentTime))

for file in os.listdir("."):
	fileLower = file.lower()
	if fileLower.endswith(".mov") or fileLower.endswith(".mp4") or fileLower.endswith(".avi") or fileLower.endswith(".wmv"): # Filetypes to process
		#print "Processing %s" % (file)
		subprocess.call([program, file])
		outputJpgName = file + ".jpg"
		if os.path.exists(outputJpgName):
			#print "Generated %s" % (outputJpgName)
			successCounter = successCounter + 1
			outputPath = ".\\" + currentTime + "\\" + outputJpgName
			shutil.move(outputJpgName,outputPath) 
			reportOutput.write('<img src="%s" WIDTH="90%%">\n<br><br>'%(outputJpgName))
			logOutput.write("Generated %s\n" % (outputJpgName)) 
			print ".",
			
		else:
			print "\nThere may have been an issue with %s as %s doesn't seem to exist" % (file, outputJpgName)
			logOutput.write("!!!!!!!!Error with %s\n" % (file)) 

print "\nSuccessfully Processed %d Videos" % (successCounter)
logOutput.close()
reportOutput.write("</html>")
reportOutput.close()