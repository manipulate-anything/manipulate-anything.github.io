#!/usr/bin/env bash

tasks=("close_box"
       "open_jar"
       "pick_up_cup"
       "put_knife"
       "lamp_on"
       "open_wine"
       "play_jenga"
       "sort_mustard"
       "open_box"
       "pick_and_lift"
       "put_block"
       "take_umbrella")

for task in "${tasks[@]}"
do
    ffmpeg -i ${task}.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k ${task}_fixed.mp4
    rm ${task}.mp4
    mv ${task}_fixed.mp4 ${task}.mp4
done
