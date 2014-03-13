#include "ml_utils.h"

/* Test with test.mat, but only with k = 2!
   (eigen vectors = (0.577, 0.577, 0.5770), (-0.707, 0, 0,707), and a mysterious third?
eig values = (12, 6, 0) */
int main(int argc, char *argv[]) {

  if (argc != 6) {
      fprintf(stderr, "Error: wrong number of arguments provided. Program expects 5 arguments (k, log(epsilon), filename, matrix dimension n, mode). \n Mode 1 = read from file. Mode 2 = generate matrix. \n\n");
      exit(1);
  }

  //int k = atoi(argv[1]);
  double epsilon = (double)atof(argv[2]);
  char *input = argv[3];
  int n = atoi(argv[4]);
  int mode = atoi(argv[5]);
  
  //printf("\nRunning eigP with arguments (%i, %f, %s, %i)\n\n", k, epsilon, input, n);

  /* Get input matrix A */
  double **A = newM(n, n);
  switch(mode) {
  case(1):
    A = readM(input, n, n);
    break;
  case(2):
    A = symRandomM(n);
    writeM(A, "test.mat", n, n);
    break;
  }
  printM(A, n, n);

  double **eVecs = newM(n, n);
  double *eVals = (double *)malloc(sizeof(double)*n);

  jacobi(A, eVecs, eVals, n, n);
  eVecs = sortEigenVecs(eVecs, eVals, n, n);

  // For Power method
  /*double *eVec1 = powerConverge(A, n, epsilon);
  printM(&eVec1, 1, n);
  eVecs = powerConvergeK(A, n, epsilon, k);
  eVals =  eigenVals(A, eVecs, n);  */

  /*
  printf("Results:\n\n");
  printM(eVecs, n, n);
  printM(&eVals, 1, n); */

  writeM(eVecs, "eVecs.data", n, n);
  writeM(&eVals, "eVals.data", 1, n);
  return 0;
}
