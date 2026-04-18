🔹 1. Importimi
import tkinter as tk

👉 Këtu po marrim një mjet që quhet Tkinter

💡 Çfarë bën?

Na lejon të krijojmë një dritare (app) në kompjuter 🪟
Si të bësh një program që duket si lojë ose aplikacion
🔹 2. Krijimi i klasës
class App:

👉 Kjo është si truri i programit 🧠

💡 Pse përdoret?

Brenda saj vendoset gjithë logjika e aplikacionit
🔹 3. Funksioni fillestar
def __init__(self):

👉 Ky funksion ndizet automatikisht kur hapet programi

💡 Si “butoni i ndezjes” 🔘

🔹 4. Krijimi i dritares
self.root = tk.Tk()

👉 Krijon dritaren kryesore 🪟

self.root.title("📞 Numra Shqipëria")

👉 Vendos emrin sipër dritares (titullin)

self.root.geometry("620x520")

👉 Vendos madhësinë e dritares 📏

self.root.configure(bg="#0f172a")

👉 Vendos ngjyrën e sfondit 🎨

🔹 5. Zgjedhja e parë
self.current = list(data.keys())[0]

👉 Merr kategorinë e parë nga lista

💡 Si me hap automatikisht “Emergjencat”

🔹 6. Ndërtimi i UI
self.build()

👉 Krijon pamjen e programit (butonat, lista, etj.)

🔹 7. Shfaqja e të dhënave
self.update()

👉 Tregon numrat në ekran 📞

🔹 8. Ndërtimi i ekranit
def build(self):

👉 Këtu ndërtohet pamja e aplikacionit

🟦 Titulli
tk.Label(self.root, text="📞 NUMRA EMERGJENCE - SHQIPËRI",

👉 Krijon tekstin e madh sipër ekranit

💡 Si titull i një libri 📖

🔽 Menu (zgjedhja e kategorisë)
self.var = tk.StringVar(value=self.current)

👉 Ruan çfarë kategorie është zgjedhur

tk.OptionMenu(self.root, self.var, *data, command=self.change)

👉 Krijon një menu ku zgjedh qytetin/kategorinë

💡 Si listë zgjedhjeje 🎯

📦 Kuti për listën
box = tk.Frame(self.root)

👉 Krijon një kuti ku futet lista

📜 Scroll (rrëshqitje)
scroll = tk.Scrollbar(box)

👉 Krijon shiritin për të lëvizur poshtë/lart

📋 Lista e numrave
self.listbox = tk.Listbox(...)

👉 Këtu shfaqen numrat dhe emrat 📞

scroll.config(command=self.listbox.yview)

👉 Lidh scroll me listën

🔹 9. Kur ndryshon zgjedhja
def change(self, val):

👉 Kur zgjedh një kategori tjetër

self.current = val

👉 Ruan zgjedhjen e re

self.update()

👉 Rifreskon listën 🔄

🔹 10. Shfaqja e numrave
def update(self):

👉 Kjo e mbush listën me të dhëna

self.listbox.delete(0, tk.END)

👉 Fshin të dhënat e vjetra 🧹

for nr, name in data[self.current]:

👉 Merr çdo numër nga kategoria e zgjedhur

self.listbox.insert(tk.END, f"📞 {nr} • {name}")

👉 I shton në ekran 📞

🔹 11. Nisja e programit
def run(self):
    self.root.mainloop()

👉 E mban programin hapur (që mos mbyllet)

🔹 12. Startimi
if __name__ == "__main__":

👉 Kontrollon që po e hapim direkt programin

App().run()

👉 E nis aplikacionin 🚀
