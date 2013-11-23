HP_COM = ../HpCommonFiles
IPD_COM = ../special_f_for_ip_distribution
COSS_API_COM = /root/happyhan/ipd_common/ic_q.cpp /root/happyhan/ipd_common/ic_r.cpp /root/happyhan/ipd_common/ipd_log_api.cpp \
			   /root/happyhan/ipd_common/coss_svr_api.cpp
COSS_CONFIG_SVR_COM = ../coss_config_src
IPD_GET_DATA = /root/happyhan/ipd_common/get_data_api.cpp
#IPD_FORM = /root/happyhan/ipd_common/ipd_form.cpp
INCFLGS= \
		-I/root/happyhan/include \
		 -I./ -I/usr/local/mysql/include -I/usr/local/include -I../lib -I../HpCommonFiles -I./ -I../special_f_for_ip_distribution \
		-I/root/happyhan/ipd_common \
		-I/root/happyhan/coss_config_src \
		-I/root/happyhan/common
LIB=-L. -L/usr/local/lib -L/usr/local/mysql/lib -L/usr/lib -lmysqlclient -lz -lcurl -lwsapi -lwsoa -lgsoap -lgsl -lgslcblas
#../lib/libwsapi.a  ../lib/libwsoa.a  ../lib/libwsoap.a
CFLAGS= -g -o
SELF_API = dccci.cpp
COM = /root/happyhan/common

%: $(HP_COM)/*.cpp $(HP_DATA_RELY) %.cpp $(SELF_API) $(IPD_GET_DATA) $(COSS_API_COM) $(COSS_CONFIG_SVR_COM)/*.cpp $(IPD_COM)/*.cpp $(COM)/*.cpp
	g++ -g $^ $(INCFLGS) $(LIB) $(CFLAGS) $@
	cp $@ /usr/local/apache2/cgi-bin/ip_distribution/
clean:
	rm -f $(COM_OBJS) $(BIN) *.o
deploy:
#	-mv /usr/local/apache2/cgi-bin/fluxplan/glsb-backup /usr/local/apache2/cgi-bin/fluxplan/gslb-backup.bak
#	cp db /usr/local/apache2/cgi-bin/fluxplan/gslb-backup
py:
	cp *.py /usr/local/apache2/cgi-bin/ip_distribution/
	chmod +x /usr/local/apache2/cgi-bin/ip_distribution/*.py
