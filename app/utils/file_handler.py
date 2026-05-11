import shutil
from datetime import datetime
from app.config import PATHS

class FileHandler:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file_input:
            return file_input.read()

    @staticmethod
    def write_markdown(content, filename, category="generated"):
        """Writes content to the specified subfolder with a timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        clean_name = filename.replace(" ", "_").lower()
        target_path = PATHS[category] / f"{timestamp}_{clean_name}.md"
        
        with open(target_path, 'w', encoding='utf-8') as file_output:
            file_output.write(content)
        return target_path

    @staticmethod
    def move_to_processed(file_path):
        """Moves raw files to docs/ after ingestion."""
        destination = PATHS["docs"] / file_path.name
        shutil.move(file_path, destination)