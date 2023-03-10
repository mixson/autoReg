class EndPoint:

    assetInventoryMethod = "/inv/listInventory"
    assetInventoryContainerMethod = "/inv/listInventoryContainer"
    assetRegistrationMethod = "/reg/listRegisterHeader"
    assetRegistrationLineMethod = "/reg/listRegisterLine"
    listRfidContainerMethod = "/rfid/listRfidContainer"
    getRfidTagContainerMethod = "/rfid/getRfidTagContainer"
    registerItemsMethod = "/reg/checkInItems"
    registerToItemsMethod = "/to/checkInItems"
    registerToItemsDirectMethod = "/to/newTransferOutLine"
    registerTiItemsMethod = "/ti/checkInItems"
    registerTiItemsDirectMethod = "/ti/newTransferInLine"
    registerContainerMethod = "/reg/checkInContainer"
    registerToContainerMethod = "/to/checkInContainer"
    registerTiContainerMethod = "/ti/checkInContainer"
    registerCompleteMethod = "/reg/registerComplete"
    registerToCompleteMethod = "/to/transferOutComplete"
    registerTiCompleteMethod = "/ti/transferInComplete"
    registerItemsValidationMethod = "/reg/registerItemsValidation"
    registerItemMethod = "/reg/registerItems"
    listTransferOutHeaderMethod = "/to/listTransferOutHeader"
    listTransferOutLineMethod = "/to/listTransferOutLine"
    setSiteCodeMethod = "/site"
    listTransferInHeaderMethod = "/ti/listTransferInHeader"
    listTransferInLineMethod = "/ti/listTransferOutLine"
    assetReturnHeaderMethod = "/assetReturn/listAssetReturnHeader"
    assetReturnItemsMethod = "/assetReturn/checkInItems"
    assetReturnContainerMethod = "/assetReturn/checkInContainer"
    assetReturnCompleteMethod = "/assetReturn/returnComplete"
    assetReturnItemsValidationMethod = "/reg/registerItemsValidation"
    assetReturnRegisterItemsMethod = "/reg/registerItems"
    assetReturnLineMethod = "/assetReturn/listAssetReturnLine"
    listLocSiteMethod = "/loc/listLocSite"
    createDirectToMethod = "/to/newTransferOutHeader"
    createDirectTiMethod = "/ti/newTransferInHeader"
    listStockTakeHeaderMethod = "/stocktake/listStocktakeHeader"
    listStockTakeLineMethod = "/stocktake/listStocktakeLine"
    newStockTakeHeaderMethod = "/stocktake/newStocktakeHeader"
    updateStockTakeHeaderMethod = "/stocktake/updateStocktakeHeader"
    removeStockTakeHeaderMethod = "/stocktake/removeStocktakeHeader"
    stockTakeInitiateMethod = "/stocktake/stocktakeInitiate"
    stockTakeStartMethod = "/stocktake/stocktakeStart"
    stockTakeCheckInItemsMethod = "/stocktake/checkInItems"
    stockTakeCancelMethod = "/stocktake/stocktakeCancel"
    stockTakeHeaderCompleteMethod = "/stocktake/stocktakeComplete"
    stockTakeLineCompleteMethod = "/stocktake/stocktakeLineComplete"
    stocktakeRecountByLocMethod = "/stocktake/stocktakeRecountByLoc"
    listStocktakeLocHeaderMethod = "/stocktake/listStocktakeLocHeader"
    getOrderDetailARMethod = "/reg/getOrderDetail"
    getOrderDetailTIMethod = "/ti/getOrderDetail"
    getOrderDetailTOMethod = "/to/getOrderDetail"
    getOrderDetailAssetReturnMethod = "/assetReturn/getOrderDetail"
    getRfidTagItemMethod = "/rfid/getRfidTagItem"

    assetRegistrationUploadMethod = "/reg/uploadM1"

    genRfidItem = "/reg/genRfidItem"
    listAllPrefixSequence = "/prefix/listPrefixSequence"
    setContainerPrefix = "/prefix"
    genRfidContainer = "/reg/genRfidContainer"
