import tkinter as tk
 
data = {
    "🚨 EMERGJENCAT KOMBËTARE": [
        ["112", "Emergjenca Unike"],
        ["129", "Policia"],
        ["127", "Ambulanca"],
        ["128", "Zjarrfikësit"],
        ["126", "Policia Rrugore"]
    ],
 
    "⚡ SHËRBIME KOMBËTARE": [
        ["0800 14 14", "OSHEE (Energjia Elektrike)"],
        ["0800 44 55", "Ujësjellës"],
        ["116", "Info / Telekom ndihmë"],
    ],
 
    "🏙️ TIRANË": [
        ["04 236 0000", "Bashkia Tiranë"],
        ["04 237 0000", "QSUT Spitali Kryesor"]
    ],
 
    "🌊 DURRËS": [
        ["052 222 222", "Bashkia Durrës"],
        ["052 234 567", "Spitali Durrës"]
    ],
 
    "❄️ SHKODËR": [
        ["022 400 000", "Bashkia Shkodër"],
        ["022 222 111", "Spitali Shkodër"]
    ],
 
    "🌿 ELBASAN": [
        ["054 400 111", "Bashkia Elbasan"],
        ["054 222 333", "Spitali Elbasan"]
    ],
 
    "🌾 FIER": [
        ["034 500 222", "Bashkia Fier"],
        ["034 222 444", "Spitali Fier"]
    ],
 
    "🌊 VLORË": [
        ["033 200 333", "Bashkia Vlorë"],
        ["033 222 555", "Spitali Vlorë"]
    ],
 
    "⛰️ KORÇË": [
        ["082 300 444", "Bashkia Korçë"],
        ["082 222 666", "Spitali Korçë"]
    ],
 
    "🏛️ BERAT": [
        ["032 210 555", "Bashkia Berat"],
        ["032 222 777", "Spitali Berat"]
    ],
 
    "🌄 GJIROKASTËR": [
        ["084 220 666", "Bashkia Gjirokastër"],
        ["084 222 888", "Spitali Gjirokastër"]
    ],
 
    "🏔️ KUKËS": [
        ["024 200 777", "Bashkia Kukës"],
        ["024 222 999", "Spitali Kukës"]
    ],
 
    "🌳 LEZHË": [
        ["0215 210 888", "Bashkia Lezhë"],
        ["0215 222 111", "Spitali Lezhë"]
    ],
 
    "⛰️ DIBËR": [
        ["0218 220 999", "Bashkia Peshkopi"],
        ["0218 222 222", "Spitali Peshkopi"]
    ]
}
 
 
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("📞 Numra Shqipëria")
        self.root.geometry("650x520")
        self.root.configure(bg="#0f172a")  # 🔵 background modern
 
        self.kat = list(data.keys())[0]
 
        self.gui()
 
    def gui(self):
        # 🔷 HEADER
        header = tk.Label(
            self.root,
            text="📞 NUMRA EMERGJENCE - SHQIPËRI",
            font=("Arial", 18, "bold"),
            bg="#1e3a8a",
            fg="white",
            pady=10
        )
        header.pack(fill="x")
 
        # 🔀 DROPDOWN
        self.var = tk.StringVar()
        self.var.set(self.kat)
 
        menu = tk.OptionMenu(self.root, self.var, *data.keys(), command=self.change_city)
        menu.config(bg="#38bdf8", fg="black", font=("Arial", 11, "bold"))
        menu.pack(pady=10)
 
        # 📜 FRAME + SCROLLBAR
        frame = tk.Frame(self.root, bg="#0f172a")
        frame.pack(fill="both", expand=True, padx=15, pady=10)
 
        self.scroll = tk.Scrollbar(frame)
        self.scroll.pack(side="right", fill="y")
 
        self.lista = tk.Listbox(
            frame,
            font=("Arial", 12),
            yscrollcommand=self.scroll.set,
            bg="#1e293b",
            fg="white",
            selectbackground="#38bdf8",
            selectforeground="black"
        )
        self.lista.pack(side="left", fill="both", expand=True)
 
        self.scroll.config(command=self.lista.yview)
 
        self.shfaq()
 
    def change_city(self, value):
        self.kat = value
        self.shfaq()
 
    def shfaq(self):
        self.lista.delete(0, tk.END)
 
        for nr, emri in data[self.kat]:
            self.lista.insert(tk.END, f"📞 {nr} - {emri}")
 
    def run(self):
        self.root.mainloop()
 
 
App().run()