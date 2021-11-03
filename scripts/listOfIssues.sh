#!/bin/bash
# $1 path to file with access info e.g. ./listOfIssues.sh ~/path/filename.txt
cd ..
echo "CHECK! Are you in the pipenv shell?"
cat $1 | xargs python ./atlass/list_of_issues
