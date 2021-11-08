
 ######  NOTICE: This program is only supported on MacBook given that you have your Messages app up and running.

# SETUP

##### This program uses zsh but bash should work as well. To be sure, you could change "zsh" to "bash" at the top of the executable.

##### In Terminal:

```
chmod +x sendfile
cd ..
mv 3-sendfile ~/
cd ~/3-sendfile
mv sendfile /usr/local/bin
```


1.  First make "sendfile" executable.
2.  Change working directory to the parent directory of "3-sendfile".
3.  Move the "3-sendfile" to your home directory.
4.  Change working directory to the one you just moved.
5.  Lastly, move the "sendfile" executable to "/usr/local/bin".


# RUNNING

##### To use this program, in Terminal simply type ```sendfile``` followed by the FULL file path (it will not work with ~/) followed by the number (or iCloud email) you wish to message. 


## For example:

```
sendfile /Users/[YOURHOMEDIRECTORY]/3-sendfile/README.md 1234567890
```
### OR
```
sendfile /Users/[YOURHOMEDIRECTORY]/3-sendfile/README.md destination@icloud.com
```

##### The easiest way to use this program is to type the keyword then drag and drop the file into the Terminal which will automatically type its location (followed by the destination).


##### I created this program to have a more convenient way of sending myself files while I use Terminal. On my personal MacBook, I set the number variable to my phone number so I don't have to type my number each time. This program requires a destination to be typed each time but can be easily changed to a single destination by deleting lines 7 and 9 in the "sendfile" executable, line 5 in "main.py", and changing ```"{number}"``` to ```"YOURDESTINATIONHERE"``` on line 12 in "main.py".

#### I hope you find this program as useful as I do. 


