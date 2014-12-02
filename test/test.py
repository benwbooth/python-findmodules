#!/usr/bin/env python3
import findmodules, sys
findmodules.init(base='src', realpath=True, append=True)
print("sys.path={}".format(sys.path))
