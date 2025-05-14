def count_string_length(input_string):
    print(len(input_string))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Count the length of an input string.')
    parser.add_argument('input_string', type=str, help='The string to count the length of')
    args = parser.parse_args()

    # Call the function with the parsed argument
    count_string_length(args.input_string)