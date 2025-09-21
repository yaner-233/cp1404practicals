import random

def main():
    population = 1000
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population: {population}")
    for year in range(1, 11):
        born_pct = random.randint(10, 20)
        born = population * born_pct // 100
        died_pct = random.randint(5, 25)
        died = population * died_pct // 100
        population += born - died
        print(f"Year {year}" )
        print()
        print(f"{born} gophers were born. {died} died.")
        print(f"Population: {population}")
    print("Simulation complete.")

if __name__ == "__main__":
    main()