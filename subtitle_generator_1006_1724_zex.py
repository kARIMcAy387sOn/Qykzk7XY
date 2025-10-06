# 代码生成时间: 2025-10-06 17:24:55
import pandas as pd


class SubtitleGenerator:
    """
    A class used to generate subtitles from a text file.
    The subtitles are created by dividing the text into sentences and each sentence is a subtitle.
    """
    def __init__(self, text_file_path):
        """
        Initialize the SubtitleGenerator with a text file path.
        :param text_file_path: The path to the text file to generate subtitles from.
        """
        self.text_file_path = text_file_path
        self.sentences = []

    def load_text(self):
        """
        Load the text from the given file path into the object.
        """
        try:
            with open(self.text_file_path, 'r', encoding='utf-8') as file:
                self.sentences = file.read().splitlines()
        except FileNotFoundError:
            print(f"Error: The file {self.text_file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def generate_subtitles(self, max_length=50):
        """
        Generate subtitles from the loaded text.
        Split each sentence into multiple subtitles if it exceeds the max_length.
        :param max_length: The maximum length of a subtitle.
        """
        subtitles = []
        for sentence in self.sentences:
            while len(sentence) > 0:
                # Find the last space before max_length to split the sentence.
                split_index = max(sentence.rfind(' ', 0, max_length) + 1, 1)
                subtitles.append(sentence[:split_index].strip())
                sentence = sentence[split_index:]
        return subtitles

    def save_subtitles(self, subtitle_file_path):
        """
        Save the generated subtitles to a file.
        :param subtitle_file_path: The path to the file where subtitles will be saved.
        """
        try:
            with open(subtitle_file_path, 'w', encoding='utf-8') as file:
                for subtitle in self.generate_subtitles():
                    file.write(subtitle + '
')
        except Exception as e:
            print(f"An error occurred while saving subtitles: {e}")

    def generate_and_save_subtitles(self, subtitle_file_path, max_length=50):
        """
        Convenience method to load text, generate subtitles, and save them to a file.
        :param subtitle_file_path: The path to save the subtitles.
        :param max_length: The maximum length of a subtitle.
        """
        self.load_text()
        self.save_subtitles(subtitle_file_path)

# Example usage:
if __name__ == '__main__':
    text_file_path = 'input_text.txt'
    subtitle_file_path = 'output_subtitles.srt'
    generator = SubtitleGenerator(text_file_path)
    generator.generate_and_save_subtitles(subtitle_file_path)