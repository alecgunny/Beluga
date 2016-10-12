# Whale call detection

Library for creating a solution to the
<a href=https://www.kaggle.com/c/whale-detection-challenge>Kaggle whale call detection
challenge</a>.  This will eventually include an ipython notebook covering the machine learning
and feature development aspects more thoroughly, as well as a separate file for all of the
individual functions for feature development.  Note that only a very small sample is included
here, I'll probably host the full train and test sets in zip files on Dropbox and write a quick
set of functions with the Dropbox python API to load it in and out and unloading the zip files
to keep from having to host a few gigs of data on any one machine.  Once I get that set up
I'll grant you access to the zip file on Dropbox.

To get things running, either open up the "driver.py" file in Spyder (if you have it) and
click either the play button up top or press F5.  Alternatively, open up a command terminal
and navigate to the folder where driver.py is located and run "python driver.py", or if you
want to play around with things once they've run, run "ipython driver.py -i", which will run
the script in an ipython terminal and then run the terminal in an interactive session once it's
done.

If you don't have any sort of git system installed, google "Git Bash". Git is a version control
software that essentially allows you to make changes to code and keep track of the changes
you make.  I won't get into the syntax of all that here, but once you have git bash installed
open up a git bash terminal, navigate to the folder where you want to download the code folder
to, and run "git clone *http address of the git repo, idk what is right now*".  That will
create a folder called Whale in your current directory, and initialize a git repository in it
which will have all of these files.

Anyway take a look for now at some of the basic data stuff.  The point here is that you should
see that the H1s (the samples with a whale call present) and the H0s (the samples without a
whale call) don't really seperate out at all when we plot these two basic features against one
another (the mean of the sample and the variance of the sample), so we're going to have to get
a bit more clever in terms of creating a "feature space" where these samples separate out more
cleanly.