#!/usr/bin/env bash
for setting in settings settings1 settings2
do
    echo ""
    echo $setting
    ./dynamic_settings.py $setting
done

