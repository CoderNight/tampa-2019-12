import java.util.List;
import java.util.ArrayList;


public class ObservedPin {
    private final static String[] possibles = {"08", "124", "2135", "326", "4157",
                                               "52468", "6359", "748", "80579", "968"};
    private static List<String> result;

    public static List<String> getPINs(String observed) {
       result = new ArrayList<>();
       buildPinStrings("", observed);
       return result;
    }

    private static void buildPinStrings(String partial, String remaining) {
        // If there are no more digits, add the pin string to the result:
        if (remaining.isEmpty()) {
            result.add(partial);

        } else {
            // Loop through the possible pin digits and recursively build the remainder of the pin:
            int digit = remaining.charAt(0) - '0';
            for (int indx = 0; indx < possibles[digit].length(); indx++) {
                buildPinStrings(partial + possibles[digit].charAt(indx), remaining.substring(1));
            }
        }
    }
}

