from exercices_heritage import Train, TrainInterCity, FreightTrain

#Le train, on complète le ride avec le temps (heures, minutes, ...).
train = Train(150)
train.ride(3)
print("Le train a parcouru "+str(train.distance)+" kilomètres.")

train.passengers=5
print("Le train a "+str(train.passengers)+" passagers.")

#Le train de villes
ville = TrainInterCity()
ville.ride(3)
print("Le train entre villes a parcouru "+str(train.distance)+" kilomètres.")

ville.passengers = 6
print("Le train entre villes a "+str(ville.passengers)+" passagers.")

print("Le train entre villes a "+str(ville.profit)+" euros de profit.")
#Le train cargo
cargo = FreightTrain()
cargo.ride(3)
print("Le train à cargo a parcouru "+str(train.distance)+" kilomètres.")

cargo.passengers = 3
print("Le train à cargo a "+str(cargo.passengers)+" passagers.")

cargo.cargo = 15
print("Le train à cargo a "+str(cargo.cargo)+" cargos.")
