#!/usr/bin/env bash

# Define the list of languages to cycle through
LANGUAGES=("en" "ru" "az")

# Get the current keyboard layout
CURRENT_LANG=$(setxkbmap -query | awk -F : '/layout/ {print $2}' | sed 's/ //g')

# Initialize a flag to indicate if the current language was found
found=false

# Loop through the languages
for ((i = 0; i < ${#LANGUAGES[@]}; i++)); do
  if [[ "${LANGUAGES[$i]}" == "$CURRENT_LANG" ]]; then
    # Set the next language in the list, or loop back to the first language
    NEXT_LANG=${LANGUAGES[$(( (i + 1) % ${#LANGUAGES[@]} ))]}
    setxkbmap "$NEXT_LANG"
    notify-send "Lang: $NEXT_LANG" -t 700
    found=true
    break
  fi
done

# If the current language was not found in the list, set to the first language
if [ "$found" = false ]; then
  NEXT_LANG=${LANGUAGES[0]}
  setxkbmap "$NEXT_LANG"
  notify-send "Lang: $NEXT_LANG" -t 700
fi

#polybar-msg action "#ipc_keyboard_status.hook.0"