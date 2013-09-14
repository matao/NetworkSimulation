import cplex
from cplexSimModule import *

class LoadBalancingModel:
    def __init__(self, network, path_demand, capacity_table):
        #Convert Equation to LB
        self.network = network
        self.network.coef = []
        for i in range(len(self.network.equation)):
            self.network.coef.append(0)
        self.network.coef.append(1)
        self.network.equation.append("Z")
        print self.network.equation
        print self.network.coef
        for i in range(len(self.network.capacity)):
            self.network.capacity[i][1].append("Z")
        print self.network.capacity
        print self.network.demandeq

        #Create the model
        self.model = cplex.Cplex()
        #Give it a name
        self.model.set_problem_name("Topo1")
        #Setting it as minimiztion problem
        self.model.objective.set_sense(1)
        #Give Cplex the minimization equation
        self.model.variables.add(names = network.equation, obj = network.coef)
        #Give Cplex the demand equations
        coef = []
        #cplexDemandLB(self.model, network, coef, path_demand)
        for i in range(len(self.network.demandeq)):
            for j in range(len(self.network.demandeq[i])):
                coef.append(1.0)
            addConstraint(self.model, self.network.demandeq[i], coef,
                          "demand{0}".format(i+1), path_demand[i], "E")
                #Making the coeficient list empty for the next equation
            coef = []
        #Give Cplex the capacity equations
        coef = []
        #cplexCapacity(self.model, network, coef, capacity_table)
        for i in range(len(self.network.capacity)):
            for j in range(len(self.network.capacity[i][1])):
                if self.network.capacity[i][1][j] == "Z":
                    coef.append(- 1 * capacity_table.capacity_table[i].capacity)
                else:
                    coef.append(1.0)
            addConstraint(self.model, self.network.capacity[i][1], coef,
                          "link{0}".format(self.network.capacity[i][0]), 0, "L")
            #Making the coeficient list empty for the next Equation
            coef = []
        #
        addConstraint(self.model, ["Z"], [1], "ZCont", 1, "L")
    def solve(self, outputFile, dynamic, overbooking, capacity, overBookingValue, time):
        self.model.get_problem_type()
        model.write("LP/" + outputFile + str(dynamic) + "-" + str(overbooking) +
                    "-" + str(capacity) + "-" +str(overBookingValue) + "-" +
                    str(time) +".lp", filetype="lp")
        solutions = []
        try:
            solutions = model.solution.get_values()
            results = printResults(network, solutions, fout)
            break
        except cplex.exceptions.CplexSolverError:




