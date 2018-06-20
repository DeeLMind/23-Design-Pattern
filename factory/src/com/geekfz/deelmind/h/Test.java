package com.geekfz.deelmind.h;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SystemFactory mFactory;
	    UiControl interfaceController;
	    OpController operationController;

	    //Android
	    mFactory=new AndroidFactory();
	    //Ios
	    mFactory=new IOSFactory();
	    //Wp
	    mFactory=new WtFactory();

	    interfaceController=mFactory.createInterfaceController();
	    operationController=mFactory.createOperationController();
	    interfaceController.display();
	    operationController.control();
	}

}
