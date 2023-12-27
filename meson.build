project(
    'valloc',
    'cpp',
    version: '0.1.0',
    default_options: [
        'warning_level=3', 'cpp_std=c++20',
        'cpp_args=-O3 -flto -march=native',
    ]
)

# cpp = meson.get_compiler('cpp')

# Uncomment the following line to enable profiling
# add_project_arguments('-pg', language: 'cpp')

# executable('valloc',
#            'main.cpp',
#            # dependencies: [cpp.find_library('pthread')]
# )

valloc_include = include_directories('include')
bc_include = include_directories('backward-cpp/')
ut_include = include_directories('ut/include')
test_files = run_command(
    'python3', 'scripts/list_tests.py', check: true
    ).stdout().strip().split('\n')

test('valloc-tests',
     executable('test_bin', test_files,
                include_directories: [
                    ut_include,
                    'tests',
                    valloc_include,
                    bc_include,
                    ],
                cpp_args: [
                    '-O3', '-g', '-march=native',
                    '-flto',
                    # '-ldl', '-lbfd'
                    ],
                link_args: [
                    '-flto',
                    # '-ldl', '-lbfd'
                    ],
     )
)

