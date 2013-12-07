
import d_be_imported
import numpy

print d_be_imported.a
d_be_imported.change_global()
print d_be_imported.a

d_be_imported.a = 50
print d_be_imported.a
d_be_imported.show_global()
