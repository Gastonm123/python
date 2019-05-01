nro_piezas = 7

vertices = (
( #palito
    (0, 2, 0),
    (1, 2, 0),
    (1, 1, 0),
    (0, 1, 0),

    (0, 1, 0),
    (1, 1, 0),
    (1, 0, 0),
    (0, 0, 0),

    (0, 0, 0),
    (1, 0, 0),
    (1, -1, 0),
    (0, -1, 0),

    (0, -1, 0),
    (1, -1, 0),
    (1, -2, 0),
    (0, -2, 0),
),
( #s
    (-1, 0, 0),
    (0, 0, 0),
    (0, -1, 0),
    (-1, -1, 0),

    (0, 0, 0),
    (1, 0, 0),
    (1, -1, 0),
    (0, -1, 0),

    (0, 1, 0),
    (1, 1, 0),
    (1, 0, 0),
    (0, 0, 0),

    (1, 1, 0),
    (2, 1, 0),
    (2, 0, 0),
    (1, 0, 0),
),
( #z 
    (-1, 1, 0),
    (0, 1, 0),
    (0, 0, 0),
    (-1, 0, 0),

    (0, 1, 0),
    (1, 1, 0),
    (1, 0, 0),
    (0, 0, 0),

    (0, 0, 0),
    (1, 0, 0),
    (1, -1, 0),
    (0, -1, 0),

    (1, 0, 0),
    (2, 0, 0),
    (2, -1, 0),
    (1, -1, 0)
),
( #cubo
    (0, 1, 0),
    (1, 1, 0),
    (1, 0, 0),
    (0, 0, 0),

    (1, 1, 0),
    (2, 1, 0),
    (2, 0, 0),
    (1, 0, 0),

    (0, 0, 0),
    (1, 0, 0),
    (1, -1, 0),
    (0, -1, 0),

    (1, 0, 0),
    (2, 0, 0),
    (2, -1, 0),
    (1, -1, 0)
),
( #T
    (0, 1, 0),
    (1, 1, 0),
    (1, 0, 0),
    (0, 0, 0),

    (0, 0, 0),
    (1, 0, 0),
    (1, -1, 0),
    (0, -1, 0),

    (1, 0, 0),
    (2, 0, 0),
    (2, -1, 0),
    (1, -1, 0),

    (0, -1, 0),
    (1, -1, 0),
    (1, -2, 0),
    (0, -2, 0)
),
( # l
    (-1, -1, 0),
    (0, -1, 0),
    (0, -2, 0),
    (-1, -2, 0),

    (-1, 0, 0),
    (0, 0, 0),
    (0, -1, 0),
    (-1, -1, 0),

    (0, 0, 0),
    (1, 0, 0),
    (1, -1, 0),
    (0, -1, 0),

    (1, 0, 0),
    (2, 0, 0),
    (2, -1, 0),
    (1, -1, 0)
),
( #j
    (-1, 0, 0),
    (0, 0, 0),
    (0, -1, 0),
    (-1, -1, 0),

    (0, 0, 0),
    (1, 0, 0),
    (1, -1, 0),
    (0, -1, 0),

    (1, 0, 0),
    (2, 0, 0),
    (2, -1, 0),
    (1, -1, 0),

    (1, -1, 0),
    (2, -1, 0),
    (2, -2, 0),
    (1, -2, 0)
)
)

colors = (
    (0, 1, 1),  #palito
    (1, 0, 0),  #s
    (0, 1, 0),    #z
    (1, 1, 0),    #cubo
    (0.5, 0, 1),    #t
    (1, 0.5, 0),    #l
    (1, 0, 0.5)    #j
)