#!/usrs/bin/env ruby
# This script searches for any string starting with h and ending with n
#

puts ARGV[0].scan(/^h.n$/).join
