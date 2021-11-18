#!/bin/bash
# $1 path to file with access info e.g. ./atlassianAPIClient.sh ~/path/filename.conf
cd ..
echo "CHECK! Are you in the pipenv shell?"
# pipenv shell
python atlassian_lab/atlassian_api_client $1
