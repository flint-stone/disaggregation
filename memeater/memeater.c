#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include <unistd.h>


int main(int argc, char** argv) {
    int max = -1;
    int mb = 0;
    char* buffer;

    if(argc > 1)
        max = atoi(argv[1]);

    //while((buffer=malloc(1024*1024*1024)) != NULL && mb != max) {
    	
    while((buffer=malloc(1024*1024)) != NULL && mb != max){
    	memset(buffer, 1, 1024*1024);
        mb+=1;
	if (mb%1024==0)
		printf("Allocated %d MB\n", mb);
        //sleep(1);
    }      
    return 0;
}
