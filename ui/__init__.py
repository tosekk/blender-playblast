# Copyright 2023 Zhandos Kadyrkulov
# SPDX-License-Identifier: GNU GPLv3

from . import panels
from . import operators


def register_modules():
    operators.register_classes()
    panels.register_classes()


def unregister_modules():
    panels.unregister_classes()
    operators.unregister_classes()