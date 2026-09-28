# -*- coding: utf-8 -*-
"""
Multiple Netherite server system.

Redstone armor grants a small movement speed modifier while equipped.
"""
from __future__ import print_function

import mod.server.extraServerApi as serverApi


CF = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()
ServerSystem = serverApi.GetServerSystemCls()

REDSTONE_ARMOR = [
    "multiple_netherite:netherite_redstone_helmet",
    "multiple_netherite:netherite_redstone_chestplate",
    "multiple_netherite:netherite_redstone_leggings",
    "multiple_netherite:netherite_redstone_boots",
]

SPEED_MODIFIER_ID = "multiple_netherite:redstone_speed"
SPEED_BONUS = 0.05


class MultipleNetheriteServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        engineNs = serverApi.GetEngineNamespace()
        engineSys = serverApi.GetEngineSystemName()
        self.ListenForEvent(engineNs, engineSys, "AddServerPlayerEvent", self, self.OnPlayerJoin)
        self.ListenForEvent(engineNs, engineSys, "DelServerPlayerEvent", self, self.OnPlayerLeave)
        self.ListenForEvent(engineNs, engineSys, "OnNewArmorExchangeServerEvent", self, self.OnArmorExchange)

    def Destroy(self):
        pass

    def OnPlayerJoin(self, args):
        playerId = args.get("id")
        if playerId:
            self.RefreshSpeed(playerId)

    def OnPlayerLeave(self, args):
        playerId = args.get("id")
        if playerId:
            self.RemoveSpeedModifier(playerId)

    def OnArmorExchange(self, args):
        playerId = args.get("playerId")
        if playerId:
            self.RefreshSpeed(playerId)

    def HasRedstoneArmor(self, playerId):
        itemComp = CF.CreateItem(playerId)
        armorItems = itemComp.GetPlayerAllItems(serverApi.GetMinecraftEnum().ItemPosType.ARMOR) or []
        for item in armorItems:
            if item and item.get("itemName") in REDSTONE_ARMOR:
                return True
        return False

    def RemoveSpeedModifier(self, playerId):
        attrComp = CF.CreateAttr(playerId)
        attrComp.RemoveModifier(
            serverApi.GetMinecraftEnum().AttrType.SPEED,
            SPEED_MODIFIER_ID,
        )

    def RefreshSpeed(self, playerId):
        self.RemoveSpeedModifier(playerId)
        if not self.HasRedstoneArmor(playerId):
            return
        attrComp = CF.CreateAttr(playerId)
        attrComp.AddModifier(
            serverApi.GetMinecraftEnum().AttrType.SPEED,
            SPEED_MODIFIER_ID,
            SPEED_BONUS,
            serverApi.GetMinecraftEnum().AttributeModifierOperation.OperationMultiplyBase,
            serverApi.GetMinecraftEnum().AttributeOperands.OperandMax,
        )