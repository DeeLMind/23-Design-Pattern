package com.geekfz.deelmind.m;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Main");
		
		ReaderFactory factoryJpg=new JpgReaderFactory();
		Reader  readerJpg=factoryJpg.getReader();
		readerJpg.read();
		
		ReaderFactory factoryPng=new PngReaderFactory();
		Reader  readerPng =factoryPng.getReader();
		readerPng.read();
		
		ReaderFactory factoryGif=new GifReaderFactory();
		Reader  readerGif=factoryGif.getReader();
		readerGif.read();
		
	}
}
