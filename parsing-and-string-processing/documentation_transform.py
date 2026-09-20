class Solution:
    def transformDocumentation(self, source: str) -> str:

        # 3 things i need to track : inside_word , result , in_backtick
        # I just keep appending to results if im not in backticks

        inside_word = ""
        result = ""
        in_backticks = False

        for char in source:

            if char == "`": 
                if in_backticks: # This is the case for the closing backtick, (It has to be, if it was the opener, you wouldn't be in_backticks)

                    if inside_word.isupper():
                        result += inside_word
                        result += "`"
                        inside_word = ""
                        in_backticks = False

                    else: 
                        capitalise_next = False
                        transformed_word = ""
                        for char in inside_word:
                            if char == "_":
                                capitalise_next = True
                            elif capitalise_next:
                                transformed_word += char.upper()
                                capitalise_next = False
                            else:
                                transformed_word += char

                        result += transformed_word
                        result += "`"
                        transformed_word = ""
                        in_backticks = False
                        inside_word = ""


                else: # so if you're not in backticks alerady you want to append the first backtick to reults and set in backticks to True
                    result += "`"
                    in_backticks = True

            else: 
                if in_backticks:
                    inside_word += char
                else:
                    result += char

        return result





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

        













