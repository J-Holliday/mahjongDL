# include <stdio.h>

int pow(int x, int n) {
	int buf = 1;
	for (int i = 0; i < n; i++) {
		buf *= x;
	}
	return buf;
}

int arctan(int y, int n) {
	int e = 1000000;
	int p = e / y;
	int c = 1;
	int t = p / c;
	int s = t;

	for (int i = 1; i <= n; i++) {
		p = p / (pow(y, 2));
		c += 2;
		t = pow((-1), i) * (p / c);
		s += t;
		printf("i:%d is %d, ", i, t);
		printf("\n");
	}

	return s;
}

int main(void) {

	int a = 5;
	for (int i = 0; i < 10; i++) {
		arctan(a, i);
		//printf("%d\n", arctan(a, i));
	}

	return 0;
}