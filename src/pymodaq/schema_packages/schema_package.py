from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
        EntryData
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Quantity, SchemaPackage, SubSection, Section

configuration = config.get_plugin_entry_point(
    'pymodaq.schema_packages:schema_package_entry_point'
)

m_package = SchemaPackage()


class Parameters():

    name = Quantity()

    options = Quantity()

    text = Quantity()

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class XMLString(EntryData):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )

    parameter = SubSection(
        section_def = Parameters,
        description="instrument used for this measurement",
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)



m_package.__init_metainfo__()
