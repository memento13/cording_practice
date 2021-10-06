#pragma warning (disable:4996)
#include <stdio.h>
#define MAX 100

int main() {
	int p, q,q2, r;
	int A[MAX][MAX];
	int B[MAX][MAX];
	int C[MAX][MAX];

	FILE *fp = fopen("input.txt", "r");

	fscanf(fp, "%d", &p);
	fscanf(fp, "%d", &q);

	for (int i = 0; i < p; i++) {
		for (int j = 0; j < q; j++) {
			fscanf(fp, "%d", &A[i][j]);
		}
	}

	fscanf(fp, "%d", &q2);
	fscanf(fp, "%d", &r);

	if (q != q2){
		printf("Wrong size \n");
		return 0;
	}

	for (int i = 0; i < q2; i++) {
		for (int j = 0; j < r; j++) {
			fscanf(fp, "%d", &B[i][j]);
		}
	}

	// C = AB

	for (int i = 0; i < p; i++) {
		for(int j = 0; j<r;j++){

            C[i][j] = 0;
            for(int k = 0; k<q;k++){
                C[i][j] += A[i][k]*B[k][j];
            }
		}
	}
    fclose(fp);

    for(int i = 0; i<p;i++){
        for(int j = 0; j<r; j++){
            printf("%d ",C[i][j]);
        }
        printf("\n");
    }

	getchar(); getchar();
	return 0;
}