import ase
from ase import Atoms
import ase.visualize

#df = pd.read_csv("KaggleChallenge/champs-scalar-coupling/structures.csv")

def view(molecule):
    # Select a molecule
    mol = df[df['molecule_name'] == molecule]

    # Get atomic coordinates
    xcart = mol.iloc[:, 3:].values

    # Get atomic symbols
    symbols = mol.iloc[:, 2].values

    # Display molecule
    system = Atoms(positions=xcart, symbols=symbols)
    print('Molecule Name: %s.' %molecule)
    return ase.visualize.view(system, viewer="x3d")
