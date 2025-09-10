# In this project we will write an OOP based to create a watch list
class Movie:
    def __init__(self,name,hero,heroine):
        self.name=name
        self.hero=hero
        self.heroine=heroine
    def intro(self):
        print("Movie Name:",self.name)
        print("Actor Name:",self.hero)
        print("Actress Name:",self.heroine)

watchlist={}

while True:
    print("Welcome to watchlist...")
    option1=int(input("Enter 1 to Add a Movie to watchlist\nEnter 2 to Remove a Movie from watchlist\nEnter 3 to view watchlist details\nEnter 4 to view Movie name in watch list\nEnter 5 to exit\n"))
    match option1:
        case 1:
            while True:
                name=input("Enter Movie Name:")
                hero=input("Enter Actor Name:")
                heroine=input("Enter Actress Name:")
                m=Movie(name,hero,heroine)
                watchlist[name]=m
                option2=input("Do you want to add more movies Yes|No:")
                if option2.lower()=='no':
                    break
        case 2:
            while True:
                name=input("Enter movie Name you want to remove:")
                del watchlist[name]
                option2=input("Do you want to remove more movies Yes|No:")
                if option2.lower()=='no':
                    break
        case 3:
            print("My watchlist...")
            print('#'*40)
            for movie in watchlist.values():
                movie.intro()
                print()
        case 4:
            print("Movie List...")
            print('-'*40)
            for movies in watchlist.keys():
                print(movies)
                print()
        case 5:
            print("Exiting Movie List...")
            break
        case _:
            print("Enter correct option")



