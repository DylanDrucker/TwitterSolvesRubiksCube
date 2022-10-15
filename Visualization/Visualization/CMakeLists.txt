cmake_minimum_required(VERSION 3.23)
project(Visualization)

set(CMAKE_CXX_STANDARD 14)

find_package(SFML 2.5 COMPONENTS graphics audio REQUIRED)
add_executable(Visualization main.cpp)
target_link_libraries(Visualization sfml-graphics sfml-audio)