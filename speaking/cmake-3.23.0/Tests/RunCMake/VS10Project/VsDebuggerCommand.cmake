enable_language(CXX)
add_library(foo foo.cpp)
add_custom_target(bar)

set_target_properties(foo bar PROPERTIES
    VS_DEBUGGER_COMMAND "my-debugger-command $<TARGET_PROPERTY:foo,NAME>")
