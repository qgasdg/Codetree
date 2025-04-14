#include <iostream>
#include <vector>

using namespace std;

int n, cnt{0};
void fill(int idx) {
    if (idx == n) {
        cnt++;
        return;
    }
    if (idx > n) return;
    for (int i = 1; i <= 4; i++) { // fill idx
        fill(idx + i);
    }
}

int main() {
    cin >> n;
    fill(0);
    cout << cnt << "\n";
}