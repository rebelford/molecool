import molecool 
import numpy as np
test_atoms = ["H", "O"]
test_coords = np.array([[1,0,0],[0,0,0], [0,1,0]])
molecool.write_xyz("test.xyz", test_atoms, test_coords)