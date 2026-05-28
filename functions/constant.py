# This is constant file, where you are going to find the transformation about the variables

## The firts transformation, where the information is constant, will be in the categorical variables.
## In this case, all the categorical variables have 3 levels, so there is not another one.

# === From categorical format to numeric ===
transform_cat_to_numeric = {
    'Bajo' : 0,
    'Medio' : 1,
    'Alto' : 2
}

# === From numerical format to categorical === 
transform_num_to_cat = {
    0 : 'Bajo',
    1 : 'Medio',
    2 : 'Alto'
}