package com.geekfz.deelmind.h;

public class IOSFactory implements SystemFactory {

	@Override
	public OpController createOperationController() {
		// TODO Auto-generated method stub
		return new IosOpControl();
	}

	@Override
	public UiControl createInterfaceController() {
		// TODO Auto-generated method stub
		return new IosUIControl();
	}

}
