class Solution:
    def transformDocumentation(self, source: str) -> str:

        in_backticks = False
        current_identifier = []
        output = []

        def to_camel_case(identifier):
                    results = []
                    capitalise_next = False
                    for char in identifier:
                        if capitalise_next:
                            char = char.upper()
                            capitalise_next = False # reset capitalise next 
                        if char == "_": 
                            capitalise_next = True # if your char is an underscore, next char is caps
                        else: 
                            results.append(char) 
                    
                    results = "".join(results) 
                    
                    return results

        for char in source: 
            if char == "`": 
                if in_backticks == False: 
                    in_backticks = not in_backticks
                    current_identifier = [] # resets it each time you open a new backtick
                else: 
                    current_identifier = "".join(current_identifier)
                    if current_identifier.isupper():
                        output.append("`" + current_identifier + "`")
                    else:
                        output.append("`" + to_camel_case(current_identifier) + "`")
                    in_backticks = False
            else:
                if in_backticks == True:
                      current_identifier.append(char)
                else:
                     output.append(char)

        output = "".join(output)
        return output
                

s = Solution()

print(s.transformDocumentation("Use `get_user_name` to read `MAX_RETRIES`."))
# expected: "Use `getUserName` to read `MAX_RETRIES`."

print(s.transformDocumentation("`API_KEY` and `user_id` are required."))
# expected: "`API_KEY` and `userId` are required."

print(s.transformDocumentation("Call `send_email` now."))
# expected: "Call `sendEmail` now."

print(s.transformDocumentation("Use `MAX_SIZE` only."))
# expected: "Use `MAX_SIZE` only."

print(s.transformDocumentation("No identifiers here."))
# expected: "No identifiers here."

print(s.transformDocumentation("`a_b_c` and `X_Y_Z` done."))
# expected: "`aBC` and `X_Y_Z` done."

        













