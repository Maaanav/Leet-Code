class Solution {
    public double angleClock(int hour, int minutes) {
        double ha = (30*hour) + (0.5 * minutes);
        double ma = 6 * minutes;

        double angle = Math.abs(ha-ma);
        return Math.min(angle, 360-angle);
    }
}
