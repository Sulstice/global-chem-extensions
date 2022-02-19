#!/usr/bin/env python3
#
# GlobalChemExtensions - Networkx Adapter
#
# ---------------------------------------

# GlobalChem Imports

from global_chem.global_chem import GlobalChem

class NetworkxAdapter(object):

    __version__ = '0.0.1'

    def __init__(self):

        self.gc = GlobalChem()
        self.gc.build_global_chem_network()
        self.network = self.gc.network
        print (self.network)