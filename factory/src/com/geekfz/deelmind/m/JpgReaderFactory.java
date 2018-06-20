package com.geekfz.deelmind.m;

public class JpgReaderFactory implements ReaderFactory {

	@Override
	public Reader getReader() {
		// TODO Auto-generated method stub
		return new JpgReader();
	}

}
