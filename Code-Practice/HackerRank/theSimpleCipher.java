// - simple caesar cipher
// how i could do it:
// - iterate through input string
// - convert input character to numerical position
// - re-convert back to input character
// what i would use:
// - for-loop
class Result {
    /* The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. STRING encrypted
     *  2. INTEGER k
     */

    public static String simpleCipher(String encrypted, int k) {
        // Write your code here
        StringBuilder decrypted = new StringBuilder();
        k = k % 26; // redeclared to cylcle all 26 letters of alphabet

        for (char ch : encrypted.toCharArray()) {
            if (ch >= 'A' && ch <= 'Z') {
                decrypted.append((char) ('A' + (ch - 'A' - k + 26) % 26));
            } else {
                decrypted.append(ch);
            }
        }
        return decrypted.toString();
    }
}

// I wasn't able to get the solution class and contents.