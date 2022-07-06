import json
with open("Tolkapiyam.json", 'r') as f:
    b = json.loads(f.read())


class Tolkapiyam:
 
    def load(self):
        for i in range(len(b)):
            adhigaramname = b[i]['adhigaram']
            iyal = []
            for j in range(len(b[i]['iyal'])):
                iyalname = b[i]['iyal'][j]['iyal_name']
                noorpa = []
                for k in range(len(b[i]['iyal'][j]['noorpa'])):
                    paadal = b[i]['iyal'][j]['noorpa'][k]['paadal']
                    vilakam = b[i]['iyal'][j]['noorpa'][k]['vilakkam']
                    n = Noorpa(paadal, vilakam)
                    noorpa.append(n)
                iy = Iyal(iyalname,noorpa)
                iyal.append(iy)
            a = Adhigaram(adhigaramname, iyal)
            self.adhigaram.append(a)
            
    def getadhigaram(self):
        return [i.name for i in self.adhigaram]
    
    def getiyals(self, number):
        return [iyal.name for iyal in self.adhigaram[number].iyals]
    
    def __init__(self):
        self.adhigaram = []
        self.load()


class Adhigaram:
    def __init__(self, name, iyals):
        self.iyals = iyals
        self.name = name


class Iyal:
    def __init__(self, name, noorpa):
        self.noorpa = noorpa
        self.name = name


class Noorpa:
     def __init__(self, paadal, vilakkam):
        self.paadal = paadal
        self.vilakkam = vilakkam


if __name__ == "__main__":
    t = Tolkapiyam()
    print(t.getadhigaram())
    

