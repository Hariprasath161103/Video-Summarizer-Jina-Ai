from gtts import gTTS
import os

def text_to_audio(input_file, output_file):
    try:
        # Read text from the Notepad file
        with open(input_file, 'r') as file:
            text = file.read()

        # Create a gTTS object
        tts = gTTS(text, lang='en')
        
        # Save the audio file
        tts.save(output_file)

        print(f"Audio file '{output_file}' created successfully.")

        # Play the audio file
        os.system(f'start {output_file}')

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify the input Notepad file and output audio file
    input_file_path = 'output.txt'  # Change this to your Notepad file
    output_file_path = 'output.mp3'  # Change this to your desired output audio file

    text_to_audio(input_file_path, output_file_path)
