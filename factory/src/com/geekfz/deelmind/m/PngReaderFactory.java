package com.geekfz.deelmind.m;

public class PngReaderFactory implements ReaderFactory {

	@Override
	public Reader getReader() {
		// TODO Auto-generated method stub
		return new PngReader();
	}

}
