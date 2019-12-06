class ConvertNumToString:
    numbers = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
               10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
               17: "seventeen", 18: "eighteen", 19: "nineteen"}
    doubles = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    def number_to_string(self, num):
        if num == 0:
            return ""
        if num < 20:
            return self.numbers[num]
        elif 100 >= num >= 20:
            number = self.doubles[num//10] + " " + self.numbers[num%10]
            return number
        elif 100 < num <= 1000:
            return str(self.number_to_string(num//100)) + " hundred " + str(self.number_to_string((num%100)))
        elif 1000 < num <= 1000000:
            return str(self.number_to_string(num//1000)) + " thousand " + str(self.number_to_string((num%1000)))
        elif 1000000 < num <= 1000000000:
            return str(self.number_to_string(num//1000000)) + " million " + str(self.number_to_string(num%1000000))
        elif num >= 1000000000:
            return str(self.number_to_string(num//1000000000)) + " billion " + str(self.number_to_string(num%1000000000))


