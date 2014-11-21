/* A message passing algorithm for de-noising images.
 * This program
 * Run with
 * $ make (or make clean; make)
 * $ ./message [INPUT-FILE] [N-VALUE] [THETA] [MU]
 * 
 * N-VALUE: the number of iterations to run
 * THETA (0.0 - 1.0): the influence that the color of a cell's neighbors have on its coloring
 * MU (0.0 - 1.0): percentage of cells to flip when noising. 
 */
   
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define LEFT 0
#define UP 1
#define RIGHT 2
#define DOWN 3
#define TOP 4

int N;
float theta;

/* 
typedef struct node{
  // array vals for left, up, right, down, top
  float *ms[2];
} node;


/* Pretty print a matrix */
void printM(int **m, int n) {
  int i, j;
  printf("\n");
  for (i = 0; i < n; i++) {
    for (j = 0; j < n ; j++) {
      printf("%i ", m[i][j]);
    }
    printf("\n");
  }
  printf("\n\n\n");
}


/* Compare two n x n matrices
 * returns number of mismatches */
int compareM(int **a, int **b, int n) {
  int err = 0;
  int i, j;
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      if (a[i][j] != b[i][j]) {
	err++;
	//fprintf(stderr, "Mismatch at [%d, %d]\n", i, j);
      }
    }
  }
  //fprintf(stderr, "There were [ %d ] mismatches.\n", err);
  return err;
}

/* Read in a matrix from specified file and store in given matrix m */
void readM(int **m, char *fname)
{
    int data;
    int i, j;
    FILE *src = fopen(fname, "r");

    //printf("\n=====================\nLoading Matrix\n=====================\n");
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            fscanf(src, "%d", &data);
            m[i][j] = data;
	} 
    }
    fclose(src);
}


/* Output matrix to the specified file */
void writeM(int **m, char *fname, int n) 
{
  int i, j;
  FILE *dst = fopen(fname, "w");

  if (!dst) 
    {
      fprintf(stderr, "Unable to open file\n");
      exit(1);
    }    
  
  for (i = 0; i < n; i++) 
    {
      for (j = 0; j < n; j++) 
	{
	  fprintf(dst, "%i ", m[i][j]);
	}
      fprintf(dst, "\n");
    }
  fclose(dst);
}

/* Return a new int matrix */
int **newM() 
{
  int i;
  int **new = (int **)malloc(sizeof(int *)*N);
  for (i = 0; i < N; i++) {
    new[i] = (int *)malloc(sizeof(int)*N);
  }
  return new;
}

/* Initialize a node */
void initNode(node *new) 
{
  int i, j;
  for (i = 0; i < N; i++) 
    {
      new->ms[0] = (float *)malloc(sizeof(float)*5);
      new->ms[1] = (float *)malloc(sizeof(float)*5);
      for (j = 0; j < 5; j++) {
	new->ms[0][j] = 1;
	new->ms[1][j] = 1;
      }
    } 
}

/* Create a new node */
node **newNodeM() 
{
  int i, j;
  node **new = (node **)malloc(sizeof(node *)*N);
  for (i = 0; i < N; i++) {
    new[i] = (node *)malloc(sizeof(node)*N);
    for (j = 0; j < N; j++) {
      initNode(new[i]+j);
    } 
  }
  return new;
}


/* Calculate one unnormalized message from node a for (node b = val) */
float unnormed(node *a, float val, int type) 
{
  int i;
  float p0 = 1;
  float p1 = 1;
  
  for (i = 0; i < 5; i++) {
    p0 *= a->ms[0][i];
    p1 *= a->ms[1][i];
  }

  p0 /= a->ms[0][type];
  p1 /= a->ms[1][type];
  
  p0 *= 1 + pow(-1, (val != 0))*theta;
  p1 *= 1 + pow(-1, (val != 1))*theta;

  return (p0 + p1) - (a->ms[0][0] < 0)*(p0 + p1 - 1);
}


