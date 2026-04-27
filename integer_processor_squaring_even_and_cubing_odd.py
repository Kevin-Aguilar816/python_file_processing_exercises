from functionalities_of_the_integer_processor_squaring_even_and_cubing_odd import IntegerProcessor


def main():
    processor = IntegerProcessor()
    if processor.read_integers():
        if processor.classify_and_transform():
            if processor.write_double_file():
                print("Processing completed successfully.")
            else:
                print("Failed to write the output file.")
        else:
            print("Failed to classify and transform integers.")
    else:
        print("Failed to read integers from the file.")


if __name__ == "__main__":
    main()
