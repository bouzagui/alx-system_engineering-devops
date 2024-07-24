#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

USER=$1

if id "$USER" &>/dev/null; then
    sudo -u $USER whoami
else
    echo "User $USER does not exist."
    exit 1
fi
