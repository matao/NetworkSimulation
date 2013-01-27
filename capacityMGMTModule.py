import re
from CapacityClass import *

class CapacityTable:
    capacityTable = []

    def __init__(self, links, capacity):
        for i in range(len(links)):
            cap = Capacity(links[i][0], capacity, links[i][1])
            self.capacityTable.append(cap)


    def capacityTableUpdate(self, results, secondLevelFlag, linkReList,
                            id, currentDemands):
        for i in range(len(results[0])):
            print results[0][i] + ": " + results[1][i]
            #Check to see if the results are greater than 0
            if float(results[1][i]) > float(0) and secondLevelFlag is False:
                #Grabs each line of information from the capacity table
                for lists in self.capacityTable:
                    #Search for the index value
                    try:
                        index = lists[2].index(results[0][i])
                    except:
                        index = -1
                    #If it has that value
                    if index is not -1:
                        addList = []
                        #Subtract the results from capacity
                        lists[1] = float(lists[1]) - float(results[1][i])
                        addList.append(lists[0])
                        addList.append(results[0][i])
                        addList.append(results[1][i])
                        linkReList.append(addList)
        pathRe = re.compile("x\d+")

        for d in currentDemands:
            print d
            demandP = d.demandPathId + 1
            for i in range(len(linkReList)):
                if len(linkReList[i]) < 4:
                    match = pathRe.search(linkReList[i][1])
                    thePath = match.group()
                    if str(thePath).strip() == str("x" + str(demandP)).strip():
                        linkReList[i].append(d[3])
                        linkReList[i].append(id)
                        id = id + 1

    def restoreCapacity(self, removeList):
        for line in removeList:
            for i in range(len(self.capacityTable)):
                if line[0] == self.capacityTable[i][0]:
                    self.capacityTable[i][1] = (float(self.capacityTable[i][1])
                                                + float(line[2]))
    
    def printCapList(self):
        print self.capacityTable
        for caps in self.capacityTable:
            caps.printCap()
