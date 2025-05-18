import tkinter as tk
from tkinter import messagebox
import ipaddress

def ip_to_bin():
    ip = ip_entry.get().strip()
    try:
        ip_obj = ipaddress.IPv4Address(ip)
        binary = ".".join(format(o, '08b') for o in ip_obj.packed)
        result_label.config(text=f"Binaire: {binary}")
    except:
        messagebox.showerror("Erreur", "Adresse IP invalide")

def bin_to_ip():
    binary = ip_entry.get().strip()
    octets = binary.split('.')
    if len(octets) == 4 and all(len(o) == 8 and set(o).issubset({'0', '1'}) for o in octets):
        ip = '.'.join(str(int(o, 2)) for o in octets)
        result_label.config(text=f"IPv4: {ip}")
    else:
        messagebox.showerror("Erreur", "Format binaire invalide")

def ip_to_int():
    ip = ip_entry.get().strip()
    try:
        result_label.config(text=f"Entier: {int(ipaddress.IPv4Address(ip))}")
    except:
        messagebox.showerror("Erreur", "Adresse IP invalide")

def int_to_ip():
    try:
        n = int(ip_entry.get().strip())
        result_label.config(text=f"IPv4: {str(ipaddress.IPv4Address(n))}")
    except:
        messagebox.showerror("Erreur", "Entier invalide")

def netcalc():
    ip = ip_entry.get().strip()
    mask = mask_entry.get().strip()
    try:
        network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
        result_label.config(text=f"Réseau: {network.network_address}\nFirst IP: {network.network_address + 1}\nLast IP: {network.broadcast_address - 1}\nBroadcast: {network.broadcast_address}")
    except:
        messagebox.showerror("Erreur", "IP ou masque invalide")

def calculate_subnet():
    ip = ip_entry.get().strip()
    devices = devices_entry.get().strip()
    if devices.isdigit():
        devices = int(devices)
        for cidr in range(32, 0, -1):
            if (2 ** (32 - cidr)) - 2 >= devices:
                network = ipaddress.IPv4Network(f"{ip}/{cidr}", strict=False)
                result_label.config(text=f"Réseau: {network.network_address}\nMasque: {network.netmask}")
                return
    messagebox.showerror("Erreur", "Nombre d'appareils invalide")

# Interface Tkinter
root = tk.Tk()
root.title("IPv4 Calculator")
root.geometry("400x500")

tk.Label(root, text="Adresse IP ou Binaire").pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

tk.Button(root, text="IP -> Binaire", command=ip_to_bin).pack()
tk.Button(root, text="Binaire -> IP", command=bin_to_ip).pack()
tk.Button(root, text="IP -> Entier", command=ip_to_int).pack()
tk.Button(root, text="Entier -> IP", command=int_to_ip).pack()

tk.Label(root, text="Masque de sous-réseau").pack()
mask_entry = tk.Entry(root)
mask_entry.pack()
tk.Button(root, text="Calcul Réseau", command=netcalc).pack()

tk.Label(root, text="Nombre d'appareils").pack()
devices_entry = tk.Entry(root)
devices_entry.pack()
tk.Button(root, text="Calcul Sous-Réseau", command=calculate_subnet).pack()

result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

tk.Button(root, text="Quitter", command=root.quit).pack()

root.mainloop()
