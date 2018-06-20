package com.geekfz.deelmind.h;

public class WtFactory implements SystemFactory {

	@Override
	public OpController createOperationController() {
		// TODO Auto-generated method stub
		return new WtOpControl();
	}

	@Override
	public UiControl createInterfaceController() {
		// TODO Auto-generated method stub
		return new WtUIControl();
	}

}
