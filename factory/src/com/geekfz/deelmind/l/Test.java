package com.geekfz.deelmind.l;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Main");
		
		Shape circle = ShapeFactory.getShape("Circle");
		circle.draw();
		
		Shape rect = ShapeFactory.getShape("Rect");
		rect.draw();
		
		Shape triang = ShapeFactory.getShape("Triang");
		triang.draw();
		
		
	}

}
