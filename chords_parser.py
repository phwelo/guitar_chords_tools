#!/usr/bin/env python3

from spellchecker import SpellChecker
import argparse
from itertools import tee, islice, chain

input_file = "output.txt"

def previous_and_next(iterable):
    prevs, items, nexts = tee(iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return izip(prevs, items, nexts)

def open_file(file_name):
  with open(file_name, "r") as f:
    return f.read()

def ls(str, arg1):
  '''lower and check if str starts with arg1'''
  return str.lower().startswith(arg1)

def tab_line_start(line):
  return ls(line, "a|-") or \
         ls(line, "b|-") or \
         ls(line, "g|-") or \
         ls(line, "d|-") or \
         ls(line, "e|-")

def tab_line_indicators(line):
  if line.count("-") > 5 and line.count("|") > 0:
    return True

def remove_tags(content):
  return content.replace("[ch]", "").replace("[/ch]", "").replace("[tab]", "").replace("[/tab]", "")

def check_if_section(line):
  line = remove_tags(line).lower()
  if (line.startswith("[") and "]" in line) or line.endswith(":"):
    return True
  elif line.count(" ") < 3 and "verse" in line or "chorus" in line or "bridge" in line or "intro" in line or "outro" in line:
    return True

def check_if_just_text(line, spell=SpellChecker()):
  known = list(spell.known(line.split(" ")))
  return True if len(known) > 2 else False

def in_scale(str):
  for note in str.split(" "):
    if note in str or "D" in str or "E" in str.upper() or "F" in str or "G" in str or "A" in str or "B" in str:
      return True

def count_sections(lines):
  return len([line for line in lines if line.startswith("[")])

def capo_in_line(line):
  return "capo" in line.lower()

def chord_line(line):
  return line.count("[ch]") > 0 or line.count("[/ch]") > 0

def only_chord_on_line(line):
  if line[0].upper() in "ABCDEFG" and len(line) < 5:
    return True

def is_too_late(history):
  return True if "section" in history or "chord" in history or "tab" in history else False

def classify_line(line, history):
  if check_if_just_text(line) or capo_in_line(line):
    if is_too_late(history):
      return "text"
    else:
      return "preface"
  elif tab_line_start(line) or tab_line_indicators(line):
    return "tab"
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
  return [ele for ele in list_of_lines if ele != None and ele.strip() != ""]

def parse_chords(content):
  newlines = list(lines_loop(content))
  return newlines

def main():
  args = parse_args()
  content = open_file(args.inputfile)
  return parse_chords(content)

if __name__ == "__main__":
  print(main())