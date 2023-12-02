# DKOS need not have the same name that the corresponding Dedukti
# files (modulogic.dk becomes zen.dko) but for each file f.dk, dkdep
# f.dk outputs the name of the produced dko file before the ':'
# character.
DKOS_LIB=$(shell cut -d ':' -f 1 .depend_Lib)
DKOS_2022=$(shell cut -d ':' -f 1 .depend_2022)
DKOS_2023=$(shell cut -d ':' -f 1 .depend_2023)

lib: $(DKOS_LIB)
all: $(DKOS_LIB) $(DKOS_2022) $(DKOS_2023)

BASE_LIB = -I Lib
BASE_2022 = -I Lib -I 2022 -I 2022/Inputs
BASE_2023 = -I Lib -I 2023 -I 2023/Inputs
FLAGS = -e

DKDEP=dk dep
DKCHECK=dk check $(FLAGS)

Lib/%.dko:
	$(DKCHECK) $(BASE_LIB) $< || echo "Pb with" $<

2022/%.dko:
	$(DKCHECK) $(BASE_2022) $< || echo "Pb with" $<

2023/%.dko:
	$(DKCHECK) $(BASE_2023) $< || echo "Pb with" $<

clean:
	rm -f */*.dko */*/*.dko .depend_Lib .depend_2022 .depend_2023

depend: .depend_Lib .depend_2022 .depend_2023
.depend_Lib:
	$(DKDEP) $(BASE_LIB) Lib/*.dk > ./.depend_Lib
.depend_2022:
	$(DKDEP) $(BASE_2022) 2022/*.dk 2022/Inputs/*.dk > ./.depend_2022
.depend_2023:
	$(DKDEP) $(BASE_2023) 2023/*.dk 2023/Inputs/*.dk > ./.depend_2023

-include .depend_Lib .depend_2022 .depend_2023
