#!/usr/bin/env ruby
# This script matches any 10 digit phone number
#

puts ARGV[0].scan(/\b[0-9]{10}\b/).join
