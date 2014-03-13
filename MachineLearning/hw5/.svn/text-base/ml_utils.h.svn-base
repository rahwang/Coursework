#ifndef ML_UTILS_H
#define ML_UTILS_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <time.h>

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <time.h>


double **newM(int n, int m); 

/* Pretty print matrix */
void printM(double **a, int n, int m);

double **transposeM(double **a, int n, int m);

/* Compare two n x m matrices
 * returns number of mismatches */
int compareM(double **a, double **b, int n, int m);

double **m_mult_m(double **a, double **b, int n, int m, int p);

double **identityM(int n);

double **copyM(double **a, int n, int m);

double **readM(char *fname, int n, int m);

/* Output matrix to the specified file */
void writeM(double **a, char *fname, int n, int m);

/* Fills a nxm matrix with random values */
double **randomM(int n, int m);

/* Fills a nxm matrix with symmetric random values */
double **symRandomM(int n);

/* Multiple a matrix by a vector */
double *m_mult_v(double **a, double *v, double *res, int n, int m);

/* Get the norm of a vector */
double norm(double *v, int n);

/* Vector subtraction */
double *v_sub_v(double *a, double *b, double *res, int n);

/* Vector addition */
double *v_add_v(double *a, double *b, double *res, int n);

/* Vector multiplication by scalar */
double *v_mult_s(double *v, double scalar, double *res, int n);

/* Vector division by scalar */
double *v_div_s(double *v, double scalar, double *res, int n);

/* Normalize a vector */
double *normalize(double *v, int n);

/* find the dot product of two vectors */
double dotProduct(double *a, double *b, int n);

/* Orthogonalize a vector by another k vectors, all of len n */
double *orthogonalize(double *a, double **v, int k, int n);

/* swap two double pointers */
void swap(double **a, double **b);

/* Apply power method until convergence to find the first eigen vector */
double *powerConverge(double **A, int n, double epsilon);

/* Is vector a contained in an array v (k x n) of other vectors? */
int containsV(double *a, double **v, int k, int n);

/* Find k eigen vectors of A */
double **powerConvergeK(double **A, int n, double epsilon, int k);

/* Given a matrix and its vector of eigen vectors, return vector of eigen vals */
double *eigenVals(double **A, double **vs, int n);

/* Sets indices of the largest non-diagonal vals in given matrix */
 void largestOffDiagonal(double **a, int n, int *idx1, int *idx2);

/* Is S matrix in Jacobi's algorithm converged? */
int converged(double **a, int n);

/* Set givens matrix for Jacobi's algorithm */
 void givens(double **a, int n, int idx1, int idx2, double theta);

/* Run Jacobi's algorithm. Set Eigen vectors and values 
   S diagonals = eigen values
   O = eigen vectors */
void jacobi(double **A, double **eVecs, double *eVals, int n, int k);

/* Swap eVals in place and returns sorted eVecs */
double **sortEigenVecs(double **eVecs, double *eVals, int n, int k);

/* Find Singular Value Decomposition */
double **svd(double **A, int k, int n, int m, double *eVals, double ***USV);

#endif
