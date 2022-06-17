#!/bin/bash

START_DATE=$(date +%Y-%m-%d)
END_DATE=$(date -d "-4 days" +%Y-%m-%d)

instalooter hashtag <KEYWORD> /home/poom/Desktop/insta/json -n 200 --time $START_DATE:$END_DATE -D
instalooter hashtag <KEYWORD> /home/poom/Desktop/insta/json -n 200 --time $START_DATE:$END_DATE -D

python /home/poom/Desktop/insta/json_to_xlsx.py

xargs google-chrome --new-tab < urls.txt

echo "Auto-remove generated files? Select 1 or 2"
select yn in "Yes" "No"; do
    case $yn in
        Yes) 
            rm /home/poom/Desktop/insta/json
            rm /home/poom/Desktop/insta/url.txt
            rm /home/poom/Desktop/insta/full.csv
            rm /home/poom/Desktop/insta/filtered.csv
            break;;
        No) exit;;
    esac
done
