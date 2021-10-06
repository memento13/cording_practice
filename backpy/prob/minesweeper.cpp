#pragma warning (disable:4996)
#include <stdio.h>
#define MAX 100

int main(){
    int n;
    char grid[MAX][MAX];
    int offset[][2] = {{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1}};
    FILE *fp = fopen("input.txt","r");
    fscanf(fp,"%d ",&n);
    for (int i = 0; i<n; i++){
        for(int j = 0; j<n;j++){
            fscanf(fp,"%c ", &grid[i][j]);
        }
    }
    fclose(fp);

    for(int i = 0; i<n;i++){
        for(int j = 0; j<n; j++){
            if(grid[i][j] =='*'){
                printf("* ");
            }
            else{
                int count = 0;
                for(int dir = 0;dir<8;dir++){
                    int r = i + offset[dir][0];
                    int c = j + offset[dir][0];
                    if(r>=0 && r<n && c>=0 && c<n && grid[r][c] == '*'){
                        count++;
                    }
                }
                printf("%d ",count);
            }
        }
        printf("\n");
    }

    for(int i = 0; i<n; i++){
        for (int j = 0; j<n;j++){
            printf("%c ",grid[i][j]);
        }
        printf("\n");
    }

    getchar();getchar();
    return 0;
}
