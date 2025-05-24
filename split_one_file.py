import os

MAX_SIZE = 50 * 1024  # 50KB
TARGET_FILE = "guide_to_tabletop_game_design.md" # Specific file to process

def split_file(filepath):
    """Splits a Markdown file into smaller parts if it exceeds MAX_SIZE."""
    try:
        file_size = os.path.getsize(filepath)
    except OSError:
        print(f"Error: Could not get size of {filepath}. Skipping.")
        return

    if file_size <= MAX_SIZE:
        print(f"File {filepath} is already small enough ({file_size / 1024:.2f}KB). Skipping.")
        return

    print(f"File {filepath} is {file_size / 1024:.2f}KB. Splitting...")
    base, ext = os.path.splitext(filepath)
    part_number = 1
    current_chunk_size = 0
    current_chunk_lines = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                line_size = len(line.encode('utf-8'))
                if current_chunk_size + line_size > MAX_SIZE and current_chunk_lines:
                    part_filepath = f"{base}_part_{part_number}{ext}"
                    with open(part_filepath, 'w', encoding='utf-8') as f_out:
                        f_out.writelines(current_chunk_lines)
                    print(f"Created {part_filepath} ({current_chunk_size / 1024:.2f}KB)")
                    
                    part_number += 1
                    current_chunk_lines = []
                    current_chunk_size = 0
                
                current_chunk_lines.append(line)
                current_chunk_size += line_size

            if current_chunk_lines:
                part_filepath = f"{base}_part_{part_number}{ext}"
                with open(part_filepath, 'w', encoding='utf-8') as f_out:
                    f_out.writelines(current_chunk_lines)
                print(f"Created {part_filepath} ({current_chunk_size / 1024:.2f}KB)")
        print(f"Successfully split {filepath}")

    except Exception as e:
        print(f"Error processing file {filepath}: {e}")

if __name__ == "__main__":
    workspace_dir = '.'
    filepath = os.path.join(workspace_dir, TARGET_FILE)
    if os.path.exists(filepath):
        if "_part_" not in TARGET_FILE: # Make sure we are not splitting a part
             split_file(filepath)
        else:
            print(f"Skipping {TARGET_FILE} as it appears to be a part already.")
    else:
        print(f"Target file {TARGET_FILE} not found in {workspace_dir}.")
    print(f"Finished processing {TARGET_FILE}.") 