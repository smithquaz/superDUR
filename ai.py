# implements the AI system based on the different requirements

from assets.logic import *

def populate_kb(current_drugs, new_drugs, not_included, ddis, medical_conditons, biconditionals):
    
    # create empty kb
    kb = And()

    yes = [current_drugs, new_drugs]
    for categories in yes:
        for drugs in categories:

            # create object then add into kb
            kb.add(Symbol(drugs))

    # populate kb with all the DDIs, Medical Conditions and new drugs (prove by contradiction)
    nots = [not_included, ddis, medical_conditons]
    for categories in nots:
        for drugs in categories:
            
            # create a not object add add into kb
            kb.add(Not(Symbol(drugs)))

    # # populate the kb with all biconditionals
    for pairs in biconditionals:
        
        left = list(pairs)[0]
        right = list(pairs)[1]

        if len(left) > 1:
            symbol_left = Symbol(list(left)[0])
            symbol_right = Symbol(list(left)[1])
            left_logic = Or(symbol_left, symbol_right)

        else:
            left_logic = Symbol(list(pairs)[0])

        if len(right) > 1:
            symbol_left = Symbol(list(right)[0])
            symbol_right = Symbol(list(right)[1])
            right_logic = Or(symbol_left, symbol_right)

        else: 
            right_logic = Symbol(list(pairs)[1])

        # create a logical symbol to represent this relationship
        logic = Biconditional(left_logic, right_logic)

        # add logic to kb
        kb.add(logic)

    return kb

# checks if the kb has reached conjunctive normal form
def is_cnf(kb):

    for symbol in kb.conjuncts:

        # print(f'testing: {symbol}')
        
        if symbol.__class__ == Not: 
            if not symbol.operand.__class__ == Symbol:
                return False
        
        elif not symbol.__class__ == Symbol and not symbol.__class__ == Or:
            return False
    
    return True

# apply the de morgan's laws
def de_morgan(kb, symbol):

    if symbol.operand.__class__ == And:

        # ~(a ^ b) => ~a v ~b
        alpha = Not(symbol.operand.conjuncts[0])
        beta = Not(symbol.operand.conjuncts[1])
        logic = Or(alpha, beta)

        # update kb
        kb.remove(symbol)
        kb.add(logic)
    
    elif symbol.operand.__class__ == Or:

        # ~(a v b) => ~a ^ ~b
        alpha = Not(symbol.operand.disjuncts[0])
        beta = Not(symbol.operand.disjuncts[1])
        logic = Or(alpha, beta)

        # update kb
        kb.remove(symbol)
        kb.add(logic)

    elif symbol.operand.__class__ == Not:

        # ~(~a) => a
        logic = symbol.operand.operand
        kb.remove(symbol)
        kb.add(logic)

    return kb

# converts the KB into conjunctive normal form
def convert_to_cnf(kb):

    while True:
    
        # break condition
        if is_cnf(kb):
            return kb
        
        for symbol in kb.conjuncts:
            
            # clear biconditionals
            if symbol.__class__  == Biconditional:
                
                # break biconditional into 2 implications and add into kb
                first = Implication(symbol.left, symbol.right)
                second = Implication(symbol.right, symbol.left)
                
                # update kb
                kb.remove(symbol)
                kb.add(first)
                kb.add(second)
                break

            # clear implication
            elif symbol.__class__ == Implication: 

                # ~a -> b => ~~a v b => a v b
                if symbol.antecedent.__class__ == Not:
                    logic = Or(symbol.antecedent.operand, symbol.consequent)
                
                # a -> b => ~a v b
                else:
                    logic = Or(Not(symbol.antecedent), symbol.consequent)
                
                # update kb
                kb.remove(symbol)
                kb.add(logic)
                break

            # applying De Morgan's Laws
            elif symbol.__class__ == Not:
                
                new_kb = de_morgan(kb, symbol)
                if not new_kb == kb:
                    kb = new_kb
                        

# determine if there is a match between the first and the second
def match(first, second):

    # determine which is the or statement
    if first.__class__ == Or: 
        or_statement = first

    elif second.__class__ == Or:
        or_statement = second

    # case where there is no or
    else:
        return False
    
    # or statement is first
    if or_statement == first:
    
        # positive case
        if second.__class__ == Symbol:

            # find this symbol in second
            for symbol in first.disjuncts:
                if second == symbol or Not(second) == symbol:
                    return True

        elif second.__class__ == Not:

            # find this symbol in second
            for symbol in first.disjuncts: 
                if second == symbol or second == Not(symbol):
                    return True

    # or statement is second
    if or_statement == second:

        # positive case
        if first.__class__ == Symbol:

            # find this symbol in second
            for symbol in second.disjuncts:
                if first == symbol or Not(first) == symbol:
                    return True

        elif first.__class__ == Not:

            # find this symbol in second
            for symbol in second.disjuncts: 
                if first == symbol or first == Not(symbol):
                    return True

    return False


