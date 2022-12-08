from openbabel import openbabel, pybel
import numpy as np

elements = ["Bq","H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Te", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm","Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

class MZMol(pybel.Molecule):
    def __init__(self, mol: openbabel.OBMol, parser_func=None):
        super(MZMol, self).__init__(mol)
        self._parser_func = parser_func

    """
    Atoms related properties
    """
    @property
    def natom(self):
        """
        Get number of atoms in molecule.
        """
        return len(self.atoms)

    @property
    def Zs(self):
        """
        Get atomic number array.
        """
        return np.array([atom.atomicnum for atom in self.atoms])

    @property
    def symbols(self):
        """
        Get chemical symbol array.
        """
        return np.array([elements[Z] for Z in self.Zs])

    @property
    def masses(self):
        """
        Get mass array. (in amu)
        """
        return np.array([atom.atomicmass for atom in self.atoms])

    """
    Coordinates related properties
    """
    @property
    def coords(self):
        """
        Export molecular coordinates in xyz format. (in Angstrom)
        """
        return np.array([atom.coords for atom in self.atoms])

    @property
    def xyz_str(self):
        """
        Export this molecule to string in xyz file format. (in Angstrom)
        """
        return self.write(format="xyz")

    @property
    def distance_matrix(self):
        """
        Calculate molecular coordinates in distance matrix format. (in Angstrom)
        Take H2O molecule as an example:
                    1          2          3
        1  H    0.000000
        2  O    0.962698   0.000000
        3  H    1.530008   0.962698   0.000000
        """
        distance_matrix = np.zeros((self.natom, self.natom))
        for r in range(self.natom):
            for c in range(0, r):
                if r != c:
                    coord_r = self.coords[r]
                    coord_c = self.coords[c]
                    distance_matrix[r, c] = np.linalg.norm(coord_r - coord_c)

        return distance_matrix

    @property
    def distance_vector(self):
        """
        Convert distance matrix to vector. (in Angstrom)
        Take H2O molecule as an example:
            r12       r13       r23
        [0.962698, 1.530008, 0.962698]
        """
        distance_vec = self.distance_matrix.flatten()
        return distance_vec[distance_vec > 0.0]
