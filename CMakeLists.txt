################################################################################
# Package: prometheus
################################################################################

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

### Install python packages
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")

include(SetupPythonPackage)



# Install files from the package:
atlas_install_python_modules( python/*.py python/storage python/messenger  python/streamable python/parsers)
atlas_install_scripts( scripts/*.py )
