#!/usr/bin/env python3
#
# GlobalChemExtensions - Master Object
#
# -----------------------------------

# GlobalChemExtensions Import

# Visualization

from global_chem_extensions.analysis_tools.sunburster.sunburster import Sunburster

# Analytics

from global_chem_extensions.analysis_tools.drug_design_filters.drug_design_filters import DrugDesignFilters
from global_chem_extensions.analysis_tools.node_pca_analysis.node_pca_analysis import PCAAnalysis

# Converters

from global_chem_extensions.software_adapters.networkx_adapter.networkx_adapter import NetworkxAdapter
from global_chem_extensions.language_adapters.amino_acid_converter.amino_acid_converter import AminoAcidAdapter

# Monitors

from global_chem_extensions.monitoring_services.database_monitor.database_monitor import DatabaseMonitor

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
            save_file = False,
            return_mol_ids = False,
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
            return_mol_ids (Bool): Return the molecule IDS for the user to mine.

        '''

        pca_analysis = PCAAnalysis(
            smiles_list,
            morgan_radius,
            bit_representation,
            number_of_clusters,
            number_of_components,
            random_state,
            file_name,
            save_file=save_file,
            return_mol_ids = False
        )

        return_mol_ids = pca_analysis.conduct_analysis()

        if return_mol_ids:
            return return_mol_ids

    @staticmethod
    def smiles_to_amino_acids(
            smiles_list
    ):

        '''

        Arguments:
            smiles_list (List): List of the SMILES

        Returns:
            converted_list (List): Converted list of the SMILES to the amino acid converters

        '''

        converter = AminoAcidAdapter()

        converted_list = []

        for smiles in smiles_list:

            converted_list.append(
                converted_list.append(converter.convert_smiles_to_amino_acid_sequence(smiles))
            )

        return converted_list

    @staticmethod
    def amino_acids_to_smiles(
            amino_acid_list
    ):

        '''

        Arguments:
            amino_acid_list (List): List of the Amino Acids

        Returns:
            converted_list (List): Converted list of the SMILES to the amino acid converters

        '''

        converter = AminoAcidConverter()

        converted_list = []

        for amino_acid in amino_acid_list:

            converted_list.append(
                converter.convert_amino_acid_sequence_to_smiles(amino_acid)
            )

        return converted_list

    @staticmethod
    def check_status_on_open_source_databases():

        '''

        Check the Status on Databases

        '''

        database_monitor = DatabaseMonitor()
        database_monitor.heartbeat()


    @staticmethod
    def filter_smiles_by_criteria(
            smiles_list,
            lipinski_rule_of_5=False,
            ghose=False,
            veber=False,
            rule_of_3=False,
            reos=False,
            drug_like=False,
            pass_all_filters=False
    ):

        '''

        Arguments:
            lipinski_rule_of_5 (Bool): Lipinski Rule of 5 Criteria
            ghose (Bool): Ghose Filter,
            veber (Bool): Veber Filter,
            rule_of_3 (Bool): Rule of 3 Filter
            reos (Bool): Reos Filter
            drug_like (Bool): Drug Like Filter
            pass_all_filters (Bool): whether the user would like to pass all the filters

        Returns:

            the filtered data set
        '''

        drug_design_filters = DrugDesignFilters(
            smiles_list,
            lipinski_rule_of_5=lipinski_rule_of_5,
            ghose=ghose,
            veber=veber,
            rule_of_3=rule_of_3,
            reos=reos,
            drug_like=drug_like,
            pass_all_filters=pass_all_filters
        )

        return drug_design_filters.filter()

    @staticmethod
    def convert_to_networkx(network):

        '''

        Arguments:
            network (Dict): Convert to a networkx object for interoperability

        Returns:
            converted_network (Graph Object): Networkx Graph object

        '''

        network_adapter = NetworkxAdapter()
        converted_network = network_adapter.convert(network)

        return converted_network
