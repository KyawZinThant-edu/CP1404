def main():
    text = input("Text: ")
    words = text.split()

    # Count occurrences
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Find the longest word for alignment
    max_length = max(len(word) for word in word_counts)

    # Display sorted word counts
    for word in sorted(word_counts):
        print(f"{word:{max_length}} : {word_counts[word]}")

main()
