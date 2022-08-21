#!/usr/bin/env python3

from spellchecker import SpellChecker
import argparse

# test case
input_file = "output.txt"

def open_file(file_name):
  '''local file is an easier way to test'''
  with open(file_name, "r") as f:
    return f.read()

def ls(str, arg1):
  '''lower and check if str starts with arg1'''
  return str.lower().startswith(arg1)

def tab_line_start(line):
  '''check if line starts with a guitar string'''
  return ls(line, "a|-") or \
         ls(line, "b|-") or \
         ls(line, "g|-") or \
         ls(line, "d|-") or \
         ls(line, "e|-")

def tab_line_indicators(line):
  '''best i could come up with is at least a few dashes and a line to indicate tablature'''
  if line.count("-") > 3 and line.count("|") > 0:
    return True

def remove_tags(content):
  '''remove tags for querying purposes'''
  return content.replace("[ch]", "").replace("[/ch]", "").replace("[tab]", "").replace("[/tab]", "")

def check_if_section(line):
  '''try to identify sections based on [sections] as well as a list of popular section names'''
  line = remove_tags(line).lower()
  if (line.startswith("[") and "]" in line) or line.endswith(":"):
    return True
  elif line.count(" ") < 3 and "verse" in line \
    or "chorus" in line or "bridge" in line \
      or "intro" in line or "outro" in line \
        or "solo" in line or "preface" in line:
    return True

def check_if_just_text(line, spell=SpellChecker()):
  '''check if line is real words (trying not to false-positive on chords)'''
  '''unfortunately i think this ties the script to windows'''
  known = list(spell.known(line.split(" ")))
  return True if len(known) > 2 else False

def in_scale(str):
  '''attempt to check if we are dealing with a line of spaces and chords'''
  for note in str.split(" "):
    if note.upper() in str.upper() or "D" in str.upper() or "E" in str.upper() or "F" in str.upper() or "G" in str.upper() or "A" in str.upper() or "B" in str.upper():
      return True

def count_sections(lines):
  '''reall just counting lines here'''
  return len([line for line in lines if line.startswith("[")])

def capo_in_line(line):
  '''capo text finder'''
  return "capo" in line.lower()

def chord_line(line):
  '''easiest way is if they were tagged properly'''
  return line.count("[ch]") > 0 or line.count("[/ch]") > 0

def only_chord_on_line(line):
  '''another easy way to identify is if its all major chords i guess'''
  compared = [True for r in [i for i in line.upper().replace(" ","")] if r in "ABCDEFGMSU#\\"]
  return False if False in compared else True

def is_too_late(history):
  '''is it too late for this line to be part of the preface?'''
  return True if "section" in history or "chord" in history or "tab" in history else False

def classify_line(line, history):
  '''unify other functions to classify a line no matter what'''
  if tab_line_start(line) or tab_line_indicators(line):
    return "tab"
  elif check_if_just_text(line) or capo_in_line(line):
    if is_too_late(history):
      return "text"
    else:
      return "preface"
  elif check_if_section(line):
    return "section"
  elif chord_line(line) or only_chord_on_line(line):
    return "chord"
  else:
    if is_too_late(history):
      return "block"
    else:
      return "preface"

def lines_loop(parsing):
  '''loop through lines and classify them'''
  parsing = remove_blank_lines(parsing.splitlines())
  so_far = []
  for line in parsing:
    result = {
      "type": classify_line(line, so_far),
      "content": remove_tags(line)
    }
    so_far.append(result["type"])
    yield result

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--inputfile', default="output.txt", help='chords file')
  return parser.parse_args()

def remove_blank_lines(list_of_lines):
  '''remove blank lines from a list of lines'''
  return [ele for ele in list_of_lines if ele != None and ele.strip() != ""]

def consolidate_tabs(lines):
  tab = []
  for i, line in enumerate(lines):
    if line["type"] == "tab" and len(tab) < 5:
      tab.append(line["content"])
    elif line["type"] == "tab" and len(tab) == 6:
      tab.append(line["content"])
      yield {"type": "tab", "content": tab}
      tab = []
    else:
      if len(tab) > 0:
        tab.append("")
        yield {"type": "tab", "content": tab}
        tab = []
      else:
        yield line

def parse_chords(content):
  '''basically the main, but i'm using this as a module'''
  newlines = list(lines_loop(content))
  with_tabs = list(consolidate_tabs(newlines))
  return with_tabs

def main():
  '''for testing'''
  args = parse_args()
  content = open_file(args.inputfile)
  return parse_chords(content)

if __name__ == "__main__":
  print(main())