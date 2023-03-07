# C++ Streams


### Write to File
```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main () {
    ofstream myfile ("example.txt");
    if (myfile.is_open()) {
        myfile << "This is a line.\n";
        myfile << "This is another line.\n";
        myfile.close();
    }
    else cout << "Unable to open file";
    return 0;
}
```

### Read file token by token
```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
    ifstream myfile ("example.txt");
    if (myfile.is_open()) {
        while (myfile >> temp) {
            cout << temp << ' ';
        }
        myfile.close();
    }
    else cout << "Unable to open file";
    return 0;
}
```

### Read file line by line

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
    string line;
    ifstream myfile ("example.txt");
    if (myfile.is_open()) {
        while ( getline (myfile, line) ) {
            cout << line << '\n';
        }
        myfile.close();
    }
    else cout << "Unable to open file";
    return 0;
}
```


---
#cpp
