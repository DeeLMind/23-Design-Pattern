package com.geekfz.deelmind.h;

public interface SystemFactory {
	public OpController createOperationController();
    public UiControl createInterfaceController();
}
