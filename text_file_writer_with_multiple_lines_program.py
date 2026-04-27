from functionalities_of_text_file_writer_with_multiple_lines import TextFileWriter


def main():
    writer = TextFileWriter()
    if writer.process():
        writer.display_file_content()


if __name__ == "__main__":
    main()
