@echo off

title Uploading...
color 0a

git add .
git commit -m "updates"
git push -u origin main

exit
