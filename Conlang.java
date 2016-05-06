/*
#The MIT License (MIT)
#
#Copyright (c) 2016 saberman888

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

import java.util.*;
import java.io.Serializable*;

class Conlang implements java.io.Serializable;
{
	public String name;
	public String author;
	public String family;
	public Typology t;
	public Alignment a;
	public LanguageType l;
	public String source;
	public String notes;
	public ArrayList<Word> w;
	public ArrayList<Dialect> d;
	public ArrayList<LSClass> c;
	
	public Conlang(String name, String author, String family, Typology t, Alignment a, LanguageType l, String source, String notes)
	{
		this.name = name;
		this.author = author;
		this.family = family;
		this.t = t;
		this.a = a;
		this.l = l;
		this.source = source;
		this.notes = notes;
		
		this.w = new ArrayList<Word>();
		this.d = new ArrayList<Dialect>();
		this.c = new ArrayList<LSClass>();
	}
	
	public void AddWord(Word w)
	{
		this.w.add(w);
	}
	
	public void AddDialect(Dialect d)
	{
		this.d.add(d);
	}
	
	public void AddClass(LSClass c)
	{
		this.c.add(c);
	}
	
}