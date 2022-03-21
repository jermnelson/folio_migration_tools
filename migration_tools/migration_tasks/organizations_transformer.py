<<<<<<< HEAD
<<<<<<< HEAD
# This is a work in progress
import csv
import ctypes
import json
import logging
import sys
import time
import traceback
import uuid
from os.path import isfile
from pathlib import Path
from typing import List, Optional

from folio_uuid.folio_namespaces import FOLIONamespaces
from migration_tools.custom_exceptions import (
    TransformationProcessError,
    TransformationRecordFailedError,
)

from migration_tools.folder_structure import FolderStructure
from migration_tools.helper import Helper
from migration_tools.library_configuration import (
    FileDefinition,
    LibraryConfiguration,
)

# TODO Create OrganizationMapper 
<<<<<<< HEAD
# TODO from migration_tools.mapping_file_transformation.organization_mapper import OrganizationMapper
=======
from migration_tools.mapping_file_transformation.organization_mapper import OrganizationMapper
>>>>>>> 71e25e7 (add organization_mapper #146)
from migration_tools.mapping_file_transformation.mapping_file_mapper_base import (
    MappingFileMapperBase,
)
from migration_tools.report_blurbs import Blurbs
from pydantic.main import BaseModel

from migration_tools.migration_tasks.migration_task_base import MigrationTaskBase

csv.field_size_limit(int(ctypes.c_ulong(-1).value // 2))

class OrganizationsTransformer(MigrationTaskBase):
    class TaskConfiguration(BaseModel):
        name: str
        migration_task_type: str
        files: List[FileDefinition]
        organizations_mapping_file_name: str

    @staticmethod
    def get_object_type() -> FOLIONamespaces:
        return FOLIONamespaces.organizations

    def __init__(
        self,
        task_config: TaskConfiguration,
        library_config: LibraryConfiguration,
    ):
        csv.register_dialect("tsv", delimiter="\t")

        super().__init__(library_config, task_config)
        self.task_config = task_config
        self.files = [
            f
            for f in self.task_config.files
            if isfile(self.folder_structure.legacy_records_folder / f.file_name)
        ]
        if not any(self.files):
            ret_str = ",".join(f.file_name for f in self.task_config.files)
            raise TransformationProcessError(
                f"Files {ret_str} not found in {self.folder_structure.data_folder}/{self.get_object_type().name}"
            )
        logging.info("Files to process:")
        for filename in self.files:
            logging.info("\t%s", filename.file_name)
        
        self.total_records = 0
<<<<<<< HEAD
        self.folio_keys = []
        self.items_map = self.setup_records_map()
        self.folio_keys = MappingFileMapperBase.get_mapped_folio_properties_from_map(
            self.items_map
        )
        self.failed_files: List[str] = list()
=======
        self.items_map = self.setup_records_map(
            self.folder_structure.mapping_files_folder
            / self.task_config.items_mapping_file_name
        )
>>>>>>> 71e25e7 (add organization_mapper #146)
    
    def wrap_up(self):
        logging.info("Wrapping up!")

<<<<<<< HEAD

=======
>>>>>>> 71e25e7 (add organization_mapper #146)
    def do_work(self):
        logging.info("Getting started!")
        for filename in self.files:
            try:
                logging.info("\t%s", filename.file_name)
                self.do_actual_work(filename)
            # Something goes really wrong and we want to stop the script
            except TransformationProcessError as tpe:
                logging.critical(tpe)
                sys.exit()
            except Exception as e:
                print(f"Something unexpected happend! {e}")
                raise e


        # Create organization
        # Create contacts
        # Create credentials

        # TODO Hemläxa: använd json-fil med fungerande mappning
        # TODO Sapa ett megaorganisationsobjekt
        # TODO Skapa schema av objektet med något verktyg!
        # TODO Behöver schemat motsvaras av ett objekt? T.ex.
        
        '''
        "organizationMigrationObject": {
            "organization": {
                "id": "uuid",
                "name": "string",
                "contacts": [uuid, uuid]
            },
            "contacts": [
                {
                "id": "uuid",
                "name": "string",
                "organizationId": "uuid"
                }
            ],
            "credentials": [
                {
                "id": "uuid",
                "username": "string"
                "contactId": "uuid"
                }
            ],
            "notes": [
                {
                "id": "uuid",
                "text": "string"
                "organizationId": "uuid"
                }
            ]
        }
        '''


    def do_actual_work(self, filename):
        for i in range(1,5):
            logging.info(i)
            try:
                if i == 2:
                    raise TransformationRecordFailedError("","I like everyone equally", str(i))
            except TransformationRecordFailedError as trfe:
                trfe.log_it()

        raise TransformationProcessError("","Error reading file with name", filename.file_name)
=======
# This is a work in progress
=======
'''
This is a work in progress
The transformer...
Sets up files, validates data.
Starts the mapper, which creates FOLIO objects from legacy data.
Compares, merges created ojects.
Wraps up.

The mapper should only take a dict of legacy date and transform that to a FOLIO object.

'''
>>>>>>> 3b9609c (continue work)
import csv
import ctypes
import json
import logging
import sys
import time
import traceback
import uuid
from os.path import isfile
from pathlib import Path
from typing import List, Optional

from folio_uuid.folio_namespaces import FOLIONamespaces
from migration_tools.custom_exceptions import (
    TransformationProcessError,
    TransformationRecordFailedError,
)

from migration_tools.folder_structure import FolderStructure
from migration_tools.helper import Helper
from migration_tools.library_configuration import (
    FileDefinition,
    LibraryConfiguration,
)

# TODO Create OrganizationMapper Titta inte för mycket på processors.

from migration_tools.mapping_file_transformation.organization_mapper import OrganizationMapper
from migration_tools.mapping_file_transformation.mapping_file_mapper_base import (
    MappingFileMapperBase,
)
from migration_tools.report_blurbs import Blurbs
from pydantic.main import BaseModel

from migration_tools.migration_tasks.migration_task_base import MigrationTaskBase

csv.field_size_limit(int(ctypes.c_ulong(-1).value // 2))

# Read files and do some work

class OrganizationsTransformer(MigrationTaskBase):
    class TaskConfiguration(BaseModel):
        name: str
        migration_task_type: str
        files: List[FileDefinition]
        organizations_mapping_file_name: str

    @staticmethod
    def get_object_type() -> FOLIONamespaces:
        return FOLIONamespaces.organizations

    def __init__(
        self,
        task_config: TaskConfiguration,
        library_config: LibraryConfiguration,
    ):
        csv.register_dialect("tsv", delimiter="\t")

        super().__init__(library_config, task_config)
        self.task_config = task_config
        self.object_type = self.get_object_type().name
        self.files = self.list_source_files()
        
        self.total_records = 0

        self.organization_map = self.setup_records_map(
            self.folder_structure.mapping_files_folder
            / self.task_config.organizations_mapping_file_name
        )
        self.results_path = self.folder_structure.created_objects_path
        self.failed_files: List[str] = list()
    
        self.folio_keys = []
        self.folio_keys = MappingFileMapperBase.get_mapped_folio_properties_from_map(
            self.organization_map
        )

        self.mapper = OrganizationMapper(
            self.folio_client,
            self.organization_map,
            # self.load_ref_data_mapping_file(
            #     self.folder_structure.mapping_files_folder,
            #     self.folio_keys,
            #     ),
            self.library_configuration
            )
        
    def list_source_files(self):
        # Source data files
        files = [
            self.folder_structure.data_folder / self.object_type / f.file_name
            for f in self.task_config.files
            if isfile(self.folder_structure.data_folder / self.object_type / f.file_name)
        ]
        if not any(files):
            ret_str = ",".join(f.file_name for f in self.task_config.files)
            raise TransformationProcessError(
                f"Files {ret_str} not found in {self.folder_structure.data_folder / 'items'}"
            )
        logging.info("Files to process:")
        for filename in files:
            logging.info("\t%s", filename)
        return files

    def process_single_file(self, filename):
        with open(
            filename, encoding="utf-8-sig") as records_file, open(
            self.folder_structure.created_objects_path, "w+"
            ) as results_file:
            self.mapper.migration_report.add_general_statistics(
                "Number of files processed"
            )
            start = time.time()
            records_processed = 0
            for idx, record in enumerate(
                self.mapper.get_objects(records_file, filename)
            ):
                records_processed += 1
                
                try:
                    if idx == 0:
                        logging.info("First legacy record:")
                        logging.info(json.dumps(record, indent=4))
                    folio_rec, legacy_id = self.mapper.do_map(
                        record, f"row {idx}", FOLIONamespaces.items
                    )
                    if idx == 0:
                        logging.info("First FOLIO record:")
                        logging.info(json.dumps(folio_rec, indent=4))
                    Helper.write_to_file(results_file, folio_rec)

                except TransformationProcessError as process_error:
                    self.mapper.handle_transformation_process_error(idx, process_error)
                except TransformationRecordFailedError as error:
                    self.mapper.handle_transformation_record_failed_error(idx, error)
                except Exception as excepion:
                    self.mapper.handle_generic_exception(idx, excepion)

                self.mapper.migration_report.add_general_statistics(
                    "Number of Legacy items in file"
                )
                if idx > 1 and idx % 10000 == 0:
                    elapsed = idx / (time.time() - start)
                    elapsed_formatted = "{0:.4g}".format(elapsed)
                    logging.info(  # pylint: disable=logging-fstring-interpolation
                        f"{idx:,} records processed. Recs/sec: {elapsed_formatted} "
                    )
            self.total_records = records_processed
            logging.info(  # pylint: disable=logging-fstring-interpolation
                f"Done processing {filename} containing {self.total_records:,} records. "
                f"Total records processed: {self.total_records:,}"
            )
<<<<<<< HEAD
>>>>>>> 2e5fb95 (continue orgs work)
=======
    
    
    def do_work(self):
        logging.info("Getting started!")
        for file in self.files:
            logging.info("Processing %s", file)
            try:
                print(file)
                self.process_single_file(file)
            except Exception as ee:
                error_str = (
                    f"Processing of {file} failed:\n{ee}."
                    "Check source files for empty lines or missing reference data"
                )
                logging.exception(error_str)
                self.mapper.migration_report.add(
                    Blurbs.FailedFiles, f"{file} - {ee}"
                )
                sys.exit()
    
    
    def wrap_up(self):
        logging.info("Done. Wrapping up...")
        with open(
            self.folder_structure.migration_reports_file, "w"
        ) as migration_report_file:
            logging.info(
                "Writing migration- and mapping report to %s",
                self.folder_structure.migration_reports_file,
            )
            self.mapper.migration_report.write_migration_report(migration_report_file)
            Helper.print_mapping_report(
                migration_report_file,
                self.total_records,
                self.mapper.mapped_folio_fields,
                self.mapper.mapped_legacy_fields,
            )
        logging.info("All done!")
>>>>>>> 6d341e1 (process files and schema)