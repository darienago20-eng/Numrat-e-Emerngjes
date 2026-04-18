# 📞 Numra Emergjence - Shqipëri

Ky është një aplikacion i thjeshtë i ndërtuar me Python dhe Tkinter që shfaq numrat më të rëndësishëm të emergjencës dhe shërbimeve në Shqipëri.

---

## 🧠 Çfarë bën ky program?

Ky program krijon një dritare (GUI) ku përdoruesi mund të:

- Zgjedhë një qytet ose kategori 📍
- Shikojë numrat e emergjencës dhe shërbimeve 📞
- Lëvizë në listë me scroll 📜

---

## 🛠️ Teknologjitë e përdorura

- Python 🐍  
- Tkinter (për krijimin e dritares grafike) 🪟  

---

## 🧩 Si funksionon programi?

### 🧠 Klasa kryesore
Programi përdor një klasë të quajtur `App`, e cila përmban gjithë logjikën e aplikacionit.

---

### 🪟 Dritarja kryesore
Kur programi nis:
- Krijohet një dritare me Tkinter
- Vendoset titulli “📞 Numra Shqipëria”
- Vendoset madhësia dhe ngjyra e sfondit

---

### 📍 Zgjedhja e kategorisë
Përdoruesi mund të zgjedhë një kategori si:
- Emergjenca kombëtare 🚨
- Tiranë 🏙️
- Durrës 🌊
- etj.

---

### 📞 Lista e numrave
Pasi zgjidhet kategoria:
- Shfaqen numrat dhe emrat e shërbimeve
- Lista përditësohet automatikisht

---

### 🔄 Ndryshimi i të dhënave
Kur ndryshohet kategoria:
- Lista pastrohet 🧹
- Shfaqen të dhënat e reja 📋

---

## 🚀 Si ta nisësh programin

```bash
python app.py
