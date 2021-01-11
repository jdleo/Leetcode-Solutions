class Codec:
    def __init__(self) -> None:
        # initialize array and current pointer
        self.a = []
        self.ptr = 0

    def encode(self, longUrl: str) -> str:
        # store url in array, shortcode is index
        # example: tinyurl.com/1 , tinyurl.com/2 ,
        self.a.append(longUrl)
        self.ptr += 1
        return str(self.ptr - 1)

    def decode(self, shortUrl: str) -> str:
        # get longUrl at index shortUrl
        return self.a[int(shortUrl)]