/* update nodes, for each node update messages received from neighbors */
int update(node **odd, node **even)
{
  int i, j;
  float tmp0, tmp1;
  node *curr, *old;
  float max = 0;

  /* update odd from even */
  for (i = 1; i < N-1; i++) 
    {
      for (j = 1; j < N-1; j++) 
	{
	  curr = odd[i]+j;
	  /* Left */
	  tmp0 = unnormed(&even[i][j-1], 0, RIGHT);
	  tmp1 = unnormed(&even[i][j-1], 1, RIGHT);
	  curr->ms[0][LEFT] = tmp0/(tmp0 + tmp1);
	  curr->ms[1][LEFT] = tmp1/(tmp0 + tmp1);

	  /* Up */ 
	  tmp0 = unnormed(&even[i-1][j], 0, DOWN);
	  tmp1 = unnormed(&even[i-1][j], 1, DOWN);
	  curr->ms[0][UP] = tmp0/(tmp0 + tmp1);
	  curr->ms[1][UP] = tmp1/(tmp0 + tmp1);

	  /* Right */
	  tmp0 = unnormed(&even[i][j+1], 0, LEFT);
	  tmp1 = unnormed(&even[i][j+1], 1, LEFT);
	  curr->ms[0][RIGHT] = tmp0/(tmp0 + tmp1);
	  curr->ms[1][RIGHT] = tmp1/(tmp0 + tmp1);

	  /* Down */
	  tmp0 = unnormed(&even[i+1][j], 0, UP);
	  tmp1 = unnormed(&even[i+1][j], 1, UP);
	  curr->ms[0][DOWN] = tmp0/(tmp0 + tmp1);
	  curr->ms[1][DOWN] = tmp1/(tmp0 + tmp1);
	}
    }
  /* update even from odd */
  for (i = 1; i < N-1; i++) 
    {
      for (j = 1; j < N-1; j++) 
	{
	  old = odd[i]+j;
	  curr = even[i]+j;
	  /* Left */
	  tmp0 = unnormed(&odd[i][j-1], 0, RIGHT);
	  tmp1 = unnormed(&odd[i][j-1], 1, RIGHT);
	  curr->ms[0][LEFT] = tmp0/(tmp0 + tmp1);
	  curr->ms[1][LEFT] = tmp1/(tmp0 + tmp1);
	  max = fmax(max, fabs(curr->ms[0][LEFT] - old->ms[0][LEFT]));
	  max = fmax(max, fabs(curr->ms[1][LEFT] - old->ms[1][LEFT]));

	  /* Up */ 
	  tmp0 = unnormed(&odd[i-1][j], 0, DOWN);
	  tmp1 = unnormed(&odd[i-1][j], 1, DOWN);
	  curr->ms[0][UP] = tmp0/(tmp0 + tmp1);
	  curr->ms[1][UP] = tmp1/(tmp0 + tmp1);
	  max = fmax(max, fabs(curr->ms[0][UP] - old->ms[0][UP]));
	  max = fmax(max, fabs(curr->ms[1][UP] - old->ms[1][UP]));

	  /* Right */
	  tmp0 = unnormed(&odd[i][j+1], 0, LEFT);
	  tmp1 = unnormed(&odd[i][j+1], 1, LEFT);
	  curr->ms[0][RIGHT] = tmp0/(tmp0 + tmp1);
	  curr->ms[1][RIGHT] = tmp1/(tmp0 + tmp1);
	  max = fmax(max, fabs(curr->ms[0][RIGHT] - old->ms[0][RIGHT]));
	  max = fmax(max, fabs(curr->ms[1][RIGHT] - old->ms[1][RIGHT]));

	  /* Down */
	  tmp0 = unnormed(&odd[i+1][j], 0, UP);
	  tmp1 = unnormed(&odd[i+1][j], 1, UP);
	  curr->ms[0][DOWN] = tmp0/(tmp0 + tmp1);
	  curr->ms[1][DOWN] = tmp1/(tmp0 + tmp1);
	  max = fmax(max, fabs(curr->ms[0][DOWN] - old->ms[0][DOWN]));
	  max = fmax(max, fabs(curr->ms[1][DOWN] - old->ms[1][DOWN]));
	}
    }
  return (max > 0.01);
}


