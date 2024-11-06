from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

import xml.etree.ElementTree as ET
from nomad.config import config
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.parsing.parser import MatchingParser

from pymodaq.schema_packages.schema_package import TypeSettings, Settings, XMLParameter

configuration = config.get_plugin_entry_point(
    'pymodaq.parsers:parser_entry_point'
)

class XMLParser(MatchingParser):
    def parse(self, mainfile: str, archive: 'EntryArchive', logger: 'BoundLogger', child_archives: dict[str, 'EntryArchive'] = None) -> None:
        if(logger):
            logger.info('XMLParser.parse', parameter=configuration.parameter)

        with open(mainfile, 'r') as file:
            xml_string = file.read()

        root = ET.fromstring(xml_string)

        xml_param = XMLParameter(name=root.get('title', 'root'))
        xml_param.settings_list = []


        def parse_group(xml_element, settings_group):
            settings_group.title = xml_element.get('title', 'Unnamed')
            settings_group.type = xml_element.get('type', 'group')
            settings_group.visible = xml_element.get('visible') == '1'
            settings_group.removable = xml_element.get('removable') == '1'
            settings_group.readonly = xml_element.get('readonly') == '1'
            settings_group.value = xml_element.text.strip() if xml_element.text else None

            settings_group.childrens = []

            for child in xml_element:
                # if child.tag == 'group':
                #     child_group = Settings()
                #     parse_group(child, child_group)
                #     settings_group.childrens.append(child_group)
                # else:
                    type_setting = TypeSettings(
                        title=child.get('title', ''),
                        type=child.get('type', ''),
                        visible=child.get('visible') == '1',
                        removable=child.get('removable') == '1',
                        readonly=child.get('readonly') == '1',
                        value=child.text.strip() if child.text else None
                    )
                    settings_group.type_settings_list.append(type_setting)

        for group in root:
            main_group = Settings()
            parse_group(group, main_group)
            xml_param.settings_list.append(main_group)

        archive.data = xml_param
