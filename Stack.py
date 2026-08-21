import tkinter as tk
from tkinter import messagebox

# The original class, slightly adapted to interact with the GUI 
# instead of using 'print'.
class GasStation:
    def __init__(self):
        self.line = []

    def arrive(self, vehicle):
        """Add a vehicle to the line."""
        self.line.append(vehicle)

    def fill_up(self):
        """Fill up the first vehicle in line and remove it from the line."""
        if self.line:
            return self.line.pop(0)
        return None

# GUI Class
class GasStationApp:
    def __init__(self, root):
        self.station = GasStation()
        self.root = root
        self.root.title("Gas Station (FIFO)")
        self.root.geometry("350x400")
        self.root.config(padx=20, pady=20)

        # --- UI Elements ---
        
        # Label and entry field for the vehicle
        self.label = tk.Label(root, text="Vehicle name (e.g., Motorcycle 1):")
        self.label.pack(pady=(0, 5))

        self.vehicle_entry = tk.Entry(root, width=30)
        self.vehicle_entry.pack(pady=(0, 15))

        # Arrive button
        self.btn_arrive = tk.Button(root, text="Arrive at the station", command=self.add_vehicle, bg="#4CAF50", fg="white")
        self.btn_arrive.pack(fill=tk.X, pady=5)

        # Fill up button
        self.btn_fill = tk.Button(root, text="Fill up first vehicle", command=self.serve_vehicle, bg="#2196F3", fg="white")
        self.btn_fill.pack(fill=tk.X, pady=5)

        # Label for the current line
        self.label_list = tk.Label(root, text="Current line:")
        self.label_list.pack(pady=(15, 5))

        # Listbox to display the queue
        self.queue_listbox = tk.Listbox(root, height=10, width=40)
        self.queue_listbox.pack()

    def add_vehicle(self):
        vehicle = self.vehicle_entry.get().strip()
        if vehicle:
            self.station.arrive(vehicle)
            self.update_listbox()
            self.vehicle_entry.delete(0, tk.END) # Clear the entry field
        else:
            messagebox.showwarning("Warning", "Please enter a vehicle name.")

    def serve_vehicle(self):
        served_vehicle = self.station.fill_up()
        if served_vehicle:
            messagebox.showinfo("Filling up", f"{served_vehicle} is filling up and will leave the station.")
            self.update_listbox()
        else:
            messagebox.showinfo("Empty", "No vehicles in line to fill up.")

    def update_listbox(self):
        """Update the visual listbox with the current data in the line."""
        self.queue_listbox.delete(0, tk.END) # Clear the current list
        for v in self.station.line:
            self.queue_listbox.insert(tk.END, v)

# Start the application
if __name__ == "__main__":
    window = tk.Tk()
    app = GasStationApp(window)
    window.mainloop()
