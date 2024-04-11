import math

def additive_dilution(starting_volume: int|float,
                        dilutor_names: list[str],
                        initial_concentrations: list[float],
                        final_concentrations: list[float]):
    '''
    Given a starting solution (x), some number of dilutors (y_n), their respective initial concentrations (y_c), and desired final concentrations (y_f), calculate the required volumes of dilutors (y_v) to add to the starting solution (x).
    '''
    n = len(final_concentrations)
    p = [math.prod(final_concentrations[j] if j == i else initial_concentrations[j] for j in range(n)) for i in range(n)] 
    q = math.prod(initial_concentrations) - sum(p)

    sol = [starting_volume * p[i] / q for i in range(n)]
    print('Total volume:', round(sum(sol) + starting_volume, 2))
    print(*[k + ' : ' + str(round(v, 2)) for k,v in zip(dilutor_names, sol)], sep = '\n') 
    return(sol)

if __name__ == '__main__':
    # add arguments here
    # all volumes & concentrations should be in the same units
    ## volume of media
    starting_volume = 500
    ## names of dilutants
    dilutor_names = [
        'sodium_pyruvate', 
        'bovine_insulin', 
        'l_glutamine'
        ]
    ## initial concentrations of dilutants 
    initial_concs = [200, 100, 100]
    ## final concentrations of dilutants
    final_concs = [5, 2, 1]

    additive_dilution(starting_volume=starting_volume,
                      dilutor_names=dilutor_names,
                      initial_concentrations=initial_concs,
                      final_concentrations=final_concs)

