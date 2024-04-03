// I don't know what half this shit does atp
#include "include/json.hpp"
#include <cstddef>
#include <iostream>
#include <fstream>
#include "include/curl/curl.h"
#include "include/curl/easy.h"
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


using namespace std;
using json = nlohmann::json;

// I'm just following the curl tutorial, god please help me
static size_t write_data(void *ptr, size_t size, size_t nmemb, FILE *stream)
{
    size_t written = fwrite(ptr, size, nmemb, stream);
    return written;
}


void download()
{
    CURL *curl;
    FILE *fp;
    CURLcode res;

    // url of the latest version of phoibe
    const char *url = "https://github.com/teenchatbot/phoibe/releases/latest/download/phoibe.zip";
    // save that shit as phoibe.zip
    const char *output_file = "phoibe.zip";

    // init curl
    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    if (curl)
    {
        fp = fopen(output_file, "wb");
        if (fp == NULL)
        {
            std::cerr << "error opening file" << std::endl;
        }

        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0);
        curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);

        res = curl_easy_perform(curl);

        // I give a shit about errors
        if (res != CURLE_OK) {
            std::cerr << "failed to download file" << curl_easy_strerror(res) << std::endl;
        }
        curl_easy_cleanup(curl);
        fclose(fp);
    }
    curl_global_cleanup();
}


int main()
{
    download();


    std::cout << "Done!" << std::endl;

}
