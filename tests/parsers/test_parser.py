import logging
import os
from nomad.datamodel import EntryArchive
import json
from pymodaq.parsers.parser import XMLParser
from pymodaq.schema_packages.schema_package import TypeSettings, Settings, XMLParameter


def test_parser():

    parser = XMLParser()
    archive = EntryArchive()
    test_file = os.path.join(os.path.dirname(__file__),'../data/data.xml')


    parser.parse(test_file, archive, logging.getLogger(__name__),None)

    json_res = json.dumps(archive.data.m_to_dict(), indent=4)

    print(json_res)

test_parser()