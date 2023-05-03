#!/usr/bin/env ruby
# This script prints out the sender, receiver and flags from a log file
#

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
