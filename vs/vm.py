def main():
    def brute_force_string_matching(text, pattern):
        
        n = len(text)
        m = len(pattern)
        occurrences = []

        for i in range(n - m + 1):
            j = 0
            while j < m and text[i + j] == pattern[j]:
                j += 1
            if j == m:
                occurrences.append(i)

        return occurrences

    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search for: ")
    matches = brute_force_string_matching(text, pattern)
    if matches:
        print("Pattern found at indices:", matches)
    else:
        print("Pattern not found in the text.")

if __name__ == "__main__":
    main()
  