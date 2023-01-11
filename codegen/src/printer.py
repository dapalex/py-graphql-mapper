import pathlib
from .utils import get_valid_folder
from .consts import CIRCULARREFS_FILENAME, ENUMS_FILENAME, MUTATIONS_FILENAME, QUERIES_FILENAME, SCALARS_FILENAME, SIMPLE_TYPES_FILENAME, TEMPLATE_FOLDER, TYPES_FILENAME
import os
import logging as logger
from .enums import TemplateType
from .priority import ExtractionResults

class Printer():

    extractionResults: ExtractionResults

    def __init__(self, extractionResults) -> None:
        self.extractionResults = extractionResults

    def save_files(self, folder: str):
        try:
            if folder:
                folder = get_valid_folder(folder)
            else:
                logger.warning('Destination folder missing')

            self.save_scalars_file(str(pathlib.Path(folder, SCALARS_FILENAME).absolute()))
            self.save_enums_file(str(pathlib.Path(folder, ENUMS_FILENAME).absolute()))
            self.save_simple_types_file(str(pathlib.Path(folder, SIMPLE_TYPES_FILENAME).absolute()))
            self.save_types_file(str(pathlib.Path(folder, TYPES_FILENAME).absolute()))
            self.save_queries_file(str(pathlib.Path(folder, QUERIES_FILENAME).absolute()))
            self.save_mutations_file(str(pathlib.Path(folder, MUTATIONS_FILENAME).absolute()))
            self.save_circular_refs_file(str(pathlib.Path(folder, CIRCULARREFS_FILENAME).absolute()))
        except Exception as ex:
            raise ex

    def save_scalars_file(self, fileName):
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.load_template_code(TemplateType.SCALAR_TEMPLATE.value))
                wrapper.write('\n')
                for scalarDefinition in self.extractionResults.scalarDefinitions.values():
                    self.write_class_line_code(scalarDefinition, wrapper)
                wrapper.write('\n')
        except Exception as ex:
            raise ex

    def save_enums_file(self, fileName):
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.load_template_code(TemplateType.ENUM_TEMPLATE.value))
                wrapper.write('\n')
                for enumClass in self.extractionResults.enumClasses.values():
                    self.write_class_code(enumClass, wrapper)
                wrapper.write('\n')
        except Exception as ex:
            raise ex

    def save_simple_types_file(self, fileName):
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.load_template_code(TemplateType.FREE_TYPE_TEMPLATE.value))
                wrapper.write('\n')
                for simpleTypeClass in self.extractionResults.simpleTypeClasses.values():
                    self.write_class_code(simpleTypeClass, wrapper)
        except Exception as ex:
            raise ex

    def save_types_file(self, fileName):
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.load_template_code(TemplateType.TYPE_TEMPLATE.value))
                wrapper.write('\n')
                for typeClass in self.extractionResults.typeClasses.values():
                    self.write_class_code(typeClass, wrapper)
        except Exception as ex:
            raise ex

    def save_queries_file(self, fileName):
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.load_template_code(TemplateType.QUERY_TEMPLATE.value))
                wrapper.write('\n')
                for queryClass in self.extractionResults.queryClasses.values():
                    self.write_class_code(queryClass, wrapper)
                if self.extractionResults.queryClasses:
                    wrapper.write('\n')
                    for queriesEnum in self.extractionResults.queriesEnumClass.values():
                        self.write_class_code(queriesEnum, wrapper)
        except Exception as ex:
            raise ex

    def save_mutations_file(self, fileName):
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.load_template_code(TemplateType.MUTATION_TEMPLATE.value))
                wrapper.write('\n')
                for nutationClass in self.extractionResults.mutationClasses.values():
                    self.write_class_code(nutationClass, wrapper)
                if self.extractionResults.mutationClasses:
                    wrapper.write('\n')
                    for mutationsEnum in self.extractionResults.mutationsEnumClass.values():
                        self.write_class_code(mutationsEnum, wrapper)
        except Exception as ex:
            raise ex

    def save_circular_refs_file(self, fileName):
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.load_template_code(TemplateType.CIRCULAR_REFS_TEMPLATE.value))
                wrapper.write('\n')
                for circularRef in self.extractionResults.circularRefs.values():
                    self.write_class_line_code(circularRef, wrapper)
                wrapper.write('\n')
        except Exception as ex:
            raise ex

    def write_class_line_code(self, codeLine, wrapper):
        """For internal use"""
        try:
            wrapper.write('\n')
            wrapper.writelines("%s\n"  %codeLine)
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
