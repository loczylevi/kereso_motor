"""
AtomicNumber,Element,Symbol,AtomicMass,NumberofNeutrons,NumberofProtons,NumberofElectrons,Period,Group,Phase,Radioactive,Natural,Metal,Nonmetal,Metalloid,Type,AtomicRadius,Electronegativity,FirstIonization,Density,MeltingPoint,BoilingPoint,NumberOfIsotopes,Discoverer,Year,SpecificHeat,NumberofShells,NumberofValence
1,Hydrogen,H,1.007,0,1,1,1,1,gas,,yes,,yes,,Nonmetal,0.79,2.2,13.5984,8.99E-05,14.175,20.28,3,Cavendish,1766,14.304,1,1
"""

import sqlite3

con = sqlite3.connect(':memory:')

cur = con.cursor()

class Adatbazis:
    def __init__(self,sor):
        AtomicNumber,Element,Symbol,AtomicMass, *felesleg  = sor.strip().split(",")
        self.AtomicNumber = AtomicNumber
        self.Element = Element
        self.Symbol = Symbol
        self.AtomicMass = AtomicMass
        
with open("eu.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    data = [Adatbazis(sor) for sor in f]
cur.execute("DROP TABLE IF EXISTS period")

cur.execute("""CREATE TABLE period
        (AtomicNumber TEXT,
        Element TEXT,
        Symbol TEXT,
        AtomicMass TEXT)
""")
for i in data:
    lista = [(i.AtomicNumber,i.Element,i.Symbol,i.AtomicMass)]
    cur.executemany("INSERT INTO period VALUES (?,?,?,?) ", lista)
    
con.commit()

msg = cur.execute("SELECT * FROM period")

#print(msg.fetchall())

for row in cur.execute("SELECT AtomicNumber,Element,Symbol,AtomicMass FROM period"):
    print(f"rendszám: {row[0]},\t Vegyjel: {row[2]},\t Név: {row[1]},\t Relativ atomtömeg: {row[3]}")

darabszam = cur.execute(" SELECT count() FROM  period ")    
print( f'2. feladat: Elemek száma:{ darabszam.fetchall() } ' )

print("")
bekeres = input("Kérek vegyjelet: ")
bekeres = bekeres.lower().capitalize()

adat = cur.execute(" SELECT * FROM  period WHERE Symbol =? OR AtomicNumber =? OR Element =? OR AtomicMass =?",(bekeres,bekeres,bekeres,bekeres))
    
print(f'3. feladat: A bekért vegyjel: {bekeres} adatai: :{adat.fetchall()} ' )
print(adat.fetchall())

bekeres = input("keresés: ")

#adat = cur.execute(" SELECT * FROM  period WHERE Symbol =?",(bekeres,))

adat = cur.execute(f" SELECT Symbol FROM period WHERE Element LIKE '%{bekeres}%'")


print(f'4. feladat: A bekért vegyjel: {bekeres} adatai: :{adat.fetchall()} ' )

