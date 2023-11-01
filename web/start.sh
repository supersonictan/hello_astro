#!/bin/bash
#
# Copyright (c) 2017 Tencent Inc. All Rights Reserved
#
# File: stop.sh
# Author: jackietan@tencent.com
# Date: 2023/11/01 23:11:34
# Brief: 

conda activate astro
nohup python run_web.py 80 stdout.log 2>&1 &
