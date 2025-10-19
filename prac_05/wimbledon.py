def read_wimbledon_data(filename):
    """Read Wimbledon data from CSV file and return as list of lists"""
    data = []
    try:
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            # Skip header row
            header = in_file.readline()

            for line in in_file:
                # Remove any trailing newline characters and split by comma
                row = line.strip().split(',')
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    return data


def count_championships(data):
    """Count how many times each champion has won"""
    champion_counts = {}

    for row in data:
        try:
            champion = row[2]  # Champion name is in the 3rd column
            champion_counts[champion] += 1
        except KeyError:
            # Champion not in dictionary yet
            champion_counts[champion] = 1
        except IndexError:
            # Row doesn't have enough columns
            continue

    return champion_counts


def get_champion_countries(data):
    """Get unique countries of champions in alphabetical order"""
    countries = set()

    for row in data:
        try:
            country = row[1]  # Champion's country is in the 2nd column
            countries.add(country)
        except IndexError:
            # Row doesn't have enough columns
            continue

    return sorted(countries)


def display_results(champion_counts, countries):
    """Display the processed information"""
    print("Wimbledon Champions: ")
    for champion, count in champion_counts.items():
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))


def main():
    """Main function to orchestrate the data processing"""
    filename = "wimbledon.csv"

    try:
        # Read and process the data
        data = read_wimbledon_data(filename)

        if not data:
            print("No data to process.")
            return

        champion_counts = count_championships(data)
        countries = get_champion_countries(data)

        # Display results
        display_results(champion_counts, countries)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()