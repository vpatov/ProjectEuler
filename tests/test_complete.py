import os
from colorama import Fore as clr
programs = sorted(filter(
    lambda name: name not in ['__init__', '__pycache__'], [
        os.path.basename(os.path.splitext(fname)[0])
        for fname in os.listdir(os.path.join('..', 'projecteuler', 'complete'))
    ])
)

failed_programs = []
for p in programs:
    try:
        print(clr.CYAN + "-------- Executing {} --------".format(p) + clr.RESET)
        exec('import projecteuler.complete.%s' % p)
        print(clr.LIGHTGREEN_EX + "----------- Success ------------\n" + clr.RESET)
    except Exception as e:
        print(e)
        print(clr.RED + "----------- Failure ------------\n" + clr.RESET)
        failed_programs.append(p)


print(clr.CYAN + "Tested {} programs.".format(len(programs)) + clr.RESET)
if failed_programs:
    print(clr.LIGHTGREEN_EX + "{} programs passed.".format(len(programs) -
                                                           len(failed_programs)) + clr.RESET)
    print(clr.RED + "{} programs failed:".format(len(failed_programs)) +
          clr.MAGENTA + ', '.join(failed_programs) + clr.RESET)

else:
    print(clr.LIGHTGREEN_EX + "All programs passed!" + clr.RESET)
