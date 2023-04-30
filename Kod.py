# Zadanie 1
class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def correct_time(self):
        if self.hour >= 0 and self.hour < 24 and self.minute >= 0 and self.minute < 60:
            is_correct=True
        else:
            is_correct=False
        return is_correct

    def __add__(self, other):
        sum_hours = self.hour + other.hour
        sum_minutes = self.minute + other.minute

        if sum_minutes >= 60:
            sum_minutes = sum_minutes - 60
            sum_hours = sum_hours + 1

        if sum_hours >= 24:
            sum_hours = sum_hours - 24

        hour = Time(sum_hours, sum_minutes)
        return hour

    def __lt__(self, other):
        return (self.hour, self.minute) > (other.hour, other.minute)

t1 = Time(13, 8)
t2 = Time(20, 50)
t3 = Time(27, 30)

print(t1.correct_time())
print(t2.correct_time())
print(t3.correct_time())
print(t1 + t2)

time = [t1,t2,t3]
print(time)
time.sort()
print(time)

### Zadanie 2
from operator import attrgetter, itemgetter

class Movie:
    def __init__(self, title, year, mark):
        self.title = title
        self.year = year
        self.mark = mark

    def __repr__(self):
        return f"{self.title} {self.year} {self.mark}"

    def __lt__(self, other):
         #sortowanie od najkrótszego tytułu
         #return len(self.title) < len(other.title)

        # sortowanie od najstarszego
        #return self.year < other.year

        # sortowanie po ocenach filmu - od najwyższej do najniższej
        #return self.mark > other.mark

        # sortowanie od najmłodszych filmów i po tytułach - odwrotnie niż alfabet
        return  (self.year,self.title) > (other.year, other.title)

movies = [Movie("Skazani na Shawshank", 1994, 8.76), Movie("Nietykalni", 2011, 8.61), Movie("Zielona mila", 1999, 8.60),
          Movie("Ojciec chrzestny", 1972, 8.59), Movie("Dwunastu gniewnych ludzi", 1957, 8.20),
          Movie("Forrest Gump", 1994, 8.52), Movie("Władca Pierścieni: Powrót króla", 2003, 8.83), Movie("Lista Schindlera", 1993, 8.34),
          Movie("Siedem", 1995, 8.27), Movie("Władca Pierścieni: Dwie wieże", 2002, 8.86)]
# oryginalna kolejnosc
print(movies)

# sortowanie z wykorzystaniem funkcji attrgetter - alfabetycznie po tytule i od najstarszych
movies.sort(key=attrgetter('title', 'year'))
print(movies)

movies.sort()
print(movies)

# Zadanie 3
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x} {self.y}"

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([a + b for a, b in zip(self.x, other.x)],[a + b for a, b in zip(self.y, other.y)])
        if type(other) == tuple:
            return Vector2D([a + other[0] for a in self.x],[a + other[1] for a in self.y])
        return NotImplemented

    def __radd__(self, other):
        if type(other) == tuple:
            return Vector2D([a + other[0] for a in self.x],[a + other[1] for a in self.y])
        return NotImplemented

v1 = Vector2D([1, 2, 3],[1,2,3])
v2 = Vector2D([2, 4, 6],[3,5,7])

v3=v1+v2
print(v3)

v4= v1 + (2,4)
print(v4)

v5 = (21,24) + v1
print(v5)

# Zadanie 4
import numpy as np

class Polynomial:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"{np.poly1d(self.x)}"

    def __setitem__(self, degree, data):
        self.x[len(self.x) - degree - 1] = data

    def __getitem__(self, degree):
        return self.x[len(self.x) - degree-1]

    def __add__(self, other):
        if isinstance(other, Polynomial):
            return Polynomial([a + b for a, b in zip(self.x, other.x)])
        if type(other) in (int,float):
            adding_scalar=np.zeros(len(self.x))
            adding_scalar[-1]=other
            return Polynomial([a + b for a,b in zip(self.x,adding_scalar)])
        return NotImplemented

    def __radd__(self, other):
        if type(other) in (int, float):
            adding_scalar = np.zeros(len(self.x))
            adding_scalar[-1] = other
            return Polynomial([a + b for a, b in zip(self.x, adding_scalar)])
        return NotImplemented



v1 = Polynomial([1, 2, 3])
v2 = Polynomial([2, 4])
print(v1)
print(v2)

# dodawanie wielomianów
v3=v1+v2
print(v3)

v4= v1 + (2)
print(v4)

v5 = (21) + v1
print(v5)

# getitem - zwraca współczynnik wielomianu przy podanym stopniu
print(v1[1])

# setitem - ustawia współczynnik wielomianu przy podanym stopniu
v1[0]=90
print(v1)


#Zadanie 5
import numpy as np
class Playlist:
    def __init__(self, title,number_on_list):
        self.title=title
        self.number_on_list = number_on_list

    def __repr__(self):
        return f"{self.number_on_list} {self.title}"

    def __getitem__(self, number):
         return self.title[self.number_on_list.index(number)]

    def __add__(self, other):
        if isinstance(other, Playlist):
            return Playlist(self.title+other.title,list(np.arange(1, len(self.title)+len(self.title), 1)))
        if type(other) == list:
            return Playlist(self.title + other,list(np.arange(1, len(self.title)+2, 1)))
        return NotImplemented

    def __radd__(self, other):
        if type(other) == list:
            return Playlist(self.title + other,list(np.arange(1, len(self.title)+2, 1)))
        return NotImplemented



playlista1 = Playlist(['Gossip','Miracle','Trustfall'],[1,2,3])
playlista2 = Playlist(['Herbata z imbirem','Lottery'],[1,2])

print(playlista1)
print(playlista2)

# dodawanie playlist
playlista3=playlista1+playlista2
print(playlista3)

playlista4= playlista3 + ['Eyes Closed']
print(playlista4)

playlista5=  ['Lay Low'] + playlista4
print(playlista5)

# getitem zwraca tytuł utworu który na liście ma zadany numer
print(playlista5[4])
