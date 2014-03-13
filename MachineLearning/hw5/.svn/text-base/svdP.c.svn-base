#include "ml_utils.h"

double frobenius(double **A, double **USV, int n, int m) {
  double sum = 0;

  int i, j;
  for (i = 0; i < n; i++) {
    for (j = 0; j < m; j++) {
      sum += pow(A[i][j] - USV[i][j], 2);
    }
  }
  return sqrt(sum);
}


int main(int argc, char *argv[]) {

  if (argc != 6) {
      fprintf(stderr, "Error: wrong number of arguments provided. Program expects 5 arguments (k, log(epsilon), filename, matrix dimension n, mode). \n Mode 1 = read from file. Mode 2 = generate matrix. \n\n");
      exit(1);
  }

  int k = atoi(argv[1]);
  double epsilon = (double)atof(argv[2]);
  char *input = argv[3];
  int n = atoi(argv[4]);
  int mode = atoi(argv[5]);

  /* Get input matrix A */
  double **A = newM(n, n);
  k = n-k;
  switch(mode) {
  case(1):
    A = readM(input, n, n);
    break;
  case(2):
    A = symRandomM(n);
    writeM(A, "svd_test.mat", n, n);
    break;
  }

  double *eVals = (double *)malloc(sizeof(double)*n);
  double **USV;
  double **eVecs = svd(A, k, n, n, eVals, &USV);

  double err = frobenius(A, USV, n, n);

  printf("err: %f\n\n", (float)err);

  printM(USV, n, n);

  writeM(eVecs, "svd_eVecs.data", k, k);
  writeM(&eVals, "svd_eVals.data", 1, n);
}
