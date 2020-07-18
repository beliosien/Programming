/* *****************************************************************************
 *  Name: Ossim Belias
 *  Date: 2020-07-17
 *  Description: Among all points given, this program examines 4 points at a time and checks whether
 * they all lie on the same line segment, returning all such line segments.
 **************************************************************************** */

import java.util.Arrays;

public class BruteCollinearPoints {
    private static final int INIT_SIZE = 1;
    private int count;
    private final Point[] points;
    private LineSegment[] lineSegments;

    // finds all line segments containing 4 points
    public BruteCollinearPoints(Point[] points) {
        if (points == null) {
            throw new IllegalArgumentException("Argument null");
        }
        else {
            this.count = 0;
            this.lineSegments = new LineSegment[INIT_SIZE];
            Arrays.sort(points);
            this.points = new Point[points.length];
            for (int i = 0; i < points.length; i++) {
                if (points[i] == null) {
                    throw new IllegalArgumentException("Argument null");
                }
                if (points[i].compareTo(points[i + 1]) == 0) {
                    throw new IllegalArgumentException("Same point twice");
                }
                this.points[i] = points[i];
            }
        }
    }

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
        LineSegment[] lineSegment;
        // review this method
        for (int i = 0; i < this.points.length - 4; i += 4) {
            double slope1 = this.points[i].slopeTo(this.points[i + 1]);
            double slop2 = this.points[i + 2].slopeTo(this.points[i + 3]);
            if (slop2 == slope1) {
                if (this.count == this.lineSegments.length) {
                    this.resize(4 * this.count);
                }
                lineSegments[this.count++] = new LineSegment(this.points[i], this.points[i + 3]);
            }
        }
        lineSegment = this.lineSegments.clone();
        return lineSegment;
    }

    // use this function for test only
    public static void main(String[] args) {
        // code here

    }
}
