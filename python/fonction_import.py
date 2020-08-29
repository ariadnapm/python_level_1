import mymodule
var = mymodule.MYCONSTANT

#ou seulement importer une seule variable
from mymodule import MYCONSTANT
var = MYCONSTANT

#ou importer plusieurs morceaux d'un même module
from mymodule import MYCONSTANT, myvariable, myfunction