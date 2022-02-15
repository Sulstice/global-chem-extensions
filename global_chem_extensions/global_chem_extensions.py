#!/usr/bin/env python3
#
# GlobalChemExtensions - Master Object
#
# -----------------------------------

# GlobalChemExtensions Import

from global_chem_extensions.sunburster.sunburster import Sunburster

class ExtensionsError(Exception):

    __version_error_parser__ = "0.0.1"
    __allow_update__ = False

    '''
    
    Raise an Extension Error if something is wrong. 
    
    '''
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class GlobalChemExtensions(object):

    __version__ = '0.0.1'

    def __init__(self):

        pass

    @staticmethod
    def sunburst_chemical_list(smiles_list, save_file=False):

        '''


        Sunburst a chemical list

        Arguments:
            smiles_list (String): list of smiles strings to analyze
            save_file (Boolean): whether the user would like it as a file

        '''

        Sunburster(smiles_list, save_file)



