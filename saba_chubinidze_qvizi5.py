class Ticket:
    def __init__(self, filmis_dasaxeleba, biletis_fasi, biletebis_raodenoba, ena="Geo"):
        self.filmis_dasaxeleba = filmis_dasaxeleba
        self.biletis_fasi = biletis_fasi
        self.biletebis_raodenoba = biletebis_raodenoba
        self.ena = ena
    def __str__(self):
        return f"filmi - {self.filmis_dasaxeleba}, filmi - {self.biletis_fasi}, raodenoba - {self.biletebis_raodenoba}, ena - {self.ena}"


    def __gt__(self, other):
        if isinstance(other, Ticket):
            print(f"{other.filmis_dasaxeleba} > {self.filmis_dasaxeleba}")
        elif isinstance(Ticket, other):
            print(f"{self.filmis_dasaxeleba} > {other.filmis_dasaxeleba}")
        return ""

    def __lt__(self, ricxvi):
        self.ricxvi = ricxvi
        if self.biletebis_raodenoba < self.ricxvi:
            print(f"{self.biletis_fasi} > {self.ricxvi}")
        elif 10 < self.biletebis_raodenoba:
            print(f"{self.biletis_fasi} < {self.ricxvi}")
        else:
            print(f"{self.biletis_fasi} = {self.ricxvi}")
        return ""

#####################################################################################---------------

class User:
    def __init__(self, user_name, fuli):
        self.user_name = user_name
        self.fuli = fuli



    def __str__(self):
        return f"saxeli - {self.user_name}, tanxis raodenoba - {self.fuli}"

    def deposit(self, tanxis_raodenoba):
        self.fuli += tanxis_raodenoba
        return ""


    def biletis_shedzena(self, raodenoba, biletis_fasi, biletebis_raodenoba):
        self.raodenoba = raodenoba
        self.biletis_fasi = biletis_fasi
        self.biletebis_raodenoba = biletebis_raodenoba
        self.jamuri_fasi = self.raodenoba * self.biletis_fasi

        if  self.jamuri_fasi < self.fuli and self.raodenoba >= self.biletebis_raodenoba:
            print("ver sheidzent ")
        else:
            self.fuli -= self.raodenoba * self.biletis_fasi
            self.biletebis_raodenoba -= self.raodenoba
            print(f"tqven sheidzinet {self.raodenoba} bileti")
        return ""



filmi1 = Ticket("avatari 3", 5, 15)
filmi2 = Ticket("scream 7", 10, 3)
user = User ("kaci", 20)
user.deposit(5)
user.biletis_shedzena(2, filmi1.biletis_fasi, filmi1.biletebis_raodenoba)
print(filmi1)
print(filmi1 > filmi2)
print(filmi1 < 10)
