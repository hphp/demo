#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

#include <curl/curl.h>


char log[1000];
CURL *curl_handle;
static size_t write_data(void *ptr, size_t size, size_t nmemb, void *stream)
{
//	printf("good for u");
	off_t of = 1024;
	CURLcode Ccc = curl_easy_setopt(curl_handle, CURLOPT_MAX_RECV_SPEED_LARGE , (curl_off_t) of);//MAX_RECV_SPEED);
//	printf(":cc%d\n",Ccc);
	int written = fwrite(ptr, size, nmemb, (FILE *)stream);
	int fd = open("d_easy_curl.record",O_WRONLY|O_CREAT|O_APPEND);
	sprintf(log,"written %d\n",written);
	write(fd,log,strlen(log));
	return written;
}

long long length = 0;
size_t getcontentlengthfunc(void *ptr, size_t size, size_t nmemb, void *stream)
{
	int r;
	long len = 0;
	/* _snscanf() is Win32 specific */
	// r = _snscanf(ptr, size * nmemb, "Content-Length: %ld\n", &len);
	char * p = (char*)ptr;
	r = sscanf(p, "Content-Length: %ld\n", &len);
	if (r) /* Microsoft: we don't read the specs */{
		*((long *) stream) = len;
		length = len;
		printf("len:%zu\n",length);
	}

	return size * nmemb;
}

long TRANSFER_TIMEOUT = 100;
long CONNECT_TIMEOUT = 1;
curl_off_t MAX_RECV_SPEED = 10;//1024*1024;

char HEADER_HOST[1024]="Host: ";

int main(void)
{

	printf("d:%d,u:%u,zu:%zu,lf:%lf\n",MAX_RECV_SPEED,MAX_RECV_SPEED,MAX_RECV_SPEED,MAX_RECV_SPEED);

	static const char *bodyfilename = "body";
	FILE *bodyfile;

	struct curl_slist * slist = NULL;
	strcat(HEADER_HOST,"dlql.qq.com");
	slist = curl_slist_append(slist,HEADER_HOST);

	curl_global_init(CURL_GLOBAL_NOTHING);

	/* init the curl session */ 
	curl_handle = curl_easy_init();

	/* set URL to get */ 
	//char url[1000] = "dlql.qq.com/dlied1.qq.com/iedvip/dnf/full/DNF_SEASON3_OB_V6.068_Full.exe";
	char url[1000] = "113.105.73.196/dlied1.qq.com/h2/full/qqxlinstaller_1.1.22.8.exe";
	CURLcode Ccc;
//	while(scanf("%s",url) != EOF){
	{
		//char url[1000] = "113.105.73.196/dlied1.qq.com/h2/full/qqxlinstaller_1.1.22.8.exe";
		int cnt = 0;
		Ccc = curl_easy_setopt(curl_handle, CURLOPT_URL, url);
		printf("hey:cc%d\n",Ccc);
		Ccc = curl_easy_setopt(curl_handle, CURLOPT_HTTPHEADER, slist);
		printf("hey:cc%d\n",Ccc);
//		curl_easy_setopt(curl_handle, CURLOPT_TIMEOUT, TRANSFER_TIMEOUT);
		//curl_easy_setopt(curl_handle, CURLOPT_BUFFERSIZE , MAX_RECV_SPEED);
		off_t of = 1024;
		Ccc = curl_easy_setopt(curl_handle, CURLOPT_MAX_RECV_SPEED_LARGE , MAX_RECV_SPEED);//MAX_RECV_SPEED);
		printf("hey:cc%d\n",Ccc);
		Ccc = curl_easy_setopt(curl_handle, CURLOPT_MAX_RECV_SPEED_LARGE , (curl_off_t) MAX_RECV_SPEED);//MAX_RECV_SPEED);
		printf("hey:cc%d\n",Ccc);
		Ccc = curl_easy_setopt(curl_handle, CURLOPT_MAX_RECV_SPEED_LARGE , 1023);//MAX_RECV_SPEED);
		printf("hey:cc%d\n",Ccc);
		Ccc = curl_easy_setopt(curl_handle, CURLOPT_MAX_RECV_SPEED_LARGE , (off_t)1023);//MAX_RECV_SPEED);
		printf("hey:cc%d\n",Ccc);
		Ccc = curl_easy_setopt(curl_handle, CURLOPT_MAX_RECV_SPEED_LARGE , of);//MAX_RECV_SPEED);
		printf("hey:cc%d\n",Ccc);
		Ccc = curl_easy_setopt(curl_handle, CURLOPT_MAX_RECV_SPEED_LARGE , (curl_off_t) of);//MAX_RECV_SPEED);
		printf("hey:cc%d\n",Ccc);
		Ccc = curl_easy_setopt(curl_handle, CURLOPT_LOW_SPEED_LIMIT
, (curl_off_t) of);//MAX_RECV_SPEED);

		printf("hey:cc%d\n",Ccc);
	//	curl_easy_setopt(curl_handle, CURLOPT_CONNECTTIMEOUT, CONNECT_TIMEOUT);

	//	curl_easy_setopt(curl_handle, CURLOPT_NOPROGRESS, 1L);

		curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, write_data);
/*
		int bfd = open(bodyfilename,O_RDONLY|O_CREAT);
		off_t resume_from = lseek(bfd, 0, SEEK_END);
		printf("%d,%lld\n",bfd,resume_from);
		close(bfd);
		curl_easy_setopt(curl_handle, CURLOPT_RESUME_FROM_LARGE, resume_from);
*/
		bodyfile = fopen(bodyfilename,"w");
		if (bodyfile == NULL) {
			curl_easy_cleanup(curl_handle);
			return -1;
		}

		Ccc = curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, bodyfile);
		printf("hey:cc%d\n",Ccc);

		Ccc = curl_easy_perform(curl_handle);
		printf("hey:cc%d\n",Ccc);

		double x;
		CURLcode Cc = curl_easy_getinfo(curl_handle,CURLINFO_SPEED_DOWNLOAD,&x);
		printf("%.0lf,%d\n",x,Cc);

		fclose(bodyfile);
	}

	/* cleanup curl stuff */ 
	curl_slist_free_all(slist);
	curl_easy_cleanup(curl_handle);

	return 0;
}


