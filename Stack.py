"At a gas station,"
" you form a line to fill up,"
" whether it's a motorcycle or a car."
" The first to fill up is the first to leave,"
" and the last to fill up is the last to leave."

class gas_station:
    
    def __init__(self):
        self.line = []

    def arrive(self, vehicle):
        """Add a vehicle to the line."""
        self.line.append(vehicle)
        print(f"{vehicle} has arrived at the gas station.")

    def fill_up(self):
        """Fill up the first vehicle in line and remove it from the line."""
        if self.line:
            vehicle = self.line.pop(0)
            print(f"{vehicle} is filling up and will leave the gas station.")
        else:
            print("No vehicles in line to fill up.")

    def current_line(self):
        """Display the current line of vehicles."""
        if self.line:
            print("Current line of vehicles:")
            for vehicle in self.line:
                print(vehicle)
        else:
            print("The line is currently empty.")
            # Instanciamos nuestra gasolinera
gas_station = gas_station()

print("--- LLEGADA DE VEHÍCULOS ---")
gas_station.arrive("Moto 1")
gas_station.arrive("Carro 1")
gas_station.arrive("Moto 2")

print("\n--- REVISANDO LA FILA ---")
gas_station.current_line()

print("\n--- ATENDIENDO ---")
gas_station.fill_up()  # Atiende a Moto 1
gas_station.fill_up()  # Atiende a Carro 1

print("\n--- FILA ACTUALIZADA ---")
gas_station.current_line()