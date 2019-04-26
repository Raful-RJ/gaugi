

if(DEFINED $ENV{Athena_SET_UP})
  # Declare the package name:
  atlas_subdir( Gaugi )
  
  find_package( Boost COMPONENTS python )
  #find_package( ROOT COMPONENTS Core Hist Gpad Tree MathCore Hist MathMore RIO )
  find_package( ROOT COMPONENTS Core Hist RIO )
  
  find_package(OpenMP)
  if (OPENMP_FOUND)
      set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
      set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
  endif()
  
  atlas_add_library( GaugiLib
                     Root/*.cxx
                     PUBLIC_HEADERS Gaugi
                     INCLUDE_DIRS ${Boost_INCLUDE_DIRS} ${ROOT_INCLUDE_DIRS}
                     LINK_LIBRARIES ${Boost_LIBRARIES} ${ROOT_LIBRARIES}
                   )
  
  # Install files from the package:
  atlas_install_python_modules( python/*.py python/storage python/messenger  python/streamable python/parsers)
  atlas_install_scripts( scripts/*.py )

else()


  include_directories(${CMAKE_SOURCE_DIR} ${ROOT_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR})
  
  
  
  ROOT_GENERATE_DICTIONARY(GaugiDict  ${CMAKE_CURRENT_SOURCE_DIR}/Gaugi/MsgStream.h
                                      ${CMAKE_CURRENT_SOURCE_DIR}/Gaugi/defines.h
                                      LINKDEF
                                      ${CMAKE_CURRENT_SOURCE_DIR}/Root/LinkDef.h
                                      MODULE
                                      Gaugi)
                                   
                                    
  add_library(Gaugi  OBJECT ${CMAKE_CURRENT_SOURCE_DIR}/Root/MsgStream.cxx GaugiDict.cxx)
  
  install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/Gaugi/MsgStream.h ${CMAKE_CURRENT_SOURCE_DIR}/Gaugi/defines.h 
          DESTINATION Gaugi)

  gaugi_install_python_modules( ${CMAKE_CURRENT_SOURCE_DIR}/python Gaugi)

endif()

