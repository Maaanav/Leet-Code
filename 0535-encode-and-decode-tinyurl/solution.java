public class Codec {

    // Encodes a URL to a shortened URL.
    private HashMap<String, String> urlMap = new HashMap<>();
    private HashMap<String, String> reverseMap = new HashMap<>();
    private final String chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    private final int CODE_LENGTH = 6;
    private final String BASE_URL = "http://tinyurl.com/";

    private String generateCode() {
        StringBuilder sb = new StringBuilder();
        Random rand = new Random();
        for (int i = 0; i < CODE_LENGTH; i++) {
            sb.append(chars.charAt(rand.nextInt(chars.length())));
        }
        return sb.toString();
    }

    public String encode(String longUrl) {
        if (reverseMap.containsKey(longUrl)) {
            return BASE_URL + reverseMap.get(longUrl);
        }

        String code = generateCode();
        while (urlMap.containsKey(code)) {
            code = generateCode();
        }

        urlMap.put(code, longUrl);
        reverseMap.put(longUrl, code);

        return BASE_URL + code;
    }

    public String decode(String shortUrl) {
        String code = shortUrl.replace(BASE_URL, "");
        return urlMap.getOrDefault(code, "");
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
