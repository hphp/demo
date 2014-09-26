#COMAKE2 edit-mode: -*- Makefile -*-
####################64Bit Mode####################
ifeq ($(shell uname -m),x86_64)
CC=gcc
CXX=g++
CXXFLAGS=
CFLAGS=
CPPFLAGS=
INCPATH=
DEP_INCPATH=

#============ CCP vars ============
CCHECK=@ccheck.py
CCHECK_FLAGS=
PCLINT=@pclint
PCLINT_FLAGS=
CCP=@ccp.py
CCP_FLAGS=


#COMAKE UUID
COMAKE_MD5=25708025340b1defa9895ed768809ed8  COMAKE


.PHONY:all
all:comake2_makefile_check .commit_interface .commit_python_loader .commit_implement .generate_output 
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40mall[0m']"
	@echo "make all done"

.PHONY:comake2_makefile_check
comake2_makefile_check:
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40mcomake2_makefile_check[0m']"
	#in case of error, update 'Makefile' by 'comake2'
	@echo "$(COMAKE_MD5)">comake2.md5
	@md5sum -c --status comake2.md5
	@rm -f comake2.md5

.PHONY:ccpclean
ccpclean:
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40mccpclean[0m']"
	@echo "make ccpclean done"

.PHONY:clean
clean:ccpclean
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40mclean[0m']"
	rm -rf sidb
	rm -rf idl/assembly.tar.gz
	rm -rf idl/assembly.so
	rm -rf .commit_interface
	rm -rf .commit_python_loader
	rm -rf implement.tar.gz
	rm -rf .commit_implement
	rm -rf output
	rm -rf .generate_output

.PHONY:dist
dist:
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40mdist[0m']"
	tar czvf output.tar.gz output
	@echo "make dist done"

.PHONY:distclean
distclean:clean
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40mdistclean[0m']"
	rm -f output.tar.gz
	@echo "make distclean done"

.PHONY:love
love:
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40mlove[0m']"
	@echo "make love done"

.commit_interface:../../../../public/sofa/bin/sofa \
  idl/OnlineDeployService.idl
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40m.commit_interface[0m']"
	rm -rf sidb
	../../../../public/sofa/bin/sofa compile -f -o ./idl/assembly.tar.gz ./idl/OnlineDeployService.idl
	../../../../public/sofa/bin/sofa commit -f ./idl/assembly.tar.gz
	tar xfz ./idl/assembly.tar.gz -C ./idl assembly.so
	touch .commit_interface

.commit_python_loader:../../../../public/sofa/bin/sofa \
  ../../../../public/sofa/lib/python/2.7/sofa.interop.python27.tar.gz \
  .commit_interface
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40m.commit_python_loader[0m']"
	../../../../public/sofa/bin/sofa commit -f ../../../../public/sofa/lib/python/2.7/sofa.interop.python27.tar.gz
	touch .commit_python_loader

.commit_implement:../../../../public/sofa/bin/sofa \
  .commit_interface \
  .commit_python_loader \
  assembly.xml \
  DeployServicePyImp.py \
  __init__.py
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40m.commit_implement[0m']"
	tar cfz implement.tar.gz assembly.xml DeployServicePyImp.py __init__.py
	../../../../public/sofa/bin/sofa commit -f ./implement.tar.gz
	touch .commit_implement

.generate_output:.commit_python_loader
	@echo "[[1;32;40mCOMAKE:BUILD[0m][Target:'[1;32;40m.generate_output[0m']"
	rm -rf output
	mkdir output
	cp ../../../../public/sofa/bin/svchost output
	cp -r sidb output
	cp sofa_config.xml output

endif #ifeq ($(shell uname -m),x86_64)


