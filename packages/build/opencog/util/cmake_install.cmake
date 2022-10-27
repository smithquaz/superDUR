# Install script for directory: /Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/Library/Developer/CommandLineTools/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencog/util" TYPE FILE MESSAGE_LAZY FILES
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/ansi.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/algorithm.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/async_buffer.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/async_method_caller.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/backtrace-symbols.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/based_variant.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/cluster.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/cogutil.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/comprehension.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/Config.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/Counter.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/Cover_Tree.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/concurrent_queue.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/concurrent_set.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/concurrent_stack.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/digraph.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/dorepeat.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/empty_string.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/exceptions.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/files.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/functional.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/hashing.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/iostreamContainer.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/jaccard_index.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/KLD.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/lazy_normal_selector.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/lazy_random_selector.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/lazy_selector.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/log_prog_name.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/Logger.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/lru_cache.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/macros.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/MannWhitneyU.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/misc.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/mt19937ar.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/numeric.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/oc_assert.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/oc_omp.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/octime.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/platform.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/pool.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/RandGen.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/random.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/ranking.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/recent_val.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/selection.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/sigslot.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/StringTokenizer.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/tree.h"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/opencog/util/zipf.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/opencog/util/libcogutil.dylib")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcogutil.dylib" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcogutil.dylib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" -x "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcogutil.dylib")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/opencog/util/boost_ext/cmake_install.cmake")

endif()

