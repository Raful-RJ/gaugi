

function(gaugi_build_directories)
  file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/python)
  file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
endfunction(gaugi_build_directories)


function(gaugi_install_python_modules filepath module)
  message(STATUS "${filepath} -> ${CMAKE_BINARY_DIR}/python/${module}")
    execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink ${filepath} ${CMAKE_BINARY_DIR}/python/${module})
endfunction(gaugi_install_python_modules)


