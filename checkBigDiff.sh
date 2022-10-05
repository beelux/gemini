#!/usr/bin/env bash
DIFF=$(git diff --numstat)
ADD=$(echo $DIFF | cut -d" " -f1)
DEL=$(echo $DIFF | cut -d" " -f2)

git --no-pager diff

if [[ $ADD > 2 && $DEL < 2 ]]
then
    exit 1
else
    exit 0
fi
