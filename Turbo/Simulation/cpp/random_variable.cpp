#include <sstream>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <stdlib.h>
#include <deque>
#include <stdint.h>
#include <math.h>

#include "random_variable.h"

using namespace std;

/* Uniform Random Variable
*/
UniformRandomVariable::UniformRandomVariable() {
  min_ = 0.0;
  max_ = 1.0;
}

UniformRandomVariable::UniformRandomVariable(double min, double max) {
  min_ = min;
  max_ = max;
}

double UniformRandomVariable::value() { // never return 0
  double unif0_1 = (1.0 * rand() + 1.0) / (RAND_MAX* 1.0 + 1.0);
  return min_ + (max_ - min_) * unif0_1;
}



/* Exponential Random Variable
 */
ExponentialRandomVariable::ExponentialRandomVariable(double avg) {
  avg_ = avg;
  urv = UniformRandomVariable();

}

double ExponentialRandomVariable::value() {
  return -1.0 * avg_ * log(urv.value());
}




/* Empirical Random Variable with random interpolation
 * Ported from NS2
 */
EmpiricalRandomVariable::EmpiricalRandomVariable(std::string filename) {
  minCDF_ = 0;
  maxCDF_ = 1;
  maxEntry_ = 32;
  table_ = new CDFentry[maxEntry_];
  loadCDF(filename);
}

double EmpiricalRandomVariable::value() {
  if (numEntry_ <= 0)
    return 0;
  double u = (1.0 * rand()) / RAND_MAX;
  int mid = lookup(u);
  if (mid && u < table_[mid].cdf_)
    return interpolate(u, table_[mid-1].cdf_, table_[mid-1].val_,
           table_[mid].cdf_, table_[mid].val_);
  return table_[mid].val_;
}

double EmpiricalRandomVariable::interpolate(double x, double x1, double y1,
                                            double x2, double y2) {
  double value = y1 + (x - x1) * (y2 - y1) / (x2 - x1);
  return ceil(value);
}

int EmpiricalRandomVariable::lookup(double u) {
  // always return an index whose value is >= u
  int lo, hi, mid;
  if (u <= table_[0].cdf_)
    return 0;
  for (lo=1, hi=numEntry_-1;  lo < hi; ) {
    mid = (lo + hi) / 2;
    if (u > table_[mid].cdf_)
      lo = mid + 1;
    else
      hi = mid;
  }
  return lo;
}

int EmpiricalRandomVariable::loadCDF(std::string filename) {
  std::string line;
  std::ifstream myfile(filename);
  if(!myfile.good()){
	  std::cout << "bad cdf file!!\n";
	  exit(0);
  }
  numEntry_ = 0;
  while (std::getline(myfile, line))
	{
    std::istringstream is(line);
    is >> table_[numEntry_].val_;
    is >> table_[numEntry_].cdf_;
    is >> table_[numEntry_].cdf_;
    numEntry_ ++;
	}
  //std::cout << "Number of lines in text file: " << numEntry_ << "\n";
	myfile.close();
  return numEntry_;
}
