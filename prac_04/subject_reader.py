def load_subject_data(filename):
    """Read subject data from file and return as list of lists."""
    data = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])  # Convert student count to integer
            data.append(parts)
    return data


def display_subject_details(subject_data):
    """Display all subject details in formatted output."""
    for subject in subject_data:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


def main():
    """Main function to load and display subject data."""
    subject_data = load_subject_data('subject_data.txt')
    display_subject_details(subject_data)


main()