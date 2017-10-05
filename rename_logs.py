#!/usr/bin/env python
# This script renames the CamHD log files. Pass as the first command-line
# argument the fully-qualified path to a top-level directory containing the
# files to rename. For example:
#
# ./rename_logs.py /home/tjc/research/ooi/mirror/rawdata.oceanobservatories.org/files/RS03ASHS/PN03B/06-CAMHDA301
#
# Or, move this script into the top level directory containing the files to
# rename and run it with a dot as the argument. For example:
#
# ./rename_log_files.py .
#
# This has been tested only on Python 3.6.2 but it should work on 2.7. This will
# not work in any Windows environment. This prgram WILL NOT DO ANYTHING AS IS.
# Uncomment the last line after testing this program to actually do a file copy.
#
# Tim Crone (tjcrone@gmail.com)

# imports
import os, sys
import datetime
from subprocess import call

# check input argument
if len(sys.argv) != 2:
    print("Please pass the name of a directory that contains the files to rename.")
    raise SystemExit
root_directory = sys.argv[1]

# loop though files in directory
for root, dirs, files in os.walk(root_directory, topdown=True):
    for name in files:
        if "log" in name:
            if "camhda301_" in name:
                # parse time
                year = int("20%s" % name[10:12])
                month = int(name[12:14])
                day = int(name[14:16])
                hour = int(name[17:19])
                minute = int(name[19:21])
                date = datetime.date(year, month, day)

                # set timestamp based on date (add 'Z' before 2016/11/22)
                if date > datetime.date(2016, 11, 21):
                    timestamp = ('%i%02.0f%02.0fT%02.0f%02.0f00' % (year, month,
                        day, hour, minute))
                else:
                    timestamp = ('%i%02.0f%02.0fT%02.0f%02.0f00Z' % (year, month,
                        day, hour, minute))

                # define new name
                new_name = 'CAMHDA301-%s.log' % timestamp

                # print what we are going to do
                print('copying:\n%s to\n%s\n' % (os.path.join(root, name), os.path.join(root, new_name)))

                # actually copy the file to a new name UNCOMMENT THIS LINE AFTER TESTING
                #call(["cp", "-a", os.path.join(root, name), os.path.join(root, new_name)])