/* Makes an image noisy */
int **noisify(int **m, float mu)
{
  int i, j;
  int **new = newM();
  unsigned int iseed = (unsigned int)time(NULL);
  srand(iseed);

  for (i = 0; i < N; i++) 
    {
      for(j = 0; j < N; j++)
	{
	  new[i][j] = pow(m[i][j]-((rand()/(double)RAND_MAX) < mu), 2);
	}
    }
  return new;
}


int main(int argc, char *argv[]) 
{
  int i, j, k, tmp;
  float tmp0, tmp1;

  if (argc != 5) {
    fprintf(stderr, "Error: too few arguments. Program expects 4 args: input file name, N value, THETA value, MU value.\n");
    exit(1);
  }
  
  /* Get parameters */
  char *in = argv[1];
  N = atoi(argv[2]);
  float total = pow(N, 2);
  theta = atof(argv[3]);
  float mu = atof(argv[4]);

  //printf("INPUT =  %s\nN = %d\nTHETA = %f\n", in, N, theta);

  /* working matrices */
  int **src = newM();
  readM(src, in);
  //printM(src, N);

  int **obs = noisify(src, mu);
  //printM(obs, N);
  int **res = newM();

  N += 2;
  node **even = newNodeM();
  node **odd = newNodeM();

  /* Store messages from observed nodes, since these will never change */
  for (i = 1; i < N-1; i++) 
    {
      for (j = 1; j < N-1; j++) 
	{
	  tmp = obs[i-1][j-1];
	  tmp0 = 1 + pow(-1, (tmp != 0))*theta;
	  tmp1 = 1 + pow(-1, (tmp != 1))*theta;
	  odd[i][j].ms[0][4] = tmp0;
	  odd[i][j].ms[1][4] = tmp1;
	  even[i][j].ms[0][4] = tmp0;
	  even[i][j].ms[1][4] = tmp1;
	}
    }

  /* Initalize pad values */
  for (i = 0; i < N; i++) 
    {
      odd[0][i].ms[0][0] = -1;
      odd[i][0].ms[0][0] = -1;
      odd[i][N-1].ms[0][0] = -1;
      odd[N-1][i].ms[0][0] = -1;
      even[0][i].ms[0][0] = -1;
      even[i][0].ms[0][0] = -1;
      even[i][N-1].ms[0][0] = -1;
      even[N-1][i].ms[0][0] = -1;
    }
 
  int runs = 0;
  int err;
  //int init_err = compareM(src, obs, N-2);
  //printM(obs, N-2);
  //printf("\nINITIAL Accuracy = %f\nINITIAL Errors = %i\n", (total-init_err)/total, init_err);

  /* begin message passing */
  while(update(odd, even) && (runs < 30))
    {
      float **curr;
      for (i = 1; i < N-1; i++) 
	{
	  for (j = 1; j < N-1; j++) 
	    {
	      curr = even[i][j].ms;
	      tmp0 = 1;
	      tmp1 = 1;
	      for (k = 0; k < 5; k++)
		{
		  tmp0 *= curr[0][k];
		  tmp1 *= curr[1][k];
		}
	      res[i-1][j-1] = (tmp1 >= tmp0);
	    }
	}
      err = compareM(src, res, N-2);
      //printM(res, N-2);
      //printf("%d Errors = %d\n", runs, err); 
      runs++;
    }
  writeM(res, "output.ppm", N-2);
  printf("%s\t%f\t%f\t%i\t%f\n", in, theta, mu, runs, err/total);
  return 0;
}
