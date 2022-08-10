#!/usr/bin/env python3

from spellchecker import SpellChecker
import argparse

input_file = "output.txt"

ch_ansi_colored_map = {
  "ch": {
    "start": "<code for gray>",
    "end":   "<code for reset>"
  },
  "tab": {
    "start": "<>",
    "end":   "<>"
  }
}

ch_html_map = {
  "ch": {
    "start": "<b>",
    "end":   "</b>"
  },
  "tab": {
    "start": "",
    "end":   ""
  }
}

plaintext_map = {
  "ch": {
    "start": "",
    "end":   ""
  },
  "tab": {
    "start": "",
    "end":   ""
  }
}

def open_file(file_name):
  with open(file_name, "r") as f:
    return f.read()

def map_replace_chords(map, content):
  parsing = content.replace("[ch]", map["ch"]["start"]).replace("[/ch]", map["ch"]["end"])
  parsing = parsing.replace("[tab]", map["tab"]["start"]).replace("[/tab]", map["tab"]["end"])
  return parsing

def classify_line(line, lines_so_far, spell=SpellChecker()):
  known = list(spell.known(line.split(" ")))
  if "[" in line and "]" in line:
    return {
      "type": "section", 
      "contents": line
    }
  elif len(known) > 0 and known.count("am") == len(known):
    return {
      "type": "chords", 
      "contents": line
    }
  elif len(known) > 0:
    sections = 0
    for newline in lines_so_far:
      if "type" in newline and newline["type"] == "section":
        sections += 1
    if sections == 0:
      return {
        "type": "preface", "contents": line
      }
    else:
      return {
        "type": "lyrics",
        "contents": line
      }
  else:
    res = [ele for ele in list("abcdefg") if(ele in line)]
    if len(res) > 0:
      return {
        "type": "chords", 
        "contents": line
      }

def lines_loop(parsing):
  for line in parsing.splitlines():
    yield classify_line(line, parsing)

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--inputfile', default="output.txt", help='chords file')
  return parser.parse_args()

def remove_blank_lines(list_of_lines):
  return [ele for ele in list_of_lines if ele != None]

def parse_chords(map, content):
  parsing = map_replace_chords(map, content)
  newlines = list(lines_loop(parsing))
  res = remove_blank_lines(newlines)
  return res

def main():
  args = parse_args()
  # need to work in an option for string
  content = open_file(args.inputfile)
  # high level parsing (for formatting and eventually transposing)
  return parse_chords(plaintext_map, content)

if __name__ == "__main__":
  print(main())