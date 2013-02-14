import cplex



def cplexCapacity(model, network, coef, capacityTable):
    for i in range(len(network.capacity)):
        for j in range(len(network.capacity[i][1])):
            coef.append(1.0)
        addConstraint(model, network.capacity[i][1], coef,
                      "link{0}".format(network.capacity[i][0]),
                      capacityTable.capacityTable[i].capacity, "L")
        #Making the coeficient list empty for the next Equation                
        coef = []

def addConstraint(model, varList, coefList, constrName, trhs, operator):
    eq = cplex.SparsePair(ind = varList, val = coefList)
    model.linear_constraints.add(names = [constrName], lin_expr = [eq],
                                 rhs = [trhs], senses = [operator])

def addUpDemands(currentDemands, Paths):
    PathDemands = []
    demand = 0
    for i in range(len(Paths)):
        for j in range(len(currentDemands)):
            if currentDemands[j].demandPathId == i:
                demand = demand + currentDemands[j].demand
        PathDemands.append(demand)
        demand = 0
    return PathDemands

def setStream(model, name_for_logs):
    model.set_log_stream(name_for_logs + ".log")
    model.set_error_stream(name_for_logs + ".err")
    model.set_results_stream(name_for_logs + ".res")