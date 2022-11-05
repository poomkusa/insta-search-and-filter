#!/bin/bash

instaloader <KEYWORD> --count=100 --post-metadata-txt="{caption}new_tabhttps://instagram.com/p/{shortcode}" --no-pictures --no-videos --no-video-thumbnails --no-metadata-json
instaloader <KEYWORD> --count=580 --post-metadata-txt="{caption}new_tabhttps://instagram.com/p/{shortcode}" --no-pictures --no-videos --no-video-thumbnails --no-metadata-json

python /home/poom/Desktop/insta/json_to_xlsx.py

xargs google-chrome --new-tab < urls.txt &

echo "Auto-remove generated files? Select 1 or 2"
select yn in "Yes" "No"; do
    case $yn in
        Yes) 
            rm -r /home/poom/Desktop/insta/<KEYWORD>
            rm -r /home/poom/Desktop/insta/<KEYWORD>
            rm /home/poom/Desktop/insta/urls.txt
            rm /home/poom/Desktop/insta/full.csv
            rm /home/poom/Desktop/insta/filtered.csv
            break;;
        No) exit;;
    esac
done
