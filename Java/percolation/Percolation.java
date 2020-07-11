/* *****************************************************************************
 *  Name:              Titanium titan
 *  Coursera User ID:  123456
 *  Last modified:     10/07/2020
 **************************************************************************** */

import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private int gridSize;
    private int count = 0;
    private int topVirtualSiteParentIndex;
    private int bottomVirtualSiteParentIndex;
    private boolean[][] grid;
    private WeightedQuickUnionUF connectedSites;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        this.gridSize = n + 1;
        this.topVirtualSiteParentIndex = this.xyTo1D(0, 0);
        this.bottomVirtualSiteParentIndex = this.xyTo1D(n, n);
        this.connectedSites = new WeightedQuickUnionUF(gridSize * gridSize + 2);
        this.grid = new boolean[gridSize][gridSize];
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                this.grid[i][j] = false;
            }
        }

        // Top virtual site
        for (int i = 1; i < gridSize; i++) {
            int indexPt = this.xyTo1D(0, i);
            this.connectedSites.union(indexPt, this.topVirtualSiteParentIndex);
        }

        // bottom virtual site
        for (int j = 0; j < gridSize - 1; j++) {
            int indexPt = this.xyTo1D(gridSize - 1, j);
            this.connectedSites.union(indexPt, this.bottomVirtualSiteParentIndex);
        }

    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        if (this.isIndexValid(row, col) && !this.grid[row][col]) {
            this.grid[row][col] = true;
            this.count++;
            this.connectSite(row, col);
        }
    }

    public void connectSite(int row, int col) {
        int top, left, bottom, right;
        int center = this.xyTo1D(row, col);

        if (isOpen(row, col - 1)) {
            bottom = this.xyTo1D(row, col - 1);
            if (bottom != -1) {
                this.connectedSites.union(center, bottom);
            }
        }

        if (isOpen(row - 1, col)) {
            left = this.xyTo1D(row - 1, col);
            if (left != -1) {
                this.connectedSites.union(center, left);
            }

        }

        if (isOpen(row, col + 1)) {
            right = this.xyTo1D(row, col + 1);
            if (right != -1) {
                this.connectedSites.union(center, right);
            }

        }

        if (isOpen(row + 1, col)) {
            top = this.xyTo1D(row + 1, col);
            if (top != -1) {
                this.connectedSites.union(center, top);
            }

        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        return this.isIndexValid(row, col) && this.grid[row][col];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        int point = this.xyTo1D(row, col);
        return this.isIndexValid(row, col)
                && this.connectedSites.find(this.topVirtualSiteParentIndex) == this.connectedSites
                .find(point);

    }

    // convert 2D coordonnates to 1D
    private int xyTo1D(int x, int y) {
        return this.isIndexValid(x, y) ? x * gridSize + y : -1;
    }

    // validate index
    public boolean isIndexValid(int row, int col) {
        try {
            if (row >= this.gridSize || col >= this.gridSize || row < 0 || col < 0) {
                throw new ArrayIndexOutOfBoundsException(
                        "Invalid indexes: " + "row:" + row + ", col:" + col);
            }
            return true;
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println(e.getMessage());
            return false;
        }
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return this.count;
    }

    // does the system percolate?
    public boolean percolates() {
        return this.connectedSites.find(this.topVirtualSiteParentIndex) == this.connectedSites
                .find(this.bottomVirtualSiteParentIndex);
    }

    // tell if two points of the grid are connected
    public boolean isConnected(int x, int y, int x2, int y2) {
        int p1 = this.xyTo1D(x, y);
        int p2 = this.xyTo1D(x2, y2);
        return this.connectedSites.find(p1) == this.connectedSites.find(p2);
    }

    // test client (optional)
    public static void main(String[] args) {

    }
}
