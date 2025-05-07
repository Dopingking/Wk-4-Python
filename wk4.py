def modify_content(content):
    """
    Modify the content of the file.
    In this example, we'll convert all text to uppercase.
    """
    return content.upper()


def main():
    try:
        # Prompt user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_content(content)

        # Define output filename
        output_filename = f"modified_{input_filename}"

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"\n✅ File has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print("\n❌ Error: The specified file does not exist.")
    except IOError:
        print("\n❌ Error: There was a problem reading or writing the file.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
