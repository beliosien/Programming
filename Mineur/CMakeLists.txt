file(GLOB_RECURSE Sources *.cpp)
file(GLOB_RECURSE Headers *.hpp)

add_executable(Mineur ${Sources} ${Headers})
target_compile_options(Mineur PRIVATE ${WARNING_FLAGS})

target_link_libraries(Mineur PRIVATE 
    common_cpp_lib
    pthread
    ssl
    crypto
    cppkafka
    boost_program_options
    sqlite3
)