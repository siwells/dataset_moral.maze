from argparse import ArgumentParser
import csv
import json

parser = ArgumentParser()
parser.add_argument('delimiter', metavar="DELIMITER", help='Delimiter to separate on')
parser.add_argument('fname', metavar='FILE', help='File to process')
args = parser.parse_args()

outfile = args.fname+".json"

f = open( args.fname, 'r' )
reader = csv.DictReader( f, delimiter=args.delimiter, fieldnames = ( "speaker","utterance" ) )

out = open( outfile, 'w' )
out.write( json.dumps( [row for row in reader] ) )
