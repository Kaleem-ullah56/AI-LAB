movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# Allowing user to add more movies
more_movies = input("Do you want to add more movies? (yes/no): ").strip().lower()
if more_movies == "yes":
    n = int(input("How many movies do you want to add? "))
    for i in range(n):
        name = input(f"Enter the name of movie {i+1}: ")
        budget = int(input(f"Enter the budget of '{name}': "))
        movies.append((name, budget))

# Calculation of the average budget
total_budget = sum(budget for _, budget in movies)
average_budget = total_budget / len(movies)
print(f"\nAverage movie budget: ${average_budget:,.2f}\n")

# Find and print movies with budget higher than average
high_budget_movies = []
for movie, budget in movies:
    if budget > average_budget:
        c = budget - average_budget
        high_budget_movies.append(movie)
        print(f"'{movie}' has a budget ${budget:,.2f}, which is ${c:,.2f} above average.")

# Print the count of movies above average
print(f"\nNumber of movies with budget above average: {len(high_budget_movies)}")