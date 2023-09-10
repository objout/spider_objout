# Spider

## Introduction

A spider for Bilibili danmaku and visualizing.

### Preview

![Preview](imgs/preview.jpg)

![Word Cloud](imgs/wordcloud.jpg)

## Tech Stack

- Python 3
- Shell script

## Usage

Prerequisites:
- `wget`
- `bash`
- `python 3`
- `pip3`

```bash
# Run the following commands in your BASH.
mkdir -p $HOME/tmp/spider_venv
cd $HOME/tmp
python3 -m venv spider_venv
source spider_venv/bin/activate

git clone git@github.com:objout/spider_objout.git
cd spider_objout
pip3 install dist/spider_objout-0.0.1.tar.gz

spider_objout

deactivate
rm -rf $HOME/tmp/spider_venv
```
