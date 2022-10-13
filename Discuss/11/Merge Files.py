# https://leetcode.com/discuss/interview-question/424409/Bloomberg-or-Phone-screen-or-Merge-Files


# Was asked a small variation of the Merge K Sorted List question -

# Given a list of files, each file containing any number of sorted strings, merge them into a single file.
# You can use the following methods as helpers if needed -

# File.readLine() -> returns the next line in the file
# File.hasNext() -> boolean if this has more lines
# File.writeLine(String) -> write a line to the file
# The signature of the method is public File merge(List<File> files) { ... }

# At the end of the code implementation, was asked to write the different test cases that the code should be tested against as well as implement a few tests using Junit and any Mock framework of choice.
# The tests cases I suggested were -

# 1. Empty input list
# 2. Null input list
# 3. happy case - multiple files, each file having multiple alphabetical strings in them
# 4. one or more file having non-alphabet chars (e.g. special chars)
# 5. multiple files, but one or more of them is empty / null
# 6. list having just 1 file
