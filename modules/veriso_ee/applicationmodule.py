# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

from veriso.base.utils.utils import dynamic_import
from veriso.modules.applicationmodule_base import ApplicationModuleBase


class ApplicationModule(ApplicationModuleBase):
    def __init__(self, veriso):
        super(ApplicationModule, self).__init__(veriso)
