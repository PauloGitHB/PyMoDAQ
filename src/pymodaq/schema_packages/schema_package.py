from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    # from nomad.datamodel.datamodel import (
    #     EntryArchive,
    #     EntryData,sss
    #     ArchiveSection
    # )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.datamodel.datamodel import EntryArchive, EntryData, ArchiveSection
from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Quantity, SchemaPackage, SubSection, MSection, Section

configuration = config.get_plugin_entry_point(
    'pymodaq.schema_packages:schema_package_entry_point'
)
m_package = SchemaPackage()

class TypeSettings(MSection):
    title = Quantity(
        type=str,
        description=""
        )

    type = Quantity(
        type=str,
        description=""
        )

    visible = Quantity(
        type=bool,
        description=""
        )

    removable = Quantity(
        type=bool,
        description="")

    readonly = Quantity(
        type=bool,
        description="")

    value = Quantity(
        type=str,
        description="")

class Settings(EntryData,ArchiveSection):
    # m_def = Section(
    #         a_eln={
    #             "properties": {
    #                 "order": [
    #                     "title", "type", "visible", "removable", "readonly", "value", "children"
    #                 ]
    #             }
    #         }
    #     )

    title = Quantity(
        type=str,
        description=""
        )

    type = Quantity(
        type=str,
        description=""
        )

    visible = Quantity(
        type=bool,
        description=""
        )

    removable = Quantity(
        type=bool,
        description="")

    readonly = Quantity(
        type=bool,
        description="")

    value = Quantity(
        type=str,
        description="")

    type_settings_list = SubSection(
        section_def=TypeSettings,
        description="",
        repeats = True)

    # childrens = SubSection(
    #     section_def='self',
    #     description="",
    #     repeats = True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:

        super().normalize(archive, logger)

class XMLParameter(EntryData,ArchiveSection):
    name = Quantity(
        type = str,
        description = "name"
    )

    settings_list = SubSection(
        section_def = Settings,
        description = 'settings',
        repeats = True
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:

        super().normalize(archive, logger)



m_package.__init_metainfo__()
