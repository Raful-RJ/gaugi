
__all__ = []

try:
    xrange
except NameError:
    xrange = range

import os, multiprocessing
RCM_GRID_ENV = int(os.environ.get('RCM_GRID_ENV',0))
RCM_NO_COLOR = int(os.environ.get('RCM_NO_COLOR',1))
OMP_NUM_THREADS = int(os.environ.get('OMP_NUM_THREADS',multiprocessing.cpu_count()))



from . import gtypes
__all__.extend(gtypes.__all__)
from .gtypes import *

from . import utilities
__all__.extend(utilities.__all__)
from .utilities import *


from . import messenger
__all__.extend(messenger.__all__)
from .messenger import *

from . import storage
__all__.extend(storage.__all__)
from .storage import *

from . import StatusCode
__all__.extend(StatusCode.__all__)
from .StatusCode import *

from . import enumerations
__all__.extend(enumerations.__all__)
from .enumerations import *

from . import parallel
__all__.extend(parallel.__all__)
from .parallel import *

from . import constants
__all__.extend(constants.__all__)
from .constants import *

from . import EventContext
__all__.extend(EventContext.__all__)
from .EventContext import *

from . import Service
__all__.extend(Service.__all__)
from .Service import *

from . import EDM
__all__.extend(EDM.__all__)
from .EDM import *

from . import Algorithm
__all__.extend(Algorithm.__all__)
from .Algorithm import *

from . import TEventLoop
__all__.extend(TEventLoop.__all__)
from .TEventLoop import *

from . import streamable
__all__.extend(streamable.__all__)
from .streamable import *

from . import tex
__all__.extend(tex.__all__)
from .tex import *




__gaugi__version__ = '2.0'

def print_gaugi_version():
  from Gaugi.enumerations import Color
  print( ("%sGaugi core (%s)%s") % (TexColor.CWHITE,__gaugi__version__,TexColor.CEND) )
  print( ("%sMaintainer: jodafons@cern.ch%s") % (TexColor.CWHITE, TexColor.CEND) )
#print_gaugi_version()
