#!/usr/bin/env python3
#
# GlobalChemExtensions - Master Object
#
# -----------------------------------

# GlobalChemExtensions Import

from global_chem_extensions.sunburster.sunburster import Sunburster
from global_chem_extensions.node_pca_analysis.node_pca_analysis import PCAAnalysis

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


    @staticmethod
    def node_pca_analysis(
            smiles_list,
            morgan_radius = 1,
            bit_representation = 512,
            number_of_clusters = 5,
            number_of_components = 0.95,
            random_state = 0,
            file_name = 'pca_analysis.html',
            save_file = False
    ):

        '''

        Perform a pca analysis on a node within globalchem, can be extended to lists outside of the dedicated SMILES.

        Arguments:
            smiles_list (List): list of SMILES that the user wants to cluster
            morgan_radius (Int): Morgan Radius of the chemical environment
            bit_representation (Int): Length of the bit representation
            number_of_clusters (Int): Number of clusters the user would like to do
            number_of_components (Int): How many PCA vectors to analyze
            random_state (Int):
            file_name (String): file name the user would like to input
            save_file (Bool): Whether the user wants to display the plot or save it.

        '''

        pca_analysis = PCAAnalysis(
            smiles_list,
            morgan_radius,
            bit_representation,
            number_of_clusters,
            number_of_components,
            random_state,
            file_name,
            save_file=save_file
        )

        pca_analysis.conduct_analysis()





