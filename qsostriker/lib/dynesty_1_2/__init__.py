#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .dynesty import NestedSampler, DynamicNestedSampler
from . import bounding
from . import utils


__version__ = "1.2 beta"
print("using Dynesty = %s"%__version__)
