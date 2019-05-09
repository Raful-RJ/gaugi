
__all__ = [ 
              #'Dataframe', 
              'StatusTool',
              'StatusWatchDog',
          ]


from Gaugi import EnumStringification


class StatusTool(EnumStringification):
  """
    The status of the tool
  """
  IS_FINALIZED   = 3
  IS_INITIALIZED = 2 
  ENABLE  = 1
  DISABLE = -1
  NOT_INITIALIZED = -2
  NOT_FINALIZED = -3
 

class StatusWatchDog(EnumStringification):
  """
    Use this to enable or disable the tool in execute call
  """
  ENABLE  = 1
  DISABLE = 0


