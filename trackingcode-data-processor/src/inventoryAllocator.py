
# created only the inventoryallocator class to not deviate from the instructions
# i would also create fruit and warehouse classes if possible


class inventoryAllocator:

    def __init__(self, items, warehouse):
        self.items = items
        self.warehouse = warehouse
        self.results = []

    def main(self):
        listofItemsUnfulfilled = []
        canShipAllItems = True
        if not self.items or not self.warehouse:
            print("Either the items list or warehouse lis is empty. Or BOTH. Please fix!")
            return []
        self.mainFunctionality()
        listofUnfulfilled, canShipAllItems = self.unfulfilledItems(listofItemsUnfulfilled, canShipAllItems) # still need to traverse through array and append any common warehouses and their items 
        if not canShipAllItems:
            print("Here is the list of inventory that can be shipped", self.results)
            print("Not enough inventory for these items" ,listofItemsUnfulfilled)
            return []
        return self.results

    def mainFunctionality(self):
        for itemName in self.items:                                                                         # traverse through item object by item name
            for warehouseName in self.warehouse:                                                            # traverse through warehouse list (we have name and inventory in every object)
                if self.items[itemName] == 0:                                                               # cuts run time but doesnt change time complexity
                    continue
                if itemName in warehouseName['inventory'] and warehouseName['inventory'][itemName] != 0:
                    res = {}                                                                                # creates nested dictionary {warehouse name: {itemName: quantity}} that is then appended to arr. 
                    if warehouseName['inventory'][itemName] >= self.items[itemName]: 
                        res = self.wareHouseInventoryUse(res, warehouseName['name'], itemName, self.items[itemName])
                        warehouseName['inventory'][itemName] -= self.items[itemName]                        # decreases item count
                        self.items[itemName] = 0                                                            # sets item inventory count to 0 
                    else:
                        res = self.wareHouseInventoryUse(res, warehouseName['name'], itemName, warehouseName['inventory'][itemName])
                        self.items[itemName] -= warehouseName['inventory'][itemName]
                    self.results.append(res)                                                                # does not need to return anything since it updates the attribute directly

    def wareHouseInventoryUse(self, results, warehouse, itemName, inventoryUsed):
        results[warehouse] = {itemName: inventoryUsed}
        return results 

    def unfulfilledItems(self, listofItemsUnfulfilled, canShipAllItems):
        for itemName in self.items:
            if self.items[itemName] != 0:
                canShipAllItems = False
                listofItemsUnfulfilled.append({itemName: self.items[itemName]})
        return listofItemsUnfulfilled, canShipAllItems

