📞 Numra Emergjence - Shqipëri (Tkinter App)
🧠 Përshkrimi
 
Ky projekt është një aplikacion desktop i ndërtuar me Python dhe Tkinter, që funksionon si një libër telefonik për numra emergjence dhe shërbime në Shqipëri.
 
Aplikacioni lejon përdoruesin të zgjedhë një qark dhe të shohë menjëherë numrat përkatës të emergjencës dhe institucioneve kryesore.
 
🎯 Qëllimi
 
Ky projekt është krijuar për:
 
Praktikë me Tkinter (GUI development)
Kuptimin e event-driven programming
Organizimin e kodit me OOP (Class-based structure)
Ndërtimin e një aplikacioni real dhe të dobishëm
⚙️ Funksionalitetet
🪟 GUI
Ndërfaqe grafike me Tkinter
Dizajn modern (dark mode)
Layout i thjeshtë dhe i pastër
🔀 Zgjedhja e qytetit
Dropdown (OptionMenu) me 12 qarqet:
Tiranë
Durrës
Shkodër
Elbasan
Fier
Vlorë
Korçë
Berat
Gjirokastër
Kukës
Lezhë
Dibër
Përditësim automatik i listës kur ndryshon qyteti
📜 Lista e numrave
Listbox për shfaqjen e të dhënave
Scrollbar për navigim
 
Format:
 
[Numri] - [Shërbimi]
🚨 Numrat Kombëtarë
112 – Emergjenca Unike
129 – Policia
127 – Ambulanca
128 – Zjarrfikësit
126 – Policia Rrugore
🔧 Shërbime Kombëtare
0800 14 14 – OSHEE
0800 44 55 – Ujësjellës
116 – Info / Telekom
🏙️ Të Dhënat për Qarqet
 
Për çdo qark përfshihen:
 
Policia
Ambulanca
Zjarrfikësit
Bashkia
Spitali kryesor
 
📌 Shënim: Numrat lokalë mund të jenë placeholder ose të personalizohen.
 
🎨 Dizajni
Background: #1e1e2f
Tekst: i bardhë (#ffffff)
Accent: blu (#4da6ff)
Highlight për elementët e selektuar
🧠 Struktura e Kodit
 
Aplikacioni përdor OOP:
 
class EmergencyApp
create_ui() → ndërton GUI
update_numbers(city) → përditëson listën
Event handling për dropdown
mainloop() për nisjen e aplikacionit
▶️ Si ta përdorësh
Sigurohu që ke Python të instaluar (3.x)
Shkarko ose klono projektin
Ekzekuto file-in kryesor:
python main.py
🚀 Ide për përmirësim
🔍 Search për numra
📱 Simulim “Call”
💾 Ruajtje e të dhënave në file (JSON)
🎨 Tema të ndryshme (light/dark toggle)
🌐 Integrim me API reale
📁 Strukturë e Sugjeruar
project/
│── main.py
│── data.py
│── ui.py
│── README.md
🧩 Teknologjitë
Python
Tkinter
📌 Statusi
 
✅ Funksional (basic version)
🔧 Open për përmirësime
 
👨‍💻 Autor
 
Projekt për praktikë dhe mësim në GUI development me Python.
