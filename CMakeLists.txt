
include_directories(${CMAKE_SOURCE_DIR} ${ROOT_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR})



ROOT_GENERATE_DICTIONARY(GaugiDict  ${CMAKE_CURRENT_SOURCE_DIR}/Gaugi/MsgStream.h
                                    ${CMAKE_CURRENT_SOURCE_DIR}/Gaugi/defines.h
                                    LINKDEF
                                    ${CMAKE_CURRENT_SOURCE_DIR}/src/LinkDef.h
                                    MODULE
                                    Gaugi)
                                 
add_library(Gaugi  OBJECT ${CMAKE_CURRENT_SOURCE_DIR}/src/MsgStream.cxx GaugiDict.cxx)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/Gaugi/MsgStream.h ${CMAKE_CURRENT_SOURCE_DIR}/Gaugi/defines.h 
        DESTINATION Gaugi)






