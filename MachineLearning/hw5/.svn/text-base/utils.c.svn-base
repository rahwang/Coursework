#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <time.h>


double **newM(int n, int m) 
{
  int i;
  double **new = (double **)malloc(sizeof(double *)*n);
  for (i = 0; i < n; i++) {
    new[i] = (double *)malloc(sizeof(double)*m);
  }
  return new;
}


/* Pretty print matrix */
void printM(double **a, int n, int m) {
  int i, j;
  printf("\n");
  for (i = 0; i < n; i++) {
    for (j = 0; j < m ; j++) {
      printf("%f ", a[i][j]);
    }
    printf("\n");
  }
  printf("\n\n\n");
}


double **transposeM(double **a, int n, int m) {
  int i, j;
  double **res = newM(n, m);

  for (i = 0; i < n; i++) {
    for (j = 0; j < m; j++) {
      res[i][j] = a[j][i];
    }
  }
  return res;
}

/* Compare two n x m matrices
 * returns number of mismatches */
int compareM(double **a, double **b, int n, int m) {
  int err = 0;
  int i, j;
  for (i = 0; i < n; i++) {
    for (j = 0; j < m; j++) {
      if (a[i][j] != b[i][j]) {
	err++;
	fprintf(stderr, "Mismatch at [%d, %d]\n", i, j);
      }
    }
  }
  fprintf(stderr, "There were [ %d ] mismatches.\n", err);
  return err;
}

double **m_mult_m(double **a, double **b, int n, int m, int p) {
  
  double **res = newM(n, p);
  int i, j, k;
  
  for(i = 0; i < n; i++) {
    for(j = 0; j < p; j++) {
      res[i][j] = 0;
      for(k = 0; k < m; k++){
	res[i][j] += a[i][k] * b[k][j];
      }
    }
  }
  return res;
}


double **identityM(int n) {
  double **new = newM(n, n);

  int i, j;
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      new[i][j] = (i == j) ? 1 : 0;
    }
  }
  return new;
}


double **copyM(double **a, int n, int m) {
  double **new = newM(n, m);

  int i, j;
  for (i = 0; i < n; i++) {
    for (j = 0; j < m; j++) {
      new[i][j] = a[i][j];
    }
  }
  return new;
}


double **readM(char *fname, int n, int m)
{
    float data;
    int i, j;
    FILE *src = fopen(fname, "r");
    double **a = newM(n, m);

    //printf("\n=====================\nLoading Matrix\n=====================\n");
    for (i = 0; i < n; i++)
      {
        for (j = 0; j < m; j++)
	  {
            fscanf(src, "%f", &data);
            a[i][j] = data;
	  } 
      }
    fclose(src);
    return a;
}


/* Output matrix to the specified file */
void writeM(double **a, char *fname, int n, int m) 
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
      for (j = 0; j < m; j++) 
	{
	  fprintf(dst, "%f ", (float)a[i][j]);
	}
      fprintf(dst, "\n");
    }
  fclose(dst);
}


/* Fills a nxm matrix with random values */
double **randomM(int n, int m)
{
  int i, j, val;
  double **a = newM(n, m);

  srand(time(NULL));
  
  for (i = 0; i < n; i++) {
    for (j = 0; j < m; j++) {
      val = (int)rand() % 100;
      a[i][j] = val/100.;
    }
  } 
  return a;
}


/* Fills a nxm matrix with symmetric random values */
double **symRandomM(int n)
{
  int i, j, val;
  double **a = newM(n, n);
  
  srand(time(NULL));
  
  for (i = 0; i < n; i++) {
    for (j = 0; j <= i; j++) {
      val = (int)rand() % 100;
      a[i][j] = a[j][i] = val/100.;
    }
  } 
  return a;
}

/* Multiple a matrix by a vector */
double *m_mult_v(double **a, double *v, double *res, int n, int m) {
  
  int i,j;
  for (i=0;i< m;i++) {
    res[i] = 0;
  }
  
  for (i = 0;i < n;i++){
    for (j = 0;j < m;j++) {
      res[i]+=(a[i][j]*v[j]);
    }
  }
  return res;
}


/* Get the norm of a vector */
double norm(double *v, int n) {
  int i;
  double sum = 0;
  
  for (i  = 0; i < n; i++) {
    sum += pow(v[i], 2);
  }
  
  return sqrt(sum);
}


/* Vector subtraction */
double *v_sub_v(double *a, double *b, double *res, int n) {
  int i;
  for (i = 0; i < n; i++) {
    res[i] = a[i] - b[i];
  }
  return res;
}


