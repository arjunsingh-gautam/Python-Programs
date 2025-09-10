# <span style="color:orange">Movie Watchlist - OOP-based Project</span>

## <span style="color:pink">Introduction</span>

This project is an **Object-Oriented Programming (OOP)** based implementation of a movie watchlist system. It allows users to **add, remove, and view movies** stored in a dictionary. The project demonstrates the use of **classes, objects, and Python's match-case statement**.

## <span style="color:pink">Features</span>

- Add movies to the watchlist
- Remove movies from the watchlist
- View detailed information about movies
- View only movie names in the watchlist
- Exit the watchlist system

## <span style="color:pink">Project Structure</span>

### <span style="color:yellow">Class: `Movie`</span>

The `Movie` class is used to represent a movie with the following attributes:

- `name` - Name of the movie
- `hero` - Lead actor of the movie
- `heroine` - Lead actress of the movie

**Methods:**

- `__init__(self, name, hero, heroine)`: Initializes the movie details.
- `intro(self)`: Displays the movie's details.

### <span style="color:yellow">Dictionary: `watchlist`</span>

A dictionary is used to store movies where:

- **Keys** → Movie names
- **Values** → `Movie` objects

## <span style="color:pink">User Menu Options</span>

### <span style="color:yellow">1️⃣ Add a Movie to Watchlist</span>

- The user can enter multiple movies.
- Each movie is stored in the `watchlist` dictionary.
- The user is prompted to add more movies or stop.

### <span style="color:yellow">2️⃣ Remove a Movie from Watchlist</span>

- The user enters the movie name to remove it.
- If the movie exists, it is deleted from the `watchlist`.
- The user can continue removing movies or exit this option.

### <span style="color:yellow">3️⃣ View Watchlist Details</span>

- Displays all movies along with their actor and actress names.

### <span style="color:yellow">4️⃣ View Only Movie Names in Watchlist</span>

- Displays only the movie names stored in `watchlist`.

### <span style="color:yellow">5️⃣ Exit the Watchlist</span>

- Exits the program.

## <span style="color:pink">Code Explanation</span>

The program runs in a loop, presenting the user with a menu. Based on the user's input, it executes the corresponding case using the **match-case** statement.

- **Adding a movie** creates a `Movie` object and stores it in `watchlist`.
- **Removing a movie** deletes the movie from the dictionary.
- **Viewing movies** displays their details or only names.
- **Invalid input handling** ensures the user selects a valid option.

## <span style="color:pink">Example Usage</span>

```
Welcome to watchlist...
1. Add a Movie to watchlist
2. Remove a Movie from watchlist
3. View watchlist details
4. View Movie names in watchlist
5. Exit
```

### <span style="color:yellow">Sample Output:</span>

```
Enter Movie Name: Interstellar
Enter Actor Name: Matthew McConaughey
Enter Actress Name: Anne Hathaway
Do you want to add more movies? Yes|No: No
```

### <span style="color:yellow">Viewing Watchlist:</span>

```
My watchlist...
########################################
Movie Name: Interstellar
Actor Name: Matthew McConaughey
Actress Name: Anne Hathaway
```

## <span style="color:pink">Enhancements & Future Improvements</span>

- Add **genre and release year** to each movie.
- Implement **file storage** to save watchlist data permanently.
- Add a **search function** to find movies easily.
- Create a **GUI-based interface** for better user experience.

---

This **Movie Watchlist** project is a great way to practice OOP concepts and dictionary manipulations in Python! 🚀
