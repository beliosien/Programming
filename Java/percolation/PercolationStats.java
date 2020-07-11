/* *****************************************************************************
 *  Name:              Titan titanium
 *  Coursera User ID:  123456
 *  Last modified:     11/07/2020
 **************************************************************************** */

import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;


public class PercolationStats {
    private static final double VALUE = 1.96;
    private double[] openSiteFraction;
    private int trials;
    private double mean;
    private double s;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        try {
            if (n <= 0 || trials <= 0) {
                throw new IllegalArgumentException("n and trials must be greater than zero.");
            }
            else {
                this.trials = trials;
                this.openSiteFraction = new double[trials];
                for (int i = 0; i < trials; i++) {
                    Percolation p = new Percolation(n);
                    while (!p.percolates()) {
                        int row = StdRandom.uniform(1, n + 1);
                        int col = StdRandom.uniform(1, n + 1);
                        p.open(row, col);
                    }
                    int openSite = p.numberOfOpenSites();
                    this.openSiteFraction[i] = (double) openSite / (n * n);
                }
            }
        }
        catch (IllegalArgumentException e) {
            // catch the error
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        this.mean = StdStats.mean(this.openSiteFraction);
        return mean;
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        double ss = StdStats.stddev(this.openSiteFraction);
        s = Math.sqrt(ss);
        return ss;
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        double confidenceLo = this.mean - ((VALUE * this.s) / (Math
                .sqrt(this.trials)));
        return confidenceLo;
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        double confidenceHi = this.mean + ((VALUE * this.s) / (Math
                .sqrt(this.trials)));
        return confidenceHi;
    }

    // test client (see below)
    public static void main(String[] args) {
        // for test only

    }

}
