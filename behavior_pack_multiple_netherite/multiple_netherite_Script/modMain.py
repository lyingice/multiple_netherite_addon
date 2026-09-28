# -*- coding: utf-8 -*-
"""
Multiple Netherite Mod
"""
from __future__ import print_function

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi


@Mod.Binding(name="multiple_netherite_Script", version="1.0.0")
class MultipleNetherite(object):
    def __init__(self):
        pass

    @Mod.InitServer()
    def initServer(self):
        serverApi.RegisterSystem(
            "multiple_netherite",
            "server",
            "multiple_netherite_Script.scripts.multiple_netherite.server.MultipleNetheriteServerSystem",
        )

    @Mod.DestroyServer()
    def destroyServer(self):
        pass

    @Mod.InitClient()
    def initClient(self):
        clientApi.RegisterSystem(
            "multiple_netherite",
            "client",
            "multiple_netherite_Script.scripts.multiple_netherite.client.MultipleNetheriteClientSystem",
        )

    @Mod.DestroyClient()
    def destroyClient(self):
        pass
