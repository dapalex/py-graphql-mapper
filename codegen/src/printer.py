import pathlib
from .utils import getValidFolder
from .consts import templateFolder
import os
from .enums import TemplateType
from .priority import ExtractionResults

class Printer():
    
    extractionResults: ExtractionResults
    
    def __init__(self, extractionResults) -> None:
        self.extractionResults = extractionResults
    
    def saveFiles(self, folder: str):
        try:
            if folder:
                folder = getValidFolder(folder)
            else:
                print('Destination folder missing')
                
            self.saveScalarsFile(str(pathlib.Path(os.path.dirname(folder), 'scalars.py').absolute()))
            self.saveEnumsFile(str(pathlib.Path(os.path.dirname(folder), 'enums.py').absolute()))
            self.saveSimpleTypesFile(str(pathlib.Path(os.path.dirname(folder), 'gqlSimpleTypes.py').absolute()))
            self.saveTypesFile(str(pathlib.Path(os.path.dirname(folder), 'gqlTypes.py').absolute()))
            self.saveQueriesFile(str(pathlib.Path(os.path.dirname(folder), 'queries.py').absolute()))
            self.saveMutationsFile(str(pathlib.Path(os.path.dirname(folder), 'mutations.py').absolute()))
            self.saveCircularRefsFile(str(pathlib.Path(os.path.dirname(folder), 'circularRefs.py').absolute()))
        except Exception as ex:
            raise ex
    
    def saveScalarsFile(self, fileName):
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper: 
                wrapper.write(self.loadTemplateCode(TemplateType.SCALAR_TEMPLATE.value))
                wrapper.write('\n')
                for scalarDefinition in self.extractionResults.scalarDefinitions.values():
                    self.writeClassLineCode(scalarDefinition, wrapper)
                wrapper.write('\n')
        except Exception as ex:
            raise ex
               
    def saveEnumsFile(self, fileName):
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper: 
                wrapper.write(self.loadTemplateCode(TemplateType.ENUM_TEMPLATE.value))
                wrapper.write('\n')
                for enumClass in self.extractionResults.enumClasses.values():
                    self.writeClassCode(enumClass, wrapper)
                wrapper.write('\n')
        except Exception as ex:
            raise ex
                     
    def saveSimpleTypesFile(self, fileName):   
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.loadTemplateCode(TemplateType.FREE_TYPE_TEMPLATE.value))
                wrapper.write('\n')
                for simpleTypeClass in self.extractionResults.simpleTypeClasses.values():
                    self.writeClassCode(simpleTypeClass, wrapper)
        except Exception as ex:
            raise ex
            
    def saveTypesFile(self, fileName):   
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper: 
                wrapper.write(self.loadTemplateCode(TemplateType.TYPE_TEMPLATE.value))
                wrapper.write('\n')
                for typeClass in self.extractionResults.typeClasses.values():
                    self.writeClassCode(typeClass, wrapper)
        except Exception as ex:
            raise ex
            
    def saveQueriesFile(self, fileName):
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper: 
                wrapper.write(self.loadTemplateCode(TemplateType.QUERY_TEMPLATE.value))
                wrapper.write('\n')
                for queryClass in self.extractionResults.queryClasses.values():
                    self.writeClassCode(queryClass, wrapper)
                if self.extractionResults.queryClasses:
                    wrapper.write('\n')
                    for queriesEnum in self.extractionResults.queriesEnumClass.values():
                        self.writeClassCode(queriesEnum, wrapper)
        except Exception as ex:
            raise ex
                
    def saveMutationsFile(self, fileName):
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper: 
                wrapper.write(self.loadTemplateCode(TemplateType.MUTATION_TEMPLATE.value))
                wrapper.write('\n')
                for nutationClass in self.extractionResults.mutationClasses.values():
                    self.writeClassCode(nutationClass, wrapper)
                if self.extractionResults.mutationClasses:
                    wrapper.write('\n')
                    for mutationsEnum in self.extractionResults.mutationsEnumClass.values():
                        self.writeClassCode(mutationsEnum, wrapper)
        except Exception as ex:
            raise ex
   
    def saveCircularRefsFile(self, fileName):
        """For internal use"""
        try:
            with open(fileName, 'w', encoding='UTF-8') as wrapper: 
                wrapper.write(self.loadTemplateCode(TemplateType.CIRCULAR_REFS_TEMPLATE.value))
                wrapper.write('\n')
                for circularRef in self.extractionResults.circularRefs.values():
                    self.writeClassLineCode(circularRef, wrapper)
                wrapper.write('\n')
        except Exception as ex:
            raise ex
               
    def writeClassLineCode(self, codeLine, wrapper):
        """For internal use"""
        try:
            wrapper.write('\n')
            wrapper.writelines("%s\n"  %codeLine)
        except Exception as ex:
            raise ex
        
    def writeClassCode(self, classCode, wrapper):
        """For internal use"""
        try:
            wrapper.write('\n')
            wrapper.writelines("%s\n"  % i for i in classCode)
        except Exception as ex:
            raise ex
        
    def loadTemplateCode(self, templateName):
        """For internal use"""
        try:
            fileName = os.path.join(getValidFolder(templateFolder), templateName)
            with(templateFile := open(fileName)):
                return templateFile.read()
        except Exception as ex:
            raise ex
