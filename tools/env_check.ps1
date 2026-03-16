@'
import sys, sysconfig, os
print("Python:", sys.version)
print("Executable:", sys.executable)
print("SOABI:", sysconfig.get_config_var("SOABI"))

import numpy, spacy
print("NumPy:", numpy.__version__)
print("spaCy:", spacy.__version__)

# Verify compiled deps load
from cymem import cymem as _cymem
from blis import cy as _blis_cy
print("cymem OK:", _cymem is not None)
print("blis.cy OK:", _blis_cy is not None)

# Verify model load
nlp = spacy.load("en_core_web_sm")
print("Pipeline:", nlp.pipe_names)
'@ | python