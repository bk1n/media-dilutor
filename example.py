from mediadilutor import additive_dilution

# all volumes & concentrations should be in the same units

## volume of media
starting_volume = 500

## names of diluents
dilutor_names = [
    'sodium_pyruvate', 
    'bovine_insulin', 
    'l_glutamine'
    ]

## initial concentrations of diluents 
initial_concs = [200, 100, 100]

## final concentrations of diluents
final_concs = [5, 2, 1]

# run additive dilution
additive_dilution(starting_volume=starting_volume,
                    dilutor_names=dilutor_names,
                    initial_concentrations=initial_concs,
                    final_concentrations=final_concs)

