#include <stdio.h>

#define MAX_LINE_SIZE 1024

int my_getline(char line[], int maxline);
void copy(char to[], char from[]);

/* Print the longest line */
int main() {
	int len, max;
	char line[MAX_LINE_SIZE], longest[MAX_LINE_SIZE];

	max = 0;
	while ((len = my_getline(line, MAX_LINE_SIZE)) > 0) {
		if (len > max) {
			max = len;
			copy(longest, line);
		}
	}
	if (max > 0) {
		printf("%s", longest);
	}

	return 0;
}

int my_getline(char line[], int limit) {
	int c, i;
	for (i = 0; i < limit - 1 && (c = getchar()) != EOF && c != '\n'; i++) {
		line[i] = c;
	}
	if (c == '\n') {
		line[i] = c;
		i++;
	}
	line[i] = '\0';
	return i;
}

void copy(char to[], char from[]) {
	int i;
	i = 0;
	while ((to[i] = from[i]) != '\0') {
		i++;
	}
}
