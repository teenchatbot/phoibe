#include <cstring>
#include <iostream>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

using namespace std;
int main()
{
    ssize_t bytesRecievedBuffer;
    // Create the socket
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);


    // specify the address
    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(8080);
    serverAddress.sin_addr.s_addr = INADDR_ANY;


    // binding the socket
    bind(serverSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress)); // If you're using nvim or any other linter, this line will throw a warning, ignore it, it shouldnt return any value at all (I think)

    // listening to the assigned socket
    listen(serverSocket, 5);
    while (true)
    {
        // accepting connection request
        int clientSocket = accept(serverSocket, nullptr, nullptr);

        // recieving data ( I know i spelled that wrong)
        // sticking this in a while true loop
        bool isEmpty = true;
        char buffer[1024] = { 0 };
        memset(buffer, 0, sizeof(buffer));
        ssize_t bytesRecieved;
        bytesRecieved = recv(clientSocket, buffer, sizeof(buffer), 0);
        if (bytesRecieved > 0) {
            if (bytesRecieved != bytesRecievedBuffer)
                std::cout << "Message from client: " << buffer << endl;
            bytesRecievedBuffer = bytesRecieved;
        }
        // return 0, because I don't know why

    }
}
