import math

def additive_dilution(starting_volume: int|float,
                        dilutor_names: list[str],
                        initial_concentrations: list[float],
                        final_concentrations: list[float],
                        verbose: bool = True):
    '''
    Given a starting solution (m), some number of dilutors (d), their respective initial concentrations (d_ci), and desired final concentrations (d_cf), calculate the required volumes of dilutors to add to the starting solution (m).

    Parameters:
    - starting_volume (int|float): The volume of the starting solution.
    - dilutor_names (list[str]): A list of names of the dilutors.
    - initial_concentrations (list[float]): A list of initial concentrations of the dilutors. The order of the concentrations should match the order of the dilutor names.
    - final_concentrations (list[float]): A list of desired final concentrations of the dilutors. The order of the concentrations should match the order of the dilutor names.
    - verbose (bool, optional): If set to True, the function will print the total volume and the volumes of each dilutor. Default is True.

    Returns:
    - list[float]: A list of volumes of dilutors to be added to the starting solution. The order of the volumes matches the order of the dilutor names.

    Example:
    ```python
    additive_dilution(100, ['dilutor1', 'dilutor2'], [0.1, 0.2], [0.05, 0.1], True)
    ```
    This will calculate the volumes of 'dilutor1' and 'dilutor2' to be added to a 100 unit starting solution to achieve final concentrations of 0.05 and 0.1 respectively. The initial concentrations of 'dilutor1' and 'dilutor2' are 0.1 and 0.2 respectively.
    '''
    n = len(final_concentrations)
    p = [math.prod(final_concentrations[j] if j == i else initial_concentrations[j] for j in range(n)) for i in range(n)] 
    q = math.prod(initial_concentrations) - sum(p)

    sol = [starting_volume * p[i] / q for i in range(n)]

    if verbose:
        print('Total volume:', round(sum(sol) + starting_volume, 2))
        print(*[k + ' : ' + str(round(v, 2)) for k,v in zip(dilutor_names, sol)], sep = '\n') 
    
    return(sol)