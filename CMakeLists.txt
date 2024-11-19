cmake_minimum_required(VERSION 3.10)

# Project name
project(anolang)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add source files
file(GLOB_RECURSE FRONTEND_SOURCES "${CMAKE_SOURCE_DIR}/frontend/*.cpp")

# Add executable target (note the change in the executable name)
add_executable(anolang-test test_all.cpp ${FRONTEND_SOURCES})

# Include directories (if needed)
include_directories(${CMAKE_SOURCE_DIR}/frontend)

# Optional: Add additional libraries if necessary
# target_link_libraries(anolang-test <library_name>)

# Add a custom target for cleaning
add_custom_target(clean-all
    COMMAND ${CMAKE_COMMAND} -E rm -rf ${CMAKE_BINARY_DIR}/*
    COMMENT "Cleaning all build files..."
)

# Print a message when configuring
message(STATUS "CMake configured for anolang project")
