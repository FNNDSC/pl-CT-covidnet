#!/usr/bin/env python                                            
#
# ct_covidnet ds ChRIS plugin app
#
# (c) 2019-2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
import sys
from .run_covidnet_ct import RunAnalysis

from chrisapp.base import ChrisApp


Gstr_title = """
 _____ _____      _____ _____  _   _ ___________        _   _      _   
/  __ \_   _|    /  __ \  _  || | | |_   _|  _  \      | \ | |    | |  
| /  \/ | |______| /  \/ | | || | | | | | | | | |______|  \| | ___| |_ 
| |     | |______| |   | | | || | | | | | | | | |______| . ` |/ _ \ __|
| \__/\ | |      | \__/\ \_/ /\ \_/ /_| |_| |/ /       | |\  |  __/ |_ 
 \____/ \_/       \____/\___/  \___/ \___/|___/        \_| \_/\___|\__|
"""


class Ct_covidnet(ChrisApp):
    PACKAGE                 = __package__
    TITLE                   = 'Plugin to run covidnet on CT images'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = '' # url of an icon image
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--imagefile', 
            dest         = 'imagefile', 
            type         = str, 
            optional     = False,
            help         = 'Name of CT image file to infer from')

    def run(self, options):
        print(Gstr_title)
        print(f'Version: {self.get_version()}')
        options.model_dir = '/usr/local/lib/covidnet/COVID-Net-CT-1-L'
        options.meta_name = 'model.meta'
        options.ckpt_name = 'model'
        options.input_width = 512
        options.input_height = 512
        RunAnalysis.run_analysis(options)


    def show_man_page(self):
        """
        Print the app's man page.
        """
        self.print_help()
