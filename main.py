# for the api docs see `bible-api.com`

import requests;

def format_json_verse(data):
    # print header
    print("=== Name: " + data['translation_name'] + ", reference: " + data['reference'] + " ===\n");

    # print every verse
    for verse in data['verses']:
        verse_n = str(verse['verse']);
        chapter_n = str(verse['chapter']);
        text = verse['text'];
        print("\tChapter: " + chapter_n + ", Verse: " + verse_n + "\n\t" + text);

# CHAPTER:VERSE - first chapter, first verse
response = requests.get("https://bible-api.com/john 1:1");
format_json_verse(response.json());

# an example of a request with translation
response = requests.get("https://bible-api.com/john 2:3?translation=kjv");
format_json_verse(response.json());

# an example of verse ranges
response = requests.get("https://bible-api.com/john 3:1-3,5-7");
format_json_verse(response.json());
