# This file will be configured to contain variables for CPack. These variables
# should be set in the CMake list file of the project before CPack module is
# included. The list of available CPACK_xxx variables and their associated
# documentation may be obtained using
#  cpack --help-variable-list
#
# Some variables are common to all generators (e.g. CPACK_PACKAGE_NAME)
# and some are specific to a generator
# (e.g. CPACK_NSIS_EXTRA_INSTALL_COMMANDS). The generator specific variables
# usually begin with CPACK_<GENNAME>_xxxx.


set(CPACK_BUILD_SOURCE_DIRS "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil;/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build")
set(CPACK_CMAKE_GENERATOR "Unix Makefiles")
set(CPACK_COMPONENT_UNSPECIFIED_HIDDEN "TRUE")
set(CPACK_COMPONENT_UNSPECIFIED_REQUIRED "TRUE")
set(CPACK_DEBIAN_PACKAGE_DEPENDS "libboost-filesystem-dev (>= 1.60), libboost-math-dev (>= 1.60), libboost-program-options-dev (>= 1.60), libboost-thread-dev (>= 1.60), libboost-system-dev (>= 1.60), libstdc++6 (>= 4.7), binutils-dev, libiberty-dev")
set(CPACK_DEBIAN_PACKAGE_HOMEPAGE "http://opencog.org")
set(CPACK_DEBIAN_PACKAGE_SECTION "libdevel")
set(CPACK_DEFAULT_PACKAGE_DESCRIPTION_FILE "/Applications/CMake.app/Contents/share/cmake-3.25/Templates/CPack.GenericDescription.txt")
set(CPACK_DEFAULT_PACKAGE_DESCRIPTION_SUMMARY "cogutil built using CMake")
set(CPACK_DMG_SLA_USE_RESOURCE_FILE_LICENSE "ON")
set(CPACK_GENERATOR "TBZ2;TGZ;TXZ;TZ")
set(CPACK_IGNORE_FILES "/CVS/;/\\.svn/;/\\.bzr/;/\\.hg/;/\\.git/;\\.swp\$;\\.#;/#")
set(CPACK_INSTALLED_DIRECTORIES "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil;/")
set(CPACK_INSTALL_CMAKE_PROJECTS "")
set(CPACK_INSTALL_PREFIX "/usr/local")
set(CPACK_MODULE_PATH "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/cmake/")
set(CPACK_NSIS_DISPLAY_NAME "libcogutil-dev 2.0.3-20221027")
set(CPACK_NSIS_INSTALLER_ICON_CODE "")
set(CPACK_NSIS_INSTALLER_MUI_ICON_CODE "")
set(CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES")
set(CPACK_NSIS_PACKAGE_NAME "libcogutil-dev 2.0.3-20221027")
set(CPACK_NSIS_UNINSTALL_NAME "Uninstall")
set(CPACK_OBJDUMP_EXECUTABLE "/Library/Developer/CommandLineTools/usr/bin/objdump")
set(CPACK_OSX_SYSROOT "/Library/Developer/CommandLineTools/SDKs/MacOSX12.3.sdk")
set(CPACK_OUTPUT_CONFIG_FILE "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/CPackConfig.cmake")
set(CPACK_PACKAGE_CONTACT "opencog@googlegroups.com")
set(CPACK_PACKAGE_DEFAULT_LOCATION "/")
set(CPACK_PACKAGE_DESCRIPTION_FILE "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/README.md")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "The OpenCog Basic C++ Utilities")
set(CPACK_PACKAGE_DIRECTORY "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/packages")
set(CPACK_PACKAGE_FILE_NAME "libcogutil-dev-2.0.3-20221027-Source")
set(CPACK_PACKAGE_INSTALL_DIRECTORY "libcogutil-dev 2.0.3-20221027")
set(CPACK_PACKAGE_INSTALL_REGISTRY_KEY "libcogutil-dev 2.0.3-20221027")
set(CPACK_PACKAGE_NAME "libcogutil-dev")
set(CPACK_PACKAGE_RELOCATABLE "true")
set(CPACK_PACKAGE_VENDOR "opencog.org")
set(CPACK_PACKAGE_VERSION "2.0.3-20221027")
set(CPACK_PACKAGE_VERSION_MAJOR "0")
set(CPACK_PACKAGE_VERSION_MINOR "1")
set(CPACK_PACKAGE_VERSION_PATCH "1")
set(CPACK_PACKAGING_INSTALL_PREFIX "/usr/local")
set(CPACK_RESOURCE_FILE_LICENSE "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil/LICENSE")
set(CPACK_RESOURCE_FILE_README "/Applications/CMake.app/Contents/share/cmake-3.25/Templates/CPack.GenericDescription.txt")
set(CPACK_RESOURCE_FILE_WELCOME "/Applications/CMake.app/Contents/share/cmake-3.25/Templates/CPack.GenericWelcome.txt")
set(CPACK_RPM_PACKAGE_SOURCES "ON")
set(CPACK_SET_DESTDIR "OFF")
set(CPACK_SOURCE_GENERATOR "TBZ2;TGZ;TXZ;TZ")
set(CPACK_SOURCE_IGNORE_FILES "/CVS/;/\\.svn/;/\\.bzr/;/\\.hg/;/\\.git/;\\.swp\$;\\.#;/#")
set(CPACK_SOURCE_INSTALLED_DIRECTORIES "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/cogutil;/")
set(CPACK_SOURCE_OUTPUT_CONFIG_FILE "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/CPackSourceConfig.cmake")
set(CPACK_SOURCE_PACKAGE_FILE_NAME "libcogutil-dev-2.0.3-20221027-Source")
set(CPACK_SOURCE_RPM "OFF")
set(CPACK_SOURCE_TBZ2 "ON")
set(CPACK_SOURCE_TGZ "ON")
set(CPACK_SOURCE_TOPLEVEL_TAG "Darwin-Source")
set(CPACK_SOURCE_TXZ "ON")
set(CPACK_SOURCE_TZ "ON")
set(CPACK_SOURCE_ZIP "OFF")
set(CPACK_STRIP_FILES "")
set(CPACK_SYSTEM_NAME "Darwin")
set(CPACK_THREADS "1")
set(CPACK_TOPLEVEL_TAG "Darwin-Source")
set(CPACK_WIX_SIZEOF_VOID_P "8")

if(NOT CPACK_PROPERTIES_FILE)
  set(CPACK_PROPERTIES_FILE "/Users/yuezhen/Desktop/SMU/CCA/Hackathon/code/superDUR/packages/build/CPackProperties.cmake")
endif()

if(EXISTS ${CPACK_PROPERTIES_FILE})
  include(${CPACK_PROPERTIES_FILE})
endif()
