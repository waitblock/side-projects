import java.util.*;

public class Main {
	
	static String[] chars = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Random rand = new Random();
		while (true) {
			System.out.println("How many words of gibberish do you want: ");
			int word_count = sc.nextInt();
			String words = "";
			for(int i = 0; i<word_count; i++) {
				int word_length = rand.nextInt(10);
				if(word_length < 2) {
					word_length = 2;
				}
				String word = "";
				for(int j = 0; j<word_length; j++) {
					word += chars[rand.nextInt(26)];
				}
				words = words + word + " ";
			}
			System.out.println(words);
			System.out.println("\n");
		}

	}

}
