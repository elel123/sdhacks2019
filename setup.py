import cx_Freeze

executables = [cx_Freeze.Executable("CompostGameLoop.py")]

cx_Freeze.setup(
    name="iCompost",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["Images"]}},
    executables = executables

    )