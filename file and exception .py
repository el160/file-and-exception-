import os

def process_file_content(content):
    """
    Modify the file content: Add line numbers and reverse each line for demonstration.
    """
    return "\n".join(
        f"{idx:03}: {line[::-1]}" for idx, line in enumerate(content.splitlines(), start=1)
    )

def get_valid_filename(prompt):
    """
    Prompt the user for a valid filename until a valid one is provided.
    Handles file existence and readability checks.
    """
    while True:
        filename = input(prompt).strip()
        if not filename:
            print("[!] Filename cannot be empty. Please try again.")
            continue

        if not os.path.isfile(filename):
            print(f"[!] File '{filename}' does not exist. Try again.")
            continue

        if not os.access(filename, os.R_OK):
            print(f"[!] File '{filename}' cannot be read. Check permissions and try again.")
            continue

        return filename

def get_output_filename(prompt):
    """
    Prompt the user for an output filename. Warn if the file already exists.
    """
    while True:
        filename = input(prompt).strip()
        if not filename:
            print("[!] Filename cannot be empty. Please try again.")
            continue

        if os.path.isfile(filename):
            overwrite = input(f"[!] File '{filename}' already exists. Overwrite? (y/n): ").strip().lower()
            if overwrite != 'y':
                print("[!] Provide a new filename.")
                continue

        return filename

def main():
    print("\n=== Professional File Processor ===")
    print("This tool will read a file, modify its content, and save it to a new file.\n")

    # Step 1: Get valid input filename
    input_file = get_valid_filename("Enter the path to the file you want to process: ")

    # Step 2: Read file content
    try:
        with open(input_file, 'r') as infile:
            original_content = infile.read()
    except Exception as e:
        print(f"[!] Unexpected error while reading the file: {e}")
        return

    # Step 3: Process file content
    modified_content = process_file_content(original_content)

    # Step 4: Get valid output filename
    output_file = get_output_filename("Enter the path for the modified file to save: ")

    # Step 5: Write the modified content to a new file
    try:
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        print(f"\n[✔] Modified file saved successfully at: {output_file}")
    except Exception as e:
        print(f"[!] Unexpected error while writing to the file: {e}")
        return

    # Final Step: Display summary
    print("\n=== Summary ===")
    print(f"Original File: {input_file}")
    print(f"Modified File: {output_file}")
    print("\nThank you for using the File Processor. Have a great day!")

if __name__ == "__main__":
    main()
