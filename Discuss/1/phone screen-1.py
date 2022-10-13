# https://leetcode.com/discuss/interview-question/2412776/Bloomberg-1st-phone-screen.


# Merge intervals

# Given a buffer that contains multiple messages, parse the buffer and process each message.
# When an exchange sends several messages over a TCP socket, they can be concatenated when performing
# the read. This is solved by parsing the buffer, and splitting in to multiple messages for each process
# call.
# Please implement a packetize function that takes a constant char* and size_t:
# void packetize(const char *data, size_t length);
# This function can be a member function if necessary.
# The packetize function should call a process function, with signature:
# void process(const char *data, size_t length);

# Given data buffer may contain incomplete packet, which may continue in the next call to packetize.
# At the same time, buffer may contain multiple packets as well, in which case all of the packets must
# be collected and process should be called for each one.
