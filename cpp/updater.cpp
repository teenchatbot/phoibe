// I don't know what half this shit does atp
// Copyright Reid Powell
// let's be honest, no one is going to want to use this flaming pile of shit
#include "include/json.hpp"
#include <cstddef>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include "include/curl/curl.h"
#include "include/curl/easy.h"
#include <ostream>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <vector>
#include <zip.h>


using namespace std;
using json = nlohmann::json;
using namespace nlohmann::literals;



// I'm just following the curl tutorial, god please help me
static size_t write_data(void *ptr, size_t size, size_t nmemb, FILE *stream)
{
    size_t written = fwrite(ptr, size, nmemb, stream);
    return written;
}


void download()
{
    // This shit is a massive mess
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
        curl_easy_setopt(curl, CURLOPT_CAINFO, "./cacert.pem");
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);


        std::cout << "Downloading the latest version from GitHub" << std::endl;
        // do the downloading
        res = curl_easy_perform(curl);

        // I give a shit about errors
        if (res != CURLE_OK) {
            std::cerr << "failed to download file" << curl_easy_strerror(res) << std::endl;
        }
        curl_easy_cleanup(curl);
        fclose(fp);
    }
    curl_global_cleanup();
    std::cout << "Done downloading file" << std::endl;
    std::cout << "Unpacking the .zip file" << std::endl;
    // unziping the file
    system("unzip -qq phoibe.zip -d phoibe");
}



int main()
{
    // this shit is an even bigger mess

    download();

    

    std::ifstream file("update.json");



    json data = json::parse(file);
    // setting this to a string for nowm, will change to array later
    // json affected_files = json::array();
    // going ahead and creating the array
    // 105 entries is the current lines in the settings.json file
    // create a list to store the output of the below loop
    std::vector<std::string> affected_files;
    std::vector<std::string> settings;
    bool changed_settings;
    // json-files/settings.json
    std::ifstream old_settings("./../json-files/settings.json");
    json old_settings_data = json::parse(old_settings);
    int counter = 0;
    for (std::string x : data["affected_files"])
    {
        affected_files.push_back(x);
        std::string mv_cmd = "mv ./phoibe/*/" + x + " ./../" + x;
        std::system(mv_cmd.c_str());
        counter++;

    }
    int counter2 = 0;
    for (std::string x : affected_files)
    {
        std::cout << affected_files.at(counter2) << std::endl;

        // THE VERY LAST THING
        counter2++;
    }
    // check if settings.json has been changed
    changed_settings = data["affects_settings"];
    if (changed_settings) {
        json additions = data["settings_to_add"];
        old_settings_data.update(additions, true);
        std::cout << std::setw(2) << old_settings_data << std::endl;
        std::ofstream o("./../json-files/settings.json");
        o << std::setw(4) << old_settings_data << std::endl;
    }
    std::cout << "Settings have finished applying, give me a second to finish up" << std::endl;
    std::system("rm -rf phoibe");
    std::system("rm phoibe.zip");





    std::cout << "Done!" << std::endl;
    std::cout << "You may now restart Phoibe." << std::endl;

}
