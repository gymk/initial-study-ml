import sys
import agate
import agateexcel

itable = agate.Table.from_xlsx(sys.argv[1])
itable.to_csv(sys.argv[2])
