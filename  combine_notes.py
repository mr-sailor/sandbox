import os

NOTES_FOLDER = "./notes/"
COMBINED_NOTES = "notes.txt"
SECTION_DIVIDER = "\n=========================\n{}\n\n\n"

# clear current notes
with open(COMBINED_NOTES, "w") as f:
    f.write("")

note_files = sorted([f for f in os.listdir(NOTES_FOLDER)])

with open(COMBINED_NOTES, "a") as f:
    for note_file in note_files:
        with open(NOTES_FOLDER + note_file) as content:

            f.write(SECTION_DIVIDER.format(note_file.upper()) + content.read())
