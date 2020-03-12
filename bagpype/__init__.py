import bagpype.molecules
import bagpype.parameters

import bagpype.covalent
import bagpype.construction
import bagpype.parsing

import bagpype.settings  # for compatibility with the server for now
from bagpype.molecules import Protein
from bagpype.parsing import PDBParser
from bagpype.construction import Graph_constructor


head_string = (
    u"\n"
    u" |\u203E|                Welcome to              \n"
    u" | |__   __ _  __ _ _ __  _   _ _ __   ___  \n"
    u" | '_ \ / _` |/ _` | '_ \| | | | '_ \ / _ \ \n"
    u" | |_) | (_| | (_| | |_) | |_| | |_) |  __/ \n"
    u" |_.__/ \__,_|\__, | .__/ \__, | .__/ \___| \n"
    u"               __/ | |     __/ | |          \n"
    u"              |___/|_|    |___/|_|          \n"
    u"Biochemical, Atomistic Graph construction   \n"
    u"software in PYthon for Proteins, Etc.       \n"
    u"(C) Yaliraki group @ Imperial College London\n"
    u"\a"
)

print(head_string)


################################################


def standard_run(pdb_file):

    myprot = bagpype.molecules.Protein()

    parser = bagpype.parsing.PDBParser(pdb_file, download=True)
    parser.parse(myprot, strip={"res_name": ["HOH"]})

    ggenerator = bagpype.construction.Graph_constructor()
    ggenerator.construct_graph(myprot)

    return myprot