/* Vector addition */
double *v_add_v(double *a, double *b, double *res, int n) {
  int i;
  for (i = 0; i < n; i++) {
    res[i] = a[i] + b[i];
  }
  return res;
}


/* Vector multiplication by scalar */
double *v_mult_s(double *v, double scalar, double *res, int n) {
  int i;
  for (i = 0; i < n; i++) {
    res[i] = v[i] * scalar;
  }
  return res;
}


/* Vector division by scalar */
double *v_div_s(double *v, double scalar, double *res, int n) {
  int i;
  for (i = 0; i < n; i++) {
    res[i] = v[i] / scalar;
  }
  return res;
}


/* Normalize a vector */
double *normalize(double *v, int n) {
  int i;
  double normv = norm(v, n);

  for (i = 0; i < n; i++) {
    v[i] /= normv;
  }
  return v;
}


/* find the dot product of two vectors */
double dotProduct(double *a, double *b, int n) {
  int i;
  double sum = 0;
  for (i = 0; i < n; i++)
    sum += a[i] * b[i];
  return sum;
 }


/* Orthogonalize a vector by another k vectors, all of len n */
double *orthogonalize(double *a, double **v, int k, int n) {
  
  int i;
  double *tmp = (double *)malloc(sizeof(double)*n);
  double scalar;
  
  for (i = 0; i < k; i++) {
    scalar = dotProduct(a, v[i], n);
    tmp = v_mult_s(v[i], scalar, tmp, n);
    a = v_sub_v(a, tmp, a, n);
  }
  //printM(&a, 1, n);
  //a = normalize(a, n);
  return a;
}


/* swap two double pointers */
void swap(double **a, double **b) {
  double *tmp = *a;
  *a = *b;
  *b = tmp;
}


/* Apply power method until convergence to find the first eigen vector */
double *powerConverge(double **A, int n, double epsilon) {

  double eps = pow(10, -1*epsilon);
  /* Create random vector */
  double *r = *randomM(1, n);
  double *newr = (double *)malloc(sizeof(double)*n);
  double *tmp = (double *)malloc(sizeof(double)*n);
  double e1, e2;
  int iter = 0;
  e1 = e2 = 1;

  while((e1 >= eps) && (e2 >= eps)) {
    newr = normalize(m_mult_v(A, r, newr, n, n), n);
    e1 = norm(v_sub_v(r, newr, tmp, n), n);
    e2 = norm(v_add_v(r, newr, tmp, n), n);
    swap(&r, &newr);
    iter++;
  }
  printf("%i\t%f\t%i\n", n, epsilon, iter);
  return r; 
}


/* Is vector a contained in an array v (k x n) of other vectors? */
int containsV(double *a, double **v, int k, int n) {
  int i, sum;
  sum = 0;
  for (i = 0; i < k; i++) {
    sum += (pow(dotProduct(a, v[i], n), 2) > 0.8);
  }
  return sum;
}


/* Find k eigen vectors of A */
double **powerConvergeK(double **A, int n, double epsilon, int k) {

  int found, iter, freq;
  double *r;
  double eps = pow(10, -1*epsilon);
  double *newr = (double *)malloc(sizeof(double)*n);
  double *tmp = (double *)malloc(sizeof(double)*n);
  double e1, e2;
  double **eigenV = newM(n, k);

  eigenV[0] = powerConverge(A, n, eps);
  found = 1;

  while (found < k) 
    {
      r = *randomM(1, n);
      orthogonalize(r, eigenV, found, n);
      e1 = e2 = 1;
      iter = 0;
      freq = 5;
      
      while((e1 >= eps) && (e2 >= eps)) 
	{
	  //printf("Iterations %i %i\n", iter, freq);
	  if (iter == freq) {
	    orthogonalize(r, eigenV, found, n);
	    iter = 0;
	    freq *= 1.2;
	  }

	  newr = normalize(m_mult_v(A, r, newr, n, n), n);
	  e1 = norm(v_sub_v(r, newr, tmp, n), n);
	  e2 = norm(v_add_v(r, newr, tmp, n), n);
	  swap(&r, &newr);
	  
	  iter++;
	}
      //printf("On to the next k\n");
      if (!containsV(r, eigenV, found, n)) {
	eigenV[found] = r;
	found++;
      }
    }
  
  return eigenV;
}


