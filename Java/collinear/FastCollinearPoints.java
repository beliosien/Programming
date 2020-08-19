/* *****************************************************************************
 *  Name: Ossim Belias
 *  Date: 2020-07-19
 *  Description: FastCollinearsPoints class
 **************************************************************************** */

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

import java.util.Arrays;
import java.util.LinkedList;

public class FastCollinearPoints {
    private static final int INIT_SIZE = 1;
    private int count;
    private LineSegment[] lineSegments;

    // finds all line segments containing 4 or more points
    public FastCollinearPoints(Point[] points) {
        if (points == null) {
            throw new IllegalArgumentException("argument is null");
        }
        else {
            Arrays.sort(points);
            lineSegments = new LineSegment[INIT_SIZE];
            for (int i = 0; i < points.length; i++) {
                if (points[i] == null) {
                    throw new IllegalArgumentException("argument null");
                }
                if (i + 1 <= points.length - 1 && points[i].compareTo(points[i + 1]) == 0) {
                    throw new IllegalArgumentException("same point twice");
                }
            }
        }

        for (int i = 0; i < points.length; i++) {
            LinkedList<Point> listonPt = new LinkedList<Point>();
            for (int j = 0; j < points.length; j++) {
                if (j + 1 < points.length) {
                    int result = points[i].slopeOrder().compare(points[j], points[j + 1]);
                    if (result == 0) {
                        listonPt.push(points[j]);
                        listonPt.push(points[j + 1]);
                    }
                }
            }
            if (listonPt.size() > 0) {
                if (this.count == this.lineSegments.length) {
                    this.resize(2 * this.count);
                }
                lineSegments[count++] = new LineSegment(listonPt.peekFirst(), listonPt.peekLast());
            }

        }
    }

    // expand the size of an array
    private void resize(int capacity) {
        LineSegment[] copy = new LineSegment[capacity];
        for (int i = 0; i < this.count; i++) {
            copy[i] = this.lineSegments[i];
        }
        this.lineSegments = copy;
    }

    // the number of line segments
    public int numberOfSegments() {
        return this.count;
    }

    // the line segments
    public LineSegment[] segments() {
        return this.lineSegments;
    }

    // use this function for test only
    public static void main(String[] args) {

        // read the n points from a file
        In in = new In(args[0]);
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
        }

        // draw the points
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        StdDraw.setPenColor(StdDraw.BLUE);
        for (Point p : points) {
            p.draw();
        }
        StdDraw.show();

        // print and draw the line segments
        FastCollinearPoints collinear = new FastCollinearPoints(points);
        StdOut.println(collinear.numberOfSegments());
        for (LineSegment segment : collinear.segments()) {
            if (segment != null) {
                StdOut.println(segment);
                segment.draw();
            }
        }
        StdDraw.show();
    }
}
