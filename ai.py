# implements the AI system based on the different requirements

# scenario 3: Overcomplicated: MC + DDI (or in context)

from assets.logic import *

def populate_kb(current_drugs, new_drugs, ddis, medical_conditons, biconditionals):
    
    # create empty kb
    kb = And()

    for drugs in current_drugs:

        # create object then add into kb
        kb.add(Symbol(drugs))

    # populate kb with all the DDIs, Medical Conditions and new drugs (prove by contradiction)
    nots = [new_drugs, ddis, medical_conditons]
    for categories in nots:
        for drugs in categories:
            
            # create a not object add add into kb
            kb.add(Not(Symbol(drugs)))

    # # populate the kb with all biconditionals
    for pairs in biconditionals:
        
        # create a logical symbol to represent this relationship
        left = Symbol(list(pairs)[0])
        right = Symbol(list(pairs)[1])
        logic = Biconditional(left, right)

        # add logic to kb
        kb.add(logic)

    return kb

# converts the KB into Conjunctive Normal Form
def resolution(kb):

    print('in resolution')
    for symbol in kb.conjuncts:
        print(symbol)
        
        # clear biconditionals
        if symbol.__class__  == Biconditional:
            
            # break biconditional into 2 implications and add into kb
            first = Implication(symbol.left, symbol.right)
            second = Implication(symbol.right, symbol.left)
            
            # update kb
            kb.remove(symbol)
            kb.add(first)
            kb.add(second)

        # clear implication
        elif symbol.__class__ == Implication: 

            # a -> b == ~a v b
            logic = Or(Not(symbol.antecedent), symbol.consequent)
            
            # update kb
            kb.remove(symbol)
            kb.add(logic)

        # applying De Morgan's Laws
        elif symbol.__class__ == Not:

            if symbol.operand.__class__ == And:

                # ~(a ^ b) == ~a v ~b
                alpha = Not(symbol.operand.conjuncts[0])
                beta = Not(symbol.operand.conjuncts[1])
                logic = Or(alpha, beta)

                # update kb
                kb.remove(symbol)
                kb.add(logic)

            
            elif symbol.operand.__class__ == Or:

                # ~(a v b) == ~a ^ ~b
                alpha = Not(symbol.operand.conjuncts[0])
                beta = Not(symbol.operand.conjuncts[1])
                logic = Or(alpha, beta)

                # update kb
                kb.remove(symbol)
                kb.add(logic)

            



    print(kb.formula())
        

    return True


# give a few parameters, determine if the doctor can safely prescribe the drug
def is_safe(current_drugs, new_drugs, ddis, medical_conditons, biconditionals):
    
    # populate a knowledge base using all the parameters
    kb = populate_kb(current_drugs, new_drugs, ddis, medical_conditons, biconditionals)
    print(kb.formula())
    print(kb)
    
    # resolve the knowledge base using resolution rules
    if (resolution(kb)):
        return True
    else:
        return False


def main():
    
    # scenario 1: Conflict between DDI and Current Drugs
    '''
        Current Drugs: A, B
        New Drug: C
        Relevant DDI: A, D
        Medical Condition: None
        Biconditionals: None
    '''
    current_drugs = {'A', 'B', 'C', 'D'}
    new_drugs = {'C'}
    ddi = {'A', 'D'}
    medical_condition = {}
    biconditionals = {frozenset(['A', 'B']), frozenset(['C', 'D'])}

    if is_safe(current_drugs, new_drugs, ddi, medical_condition, biconditionals):
        print('Test 1 Failed')
    else:
        print('Test 1 Passed')


    # scenario 2: Doctor forgot to prescribe certain drugs together (biconditional)
    '''
        Current Drugs: A, B
        New Drug: E
        Relevant DDI: A, D
        Medical Condition: None
        Biconditionals: E <=> F
    '''
    current_drugs = {'A', 'B', 'C', 'D'}
    new_drugs = {'C'}
    ddi = {'A', 'D'}
    medical_condition = {}
    biconditionals = {frozenset(['E', 'F'])}

    if is_safe(current_drugs, new_drugs, ddi, medical_condition, biconditionals):
        print('Test 1 Failed')
    else:
        print('Test 1 Passed')


if __name__ == "__main__":
    main()
