package com.geekfz.deelmind.l;

public class ShapeFactory {
    public static final String TAG = "ShapeFactory";
    public static Shape getShape(String type) {
        Shape shape = null;
        if (type.equalsIgnoreCase("Circle")) {
            shape = new Circle();
        } else if (type.equalsIgnoreCase("Rect")) {
            shape = new Rect();
        } else if (type.equalsIgnoreCase("Triang")) {
            shape = new Triang();
        }
        return shape;
    }
}
