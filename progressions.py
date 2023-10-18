# -*- coding: utf-8 -*-
from typing import Tuple

import requests
from enum import Enum
from bs4 import BeautifulSoup
from util import Aspect, Star, House
from util import *
from util import marriage_trace_dict

def test():
    logger.debug('test haaaaaaaaaaaaaaaaa')

    report.set_msg('A', 'a', 'a1')
    report.set_msg('A', 'a', 'a12')
    report.set_msg('A', 'aa', 'a2')
    report.set_msg('A', 'aa', 'a3')
    report.set_msg('B', 'b', 'b1')
    report.set_msg('B', 'bb', 'b2')
    print(report)