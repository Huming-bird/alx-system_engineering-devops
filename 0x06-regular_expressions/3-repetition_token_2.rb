#!/usr/bin/env ruby
# This script searches for any ocuurence of 'hbtn' string
#


puts ARGV[0].scan(/[hbt{1,4}n]/).join
