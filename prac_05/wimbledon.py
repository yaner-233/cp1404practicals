"""
Word Occurrences
Estimate: 35 minutes
Actual:   40 minutes
"""
def read_wimbledon_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(',')
            data.append([parts[0], parts[1], parts[2]])
    return data


def count_wins(champions_data):
    champion_wins = {}
    for times in champions_data:
        champion = times[2]
        if champion in champion_wins:
            champion_wins[champion] += 1
        else:
            champion_wins[champion] = 1
    return champion_wins


def get_sorted_countries(champions_data):
    countries = set()
    for times in champions_data:
        countries.add(times[1])
    return sorted(countries)


def main():
    wimbledon_data = read_wimbledon_data("wimbledon.csv")

    champion_wins = count_wins(wimbledon_data)

    sorted_countries = get_sorted_countries(wimbledon_data)


    print("Wimbledon Champions:")
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


if __name__ == "__main__":
    main()
