import pathlib
from .utils import get_valid_folder
from .consts import PY_EXTENSION, TYPE_REFS_FILENAME, ENUMS_FILENAME, MUTATIONS_FILENAME, QUERIES_FILENAME, SCALARS_FILENAME, SIMPLE_TYPES_FILENAME, TEMPLATE_FOLDER, TYPES_FILENAME
import os
import logging as logger
from .enums import TemplateType
from .priority import ExtractionResults

class Printer():

    extractionResults: ExtractionResults

    def __init__(self, extractionResults) -> None:
        self.extraction_results = extractionResults

    def save_files(self, folder: str):
        try:
            if folder:
                folder = get_valid_folder(folder)
            else:
                logger.warning('Destination folder missing')
            self.save_file(TemplateType.SCALAR_TEMPLATE, str(pathlib.Path(folder, SCALARS_FILENAME + PY_EXTENSION).absolute()), 'scalar_defs')
            self.save_file(TemplateType.ENUM_TEMPLATE, str(pathlib.Path(folder, ENUMS_FILENAME + PY_EXTENSION).absolute()), 'enum_classes')
            self.save_file(TemplateType.FREE_TYPE_TEMPLATE, str(pathlib.Path(folder, SIMPLE_TYPES_FILENAME + PY_EXTENSION).absolute()), 'simple_type_classes')
            self.save_file(TemplateType.TYPE_TEMPLATE, str(pathlib.Path(folder, TYPES_FILENAME + PY_EXTENSION).absolute()), 'type_classes')
            self.save_operation_file(TemplateType.QUERY_TEMPLATE, str(pathlib.Path(folder, QUERIES_FILENAME + PY_EXTENSION).absolute()), ('query_classes', 'queries_enum_class'))
            self.save_operation_file(TemplateType.MUTATION_TEMPLATE, str(pathlib.Path(folder, MUTATIONS_FILENAME + PY_EXTENSION).absolute()), ('mutation_classes', 'mutations_enum_class'))
            self.save_file(TemplateType.TYPE_REFS_TEMPLATE, str(pathlib.Path(folder, TYPE_REFS_FILENAME + PY_EXTENSION).absolute()), 'type_refs')
        except Exception as ex:
            raise ex

    def save_file(self, enum_template, file_name, attr_name_result):
        """For internal use"""
        try:
            with open(file_name, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.load_template_code(enum_template.value))
                wrapper.write('\n')
                for curr_class in getattr(self.extraction_results, attr_name_result).values():
                    self.write_class_code(curr_class, wrapper)
        except Exception as ex:
            raise ex

    def save_operation_file(self, enum_template, file_name, attr_name_results):
        """For internal use"""
        try:
            with open(file_name, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.load_template_code(enum_template.value))
                wrapper.write('\n')
                for curr_class in getattr(self.extraction_results, attr_name_results[0]).values():
                    self.write_class_code(curr_class, wrapper)
                if getattr(self.extraction_results, attr_name_results[0]):
                    wrapper.write('\n')
                    for queriesEnum in getattr(self.extraction_results, attr_name_results[1]).values():
                        self.write_class_code(queriesEnum, wrapper)
        except Exception as ex:
            raise ex

    def write_class_code(self, classCode, wrapper):
        """For internal use"""
        try:
            wrapper.write('\n')
            wrapper.writelines("%s\n"  % i for i in classCode)
        except Exception as ex:
            raise ex

    def load_template_code(self, templateName):
        """For internal use"""
        try:
            fileName = os.path.join(get_valid_folder(TEMPLATE_FOLDER), templateName)
            with(templateFile := open(fileName)):
                return templateFile.read()
        except Exception as ex:
            raise ex
