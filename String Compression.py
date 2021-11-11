class Solution:
    
    def compress(chars):
        
        def split_digit(x):
            output = []
            while x > 0:
                output.append(str(x%10))
                x = x // 10
            #print(output)
            return output[::-1]
        if len(chars) < 2:
            return len(chars)
        current_char = ''
        output_length = 0
        for i in range (len(chars)-1):
            #print(output_length)
            if chars[i] == current_char:
                continue
            if chars[i] != chars[i+1]:
                output_length = output_length + 1
                #print("samman")
                continue
            occurances = 1
            
            for j in range (i+1,len(chars)):
                if chars[i] == chars[j]:
                    occurances = occurances + 1
                if chars[i] != chars[j] or j == len(chars) - 1: 
                    
                    output = split_digit(occurances)
                    for k in range(0,len(output)):
                        chars[i+1+k] = output[k]
                        output_length = output_length + 1
                        
                    
                    current_char = chars[j - 1]
                    break
        return output_length

        
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(compress(chars))
    print(chars)