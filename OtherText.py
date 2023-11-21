from googletrans import Translator

def translate_text(input_file, output_file, target_language='en'):
    try:
        # Read text from the Notepad file
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Create a Translator object
        translator = Translator()

        # Translate the text to the specified language
        translated_text = translator.translate(text, dest=target_language).text

        # Save the translated text to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translated_text)

        print(f"Translation to {target_language} completed. Translated text saved to '{output_file}'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify the input Notepad file, output file, and target language
    input_file_path = 'output.txt'  # Change this to your Notepad file
    output_file_path = 'frenchoutput.txt'  # Change this to your desired output file
    target_language = 'fr'  # Change this to your desired target language code

    translate_text(input_file_path, output_file_path, target_language)
