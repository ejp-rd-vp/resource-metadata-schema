#!/bin/sh
SEED=$1
SPARQL=$2

V=$(sed -e :a -e '$!N; s/\n/> </; ta' $SEED)

echo "prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?o WHERE {
    VALUES ?sub { <$V> }
    ?sub rdfs:subClassOf* ?o .
} " > "$SPARQL"

sed -i 's/[<][ ]/</' $SPARQL
sed -i 's/[<][ ][ ]/</' $SPARQL
sed -i 's/[ ][<][ ][ ]/</' $SPARQL
#sed -i 's/[ ][>]/>/' $SPARQL
