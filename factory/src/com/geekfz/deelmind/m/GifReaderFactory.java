package com.geekfz.deelmind.m;

public class GifReaderFactory implements ReaderFactory {

	@Override
	public Reader getReader() {
		// TODO Auto-generated method stub
		return new GifReader();
	}

}
