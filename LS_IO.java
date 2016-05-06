#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

class LS_IO
{
	public static void Serialize(Conlang c, String output)
	{
		try
		{
			FileOutputStream FO = new FileOutputStream(output);
			ObjectOutputStream out = new ObjectOutputStream(FO);
			out.writeObject(c);
			out.close();
			FO.close();
			System.out.println("Serialized data is saved at " + output);
		} catch(IOExcepton i){
			i.printStackTrace();
		}
	}
	
	public static Conlang Deserialize(String directory)
	{
		Conlang c = null;
		
		try{
			FileInputStream FI = new FileInputStream(directory);
			ObjectInput in = new ObjectInputStream(FI);
			c = (Conlang) in.readObject();
			in.close();
			FI.close();
		} catch(IOException i)
		{
			i.printStackTrace();
			return null;
		} catch(ClassNotFoundException k)
		{
			System.out.println("Conlang de-serialized\n");
			k.printStackTrace();
			return null;
		}
		
		
		return c;
	}
}
