import javax.xml.parsers.*;
import org.w3c.dom.*;
import org.xml.sax.*;
import java.text.*;

public class xmlproc
{
	public static Document getDocument(String name)
	{
		try
		{
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			factory.setIgnoringComments(true);
			factory.setIgnoringComments(true);
			factory.setValidating(true);
			DocumentBuilder builder = factory.newDocumentBuilder();
			return builder.parse(new InputSource(name));
		}
		catch(Exception e)
		{
			System.out.prinln(e.getMessage());
		}
		return null;
	}
	
	public static String getNodeValue(Node n)
	{
		return n.getFirstChild().getNodeValue();
	}
	
	public static String[] GetInfo(Element e)
	{
		return [e.getAttribute("entry"), getNodeValue(e).trim()];
	}
	public static language ProcessTranslation(String name)
	{
		language c = new language();
		Document w = getDocument(name)
		
		Element r = w.getDocumentElement();
		
		Element k = (Element)r.getFirstChild();
		while(k != null)
		{
			String[] d = GetInfo(k);
			c.translations.put(d[0], f[1]);
			k = (Element)k.getNextSibling();
		}
		return c;
	}
	
}