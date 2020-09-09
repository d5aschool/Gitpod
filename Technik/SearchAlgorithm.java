package Technik;

public class SearchAlgorithm {

    public static final int NO_KEY = -1;

    public static void main(final String[] args) {

        // This is the string-sequence the algorithm should search for in the list. 
        final String query = "simon";

        // This is the list with all possible values put all your trash in here:
        final String[] values = { "niklas", "simon", "steven", "lasse", "phi-anh" };

        final int result = findInArray(values, query);

        // if result is -1 (NO_KEY) return "Nicht gefunden"
        if (result == SearchAlgorithm.NO_KEY) {
            System.out.println("Nicht gefunden");
        } else {
        // otherwise "Gefunden"
            System.out.println("Gefunden an Index: " + result);
        }
    }

    /**
     * Searches a specific string in an string array
     * 
     * @param values    The values to look for the query
     * @param query     The string to look for in the values
     * 
     * @return Index of value in array
     */
    private static int findInArray(final String[] values, final String query) {
        for (int i = 0; i < values.length; i++) {
            final String value = values[i];
            if (value.equalsIgnoreCase(query)) {
                return i;
            }
        }

        return SearchAlgorithm.NO_KEY;
    }

}