/* Given a matrix and its vector of eigen vectors, return vector of eigen vals */
double *eigenVals(double **A, double **vs, int n) {
  int i;
  double *new = (double *)malloc(sizeof(double));
  double *tmp = (double *)malloc(sizeof(double)); 

  for (i = 0; i < n; i++) {
    new[i] = norm(m_mult_v(A, vs[i], tmp, n, n), n) / norm(vs[i], n);
  }
  free(tmp);
  return new;
}


/* Sets indices of the largest non-diagonal vals in given matrix */
void largestOffDiagonal(double **a, int n, int *idx1, int *idx2) {

  int i, j;
  double max = 0;
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      if ((a[i][j] > max) && (i != j)) {
	max = a[i][j];
	*idx1 = i;
	*idx2 = j;
      }
    }
  }
}


/* Is S matrix in Jacobi's algorithm converged? */
int converged(double **a, int n) {
  int i, j;
  double avg;

  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      if (i != j) {
	avg += pow(a[i][j], 2); 
      }
    }
  }
  avg /= n*(n-1);
  printf("avg = %f\n", avg);
  return (avg < 0.12);
}


/* Set givens matrix for Jacobi's algorithm */
void givens(double **a, int n, int idx1, int idx2, double theta) {
  int i, j;
  
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      a[i][j] = (i == j) ? 1 : 0;
    }
  }
  
  a[idx1][idx1] = cos(theta);
  a[idx2][idx2] = cos(theta);  
  int bigger = (idx1 > idx2) ? idx1 : idx2;
  int smaller = (idx1 > idx2) ? idx2 : idx1;
  
  a[bigger][smaller] = -1 * sin(theta);
  a[smaller][bigger] = sin(theta);
}


/* Run Jacobi's algorithm. Set Eigen vectors and values 
   S diagonals = eigen values
   O = eigen vectors */
void jacobi(double **A, double **eVecs, double *eVals, int n) {
  double **S = copyM(A, n, n);
  double **O = identityM(n);
  double **G = newM(n, n);
  double **tmp = newM(n, n);
  double theta;
  int idx1, idx2;

  while(!converged(S, n)) {
    //for (int i = 0; i < 10; i++) {
    printM(S, n, n);
    largestOffDiagonal(S, n, &idx1, &idx2);
    //printf("%i %i\n", idx1, idx2);
    theta = 0.5 * atan(2 * S[idx1][idx2]/(S[idx2][idx2] - S[idx1][idx1]));
    givens(G, n, idx1, idx2, theta);
    //printM(G, n, n);
    tmp = transposeM(G, n, n);
    //printM(tmp, n, n);
    S = m_mult_m(m_mult_m(G, S, n, n, n), tmp, n, n, n);
    //printM(S, n, n);
    O = m_mult_m(G, O, n, n, n);
    //printM(O, n, n);
  }

  // Now copy results
  int i, j;
  for (i = 0; i < n; i++) {
    eVals[i] = S[i][i];
    for (j = 0; j < n; j++) {
      eVecs[i][j] = O[i][j];
    }
  }
}
		 
		 
/* Test with test.mat, but only with k = 2!
(eigen vectors = (0.577, 0.577, 0.5770), (-0.707, 0, 0,707), and a mysterious third?
eig values = (12, 6, 0) */
int main(int argc, char *argv[]) {

  if (argc != 6) {
      fprintf(stderr, "Error: wrong number of arguments provided. Program expects 5 arguments (k, log(epsilon), filename, matrix dimension n, mode). \n Mode 1 = read from file. Mode 2 = generate matrix. \n\n");
      exit(1);
  }

  //int k = atoi(argv[1]);
  //double epsilon = (double)atof(argv[2]);
  char *input = argv[3];
  int n = atoi(argv[4]);
  int mode = atoi(argv[5]);
  
  //printf("\nRunning eigP with arguments (%i, %f, %s, %i)\n\n", k, epsilon, input, n);

  /* Get input matrix A */
  double **A;
  switch(mode) {
  case(1):
    A = readM(input, n, n);
    break;
  case(2):
    A = symRandomM(n);
    writeM(A, "test10.mat", n, n);
    break;
  }
  //printM(A, n, n);
    
  double **eVecs = newM(n, n);
  double *eVals = (double *)malloc(sizeof(double)*n);;

  jacobi(A, eVecs, eVals, n);

  // For Power method
  /*double *eVec1 = powerConverge(A, n, epsilon);
  printM(&eVec1, 1, n);
  eVecs = powerConvergeK(A, n, epsilon, k);
  eVals =  eigenVals(A, eVecs, n);  */

  printf("Results:\n\n");
  printM(eVecs, n, n);
  printM(&eVals, 1, n);
  return 0;
}
