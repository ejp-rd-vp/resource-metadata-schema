#!/usr/bin/env python
"""
Generate example JSON documents,. convert to RDF and validate against the schema
"""

import json
import requests
import sys
import glob
import os

from rdflib.plugin import register, Parser
from rdflib import RDF,Namespace, Graph, ConjunctiveGraph

from jsonschema import validate as js_validate
from jsonschema import RefResolver, Draft7Validator, ValidationError
import rdflib_jsonld

from ShExJSG import Schema
from pyshex.evaluate import evaluate

PATH_TO_SCHEMAS='../json_schema/'
PATH_TO_EXAMPLES='../examples/'
EJP = Namespace("http://purl.org/ejp-rd/vocabulary/")
EJPS = Namespace("http://purl.org/ejp-rd/metadata/shapes/")

def get_file(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)


def test_catalog_schema(instance_file, json_schema_file, shex_file, shex_subject, shex_rule):
    try:
        instance = get_file (instance_file )

        abs_path = 'file:'+os.getcwd()+os.sep+PATH_TO_SCHEMAS
        resolver = RefResolver(base_uri=abs_path, referrer=None)
        schema = get_file(json_schema_file)
        validator = Draft7Validator(schema=schema, resolver=resolver)
        validator.validate(instance)

        context = get_file('../ejp_vocabulary_context.json')
        instance["@context"] = context

        graph = ConjunctiveGraph()
        graph.parse(data=json.dumps(instance), format='json-ld')

        with open(shex_file, 'r') as shex_schema:
            for s, p, o in graph.triples((None, RDF.type, shex_subject)):
                print("checking ShEX valdidation for {}".format(s))
                rslt, reason = evaluate(graph, shex_schema.read(),
                                        start=shex_rule,
                                        focus=s)
                if not rslt:
                    print(f"{reason if reason else 'DOES NOT CONFORM'}")

    except ValidationError as e:
        print("testing catalog schema failed")
        print ("error validating file : {}".format(e))
        raise
    pass
    print("testing catalog schema passed")

if __name__ == "__main__":
    test_catalog_schema(
        PATH_TO_EXAMPLES+'erdri_catalog.json',
        PATH_TO_SCHEMAS + 'catalog_of_registries.json',
        '../validation_vp_model/metadata_model.shex',
        EJP.CatalogOfRegistries,
        EJPS.CatalogOfRegistriesShape
    )

    test_catalog_schema(
        PATH_TO_EXAMPLES + 'registry-1.json',
        PATH_TO_SCHEMAS + 'registry.json',
        '../validation_vp_model/metadata_model.shex',
        EJP.PatientRegistryDataset,
        EJPS.RegistryDatasetShape
    )
