package com.geekfz.deelmind.h;

public class AndroidFactory implements SystemFactory {

	@Override
	public OpController createOperationController() {
		// TODO Auto-generated method stub
		return new AndroidOpControl();
	}

	@Override
	public UiControl createInterfaceController() {
		// TODO Auto-generated method stub
		return new AndroidUIControl();
	}

}
