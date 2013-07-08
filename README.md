dataset_moral.maze
==================

A dataset of dialogue data drawn from the BBC Radio 4 Moral Maze discussion show


Cleaning Process:

* Extract individual episodes from word document
* Check no instances of '|' character within the text. NB. Because the data consists of free-text it is difficult to select a delimiter that is guaranteed not to occur. The pipe is a safe bet
* Create a pipe delimited file consisting of line oriented data of the following form: 
 * speaker | utterance
* Use the csvtojson.py file in /tools to convert each csv file into a JSON document
* Create a JSON document for each episode that has the structure shown in schema/datafile.json
* Calculate an MD5 sum for each episode, e.g.
 * ```for f in *.json; do md5 "$f" > `basename "$f" .json`.md5; done```
