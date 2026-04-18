import tkinter as tk

data = {
    "🚨EMERGJENCAT KOMBËTARE": [
        ("112", "Emergjenca Unike"),
        ("129", "Policia"),
        ("127", "Ambulanca"),
        ("128", "Zjarrfikësit"),
        ("126", "Policia Rrugore"),
    ],

    "⚡SHËRBIME KOMBËTARE": [
        ("0800 14 14", "OSHEE"),
        ("0800 44 55", "Ujësjellës"),
        ("116", "Info / Telekom"),
    ],

    "🏙️TIRANË": [
        ("04 236 0000", "Bashkia"),
        ("04 237 0000", "QSUT"),
    ],

    "🌊DURRËS": [
        ("052 222 222", "Bashkia"),
        ("052 234 567", "Spitali"),
    ],

    "❄️SHKODËR": [
        ("022 400 000", "Bashkia"),
        ("022 222 111", "Spitali"),
    ],

    "🌿ELBASAN": [
        ("054 400 111", "Bashkia"),
        ("054 222 333", "Spitali"),
    ],

    "🌾FIER": [
        ("034 500 222", "Bashkia"),
        ("034 222 444", "Spitali"),
    ],

    "🌊VLORË": [
        ("033 200 333", "Bashkia"),
        ("033 222 555", "Spitali"),
    ],

    "⛰️KORÇË": [
        ("082 300 444", "Bashkia"),
        ("082 222 666", "Spitali"),
    ],

    "🏛️BERAT": [
        ("032 210 555", "Bashkia"),
        ("032 222 777", "Spitali"),
    ],

    "🌄GJIROKASTËR": [
        ("084 220 666", "Bashkia"),
        ("084 222 888", "Spitali"),
    ],

    "🏔️KUKËS": [
        ("024 200 777", "Bashkia"),
        ("024 222 999", "Spitali"),
    ],

    "🌳LEZHË": [
        ("0215 210 888", "Bashkia"),
        ("0215 222 111", "Spitali"),
    ],

    "⛰️DIBËR": [
        ("0218 220 999", "Bashkia Peshkopi"),
        ("0218 222 222", "Spitali Peshkopi"),
    ],
}


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("📞 Numra Shqipëria")
        self.root.geometry("620x520")
        self.root.configure(bg="#0f172a")

        self.current = list(data.keys())[0]
        self.build_ui()
        self.update_list()

    def build_ui(self):
        # Header
        tk.Label(
            self.root,
            text="📞 NUMRA EMERGJENCE - SHQIPËRI",
            font=("Segoe UI", 18, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            pady=12
        ).pack(fill="x")

        # Dropdown
        self.var = tk.StringVar(value=self.current)
        menu = tk.OptionMenu(self.root, self.var, *data.keys(), command=self.change)
        menu.config(bg="#38bdf8", fg="black", font=("Segoe UI", 11, "bold"), bd=0)
        menu.pack(pady=10)

        # Container
        container = tk.Frame(self.root, bg="#0f172a")
        container.pack(fill="both", expand=True, padx=15, pady=10)

        # Scrollbar
        scroll = tk.Scrollbar(container)
        scroll.pack(side="right", fill="y")

        # Listbox
        self.listbox = tk.Listbox(
            container,
            font=("Segoe UI", 12),
            bg="#1e293b",
            fg="white",
            selectbackground="#38bdf8",
            selectforeground="black",
            bd=0,
            highlightthickness=0,
            yscrollcommand=scroll.set
        )
        self.listbox.pack(fill="both", expand=True)
        scroll.config(command=self.listbox.yview)

        # Footer
        tk.Label(
            self.root,
            text="Made by Darien💙",
            bg="#0f172a",
            fg="#64748b",
            font=("Segoe UI", 9)
        ).pack(pady=5)

    def change(self, value):
        self.current = value
        self.update_list()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for nr, name in data[self.current]:
            self.listbox.insert(tk.END, f"📞 {nr}  •  {name}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    App().run()
