# Install script for directory: /Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake

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
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/opencog/cmake/AddCxxtest.cmake;/usr/local/share/opencog/cmake/FindBFD.cmake;/usr/local/share/opencog/cmake/Findcpprest.cmake;/usr/local/share/opencog/cmake/FindCxxtest.cmake;/usr/local/share/opencog/cmake/FindCython.cmake;/usr/local/share/opencog/cmake/FindFolly.cmake;/usr/local/share/opencog/cmake/FindGHC.cmake;/usr/local/share/opencog/cmake/FindGTK3.cmake;/usr/local/share/opencog/cmake/FindGuile.cmake;/usr/local/share/opencog/cmake/FindHyperTable.cmake;/usr/local/share/opencog/cmake/FindIberty.cmake;/usr/local/share/opencog/cmake/FindLibGearman.cmake;/usr/local/share/opencog/cmake/FindLinkGrammar.cmake;/usr/local/share/opencog/cmake/FindMOSES.cmake;/usr/local/share/opencog/cmake/FindMsgPack.cmake;/usr/local/share/opencog/cmake/FindOCaml.cmake;/usr/local/share/opencog/cmake/FindOctomap.cmake;/usr/local/share/opencog/cmake/FindPGSQL.cmake;/usr/local/share/opencog/cmake/FindPthreads.cmake;/usr/local/share/opencog/cmake/FindPython3Interp.cmake;/usr/local/share/opencog/cmake/FindRocksDB.cmake;/usr/local/share/opencog/cmake/FindSIGAR.cmake;/usr/local/share/opencog/cmake/FindStack.cmake;/usr/local/share/opencog/cmake/FindSTLPort.cmake;/usr/local/share/opencog/cmake/FindTBB.cmake;/usr/local/share/opencog/cmake/FindUUID.cmake;/usr/local/share/opencog/cmake/FindVALGRIND.cmake;/usr/local/share/opencog/cmake/FindZMQ.cmake;/usr/local/share/opencog/cmake/OCamlDep.cmake;/usr/local/share/opencog/cmake/OpenCogFindPython.cmake;/usr/local/share/opencog/cmake/OpenCogFindGuile.cmake;/usr/local/share/opencog/cmake/OpenCogGccOptions.cmake;/usr/local/share/opencog/cmake/OpenCogInstallOptions.cmake;/usr/local/share/opencog/cmake/OpenCogLibOptions.cmake;/usr/local/share/opencog/cmake/Summary.cmake;/usr/local/share/opencog/cmake/UseOCaml.cmake;/usr/local/share/opencog/cmake/COPYING-CMAKE-SCRIPTS")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/opencog/cmake" TYPE FILE MESSAGE_LAZY FILES
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/AddCxxtest.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindBFD.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/Findcpprest.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindCxxtest.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindCython.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindFolly.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindGHC.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindGTK3.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindGuile.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindHyperTable.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindIberty.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindLibGearman.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindLinkGrammar.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindMOSES.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindMsgPack.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindOCaml.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindOctomap.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindPGSQL.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindPthreads.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindPython3Interp.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindRocksDB.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindSIGAR.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindStack.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindSTLPort.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindTBB.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindUUID.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindVALGRIND.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/FindZMQ.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/OCamlDep.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/OpenCogFindPython.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/OpenCogFindGuile.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/OpenCogGccOptions.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/OpenCogInstallOptions.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/OpenCogLibOptions.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/Summary.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/UseOCaml.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/COPYING-CMAKE-SCRIPTS"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/CogUtil" TYPE FILE MESSAGE_LAZY FILES
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cmake/CogUtilConfigVersion.cmake"
    "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cmake/CogUtilConfig.cmake"
    )
endif()

