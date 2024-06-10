#!/usr/bin/env bash

choice=$(printf "us\nru\naz" | rofi -dmenu)
case "$choice" in
  us) sh setxkbmap us ;;
  ru) sh setxkbmap ru ;;
  az) sh setxkbmap az ;;
esac
