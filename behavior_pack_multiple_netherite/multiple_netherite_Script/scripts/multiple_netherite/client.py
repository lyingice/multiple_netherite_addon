# -*- coding: utf-8 -*-
"""
Multiple Netherite client system.
"""
from __future__ import print_function

import mod.client.extraClientApi as clientApi


ClientSystem = clientApi.GetClientSystemCls()


class MultipleNetheriteClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)

    def Destroy(self):
        pass