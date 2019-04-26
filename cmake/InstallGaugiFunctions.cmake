

function(gaugi_initialize)
  file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/python)
  file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
endfunction(gaugi_initialize)


function(gaugi_install_python_modules filepath module)
  message(STATUS "${filepath} -> ${CMAKE_BINARY_DIR}/python/${module}")
    execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink ${filepath} ${CMAKE_BINARY_DIR}/python/${module})
endfunction(gaugi_install_python_modules)



function( gaugi_finalize )

  file(GLOB SO_FILES ${CMAKE_BINARY_DIR}/*.so)
  FOREACH( SFILE ${SO_FILES})
    execute_process(POST_BUILD COMMAND ${CMAKE_COMMAND} -E create_symlink ${SFILE} ${CMAKE_BINARY_DIR}/lib/)
  ENDFOREACH()

endfunction( gaugi_finalize )