# determine if there is an or statement to resolve
def contradiction(kb):
    
    resolved = False
    while not resolved:
    
        resolved = True

        # iterate over kb, looking to resolve or statements
        symbols = kb.conjuncts
        for i in range(len(symbols)):
                
            for j in range(i + 1, len(symbols)):

                # direct contradiction
                if symbols[j] == Not(symbols[i]) or Not(symbols[j]) == symbols[i]:
                    return True

                # or statement to resolve (update kb)
                elif match(symbols[i], symbols[j]):
                    
                    if symbols[i].__class__ == Or:
                        left = symbols[i].disjuncts[0]
                        right = symbols[i].disjuncts[1]
                        symbol = symbols[j]
                    else:
                        left = symbols[j].disjuncts[0]
                        right = symbols[j].disjuncts[1]
                        symbol = symbols[i]

                    # print(f'left: {left}, right: {right}, symbol: {symbol}')
                    # print(f'current kb: {kb.formula()}')
                    
                    # direct match (p ^ (p v q) => p ^ ~q)
                    if left == symbols[i]:
                        # print(f'direct right added: {right}')
                        if right.__class__ == Not: 
                            kb.add(right.operand)
                        else:
                            kb.add(Not(right))

                    elif right == symbols[i]:
                        # print(f'direct left added: {left}')
                        if left.__class__ == Not: 
                            kb.add(left.operand)
                        else:
                            kb.add(Not(left))
                    
                    # indirect match (p ^ (~p v q) => q)
                    elif Not(left) == symbol or Not(symbol) == left:
                        # print(f'indirect right added: {right}')
                        kb.add(right)

                    elif Not(right) == symbol or Not(symbol) == right:
                        # print(f'indirect left added: {left}')
                        kb.add(left)

                    # remove the or statement
                    if symbols[i].__class__ == Or:
                        kb.remove(symbols[i])
                    else:
                        kb.remove(symbols[j])

                    resolved = False
                    print(f'    updated kb: {kb.formula()}')
                    break

            if not resolved: 
                break
            
    return False

# give a few parameters, determine if the doctor can safely prescribe the drug
def is_safe(current_drugs, new_drugs, not_included, ddis, medical_conditons, biconditionals):
    
    # populate a knowledge base using all the parameters
    kb = populate_kb(current_drugs, new_drugs, not_included, ddis, medical_conditons, biconditionals)
    print(f'    original kb: {kb.formula()}')

    # convert the kb to conjunctive normal form
    kb = convert_to_cnf(kb)
    print(f'    cnf kb: {kb.formula()}')
    
    # resolve the knowledge base using resolution rules
    if (not contradiction(kb)):
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
    current_drugs = {'A', 'B'}
    new_drugs = {'C'}
    not_included = {'D'}
    ddi = {'A', 'D'}
    medical_condition = {}
    biconditionals = {}

    if is_safe(current_drugs, new_drugs, not_included, ddi, medical_condition, biconditionals):
        print('Test 1 Failed')
    else:
        print('Test 1 Passed')

    # scenario 1b: Conflict between DDI and Current Drugs
    '''
        Current Drugs: A, B
        New Drug: C
        Relevant DDI: D
        Medical Condition: None
        Biconditionals: None
    '''
    current_drugs = {'A', 'B'}
    new_drugs = {'C'}
    not_included = {'D'}
    ddi = {'D'}
    medical_condition = {}
    biconditionals = {}

    if is_safe(current_drugs, new_drugs, not_included, ddi, medical_condition, biconditionals):
        print('Test 1b Passed')
    else:
        print('Test 1b Failed')


    # scenario 2: Doctor forgot to prescribe certain drugs together (biconditional)
    '''
        Current Drugs: A, B
        New Drug: C
        Relevant DDI: None
        Medical Condition: E
        Biconditionals: A <=> E
    '''
    current_drugs = {'A'}
    new_drugs = {'B'}
    not_included = {'C'}
    ddi = {}
    medical_condition = {}
    biconditionals = {frozenset(['B', 'C'])}

    if is_safe(current_drugs, new_drugs, not_included, ddi, medical_condition, biconditionals):
        print('Test 2 Failed')
    else:
        print('Test 2 Passed')

    # scenario 3: Very complicated 
    '''
        Current Drugs: A, B
        New Drug: C
        Relevant DDI: G, H
        Medical Condition: E
        Biconditionals: C <=> B v H
    '''
    current_drugs = {'A', 'B'}
    new_drugs = {'C'}
    not_included = {'D'}
    ddi = {}
    medical_condition = {'E'}
    biconditionals = {frozenset(['C', frozenset(['B', 'H'])])}

    if is_safe(current_drugs, new_drugs, not_included, ddi, medical_condition, biconditionals):
        print('Test 3 Passed')
    else:
        print('Test 3 Failed')


if __name__ == "__main__":
    main()
