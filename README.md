This is a plugin for Sublime Text 2 which automatically opens files for edit in Perforce.

##Installation:

###Option 1:

If you don't plan on getting updates or making improvements you can simply copy "perforce.py" into your user packages folder...

    cd C:\Users\%USERNAME%\AppData\Roaming\Sublime Text 2\Packages\User
    wget https://github.com/seanhoughton/SublimePerforce/blob/master/perforce.py

###Option 2:

If you would like to use git to keep up-to-date and to make improvements you can init a repository in your plugins folder.  Unfortunately Sublime Text doesn't support subfolders so you can only have a single repository in here.

    cd C:\Users\%USERNAME%\AppData\Roaming\Sublime Text 2\Packages\User
    git init
    git remote add origin git://github.com/seanhoughton/SublimePerforce.git
    git pull origin