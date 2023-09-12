#!/bin/bash

USER_AGENT='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.54'
REFERER='https://www.baidu.com'
TARGET='https://www.bilibili.com'

wget --user-agent="$USER_AGENT" \
  --referer="$REFERER" \
  -O /dev/null \
  --save-cookies "$1" \
  --quiet \
  --spider \
  "$TARGET"
