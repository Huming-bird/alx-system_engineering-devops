#!/usr/bin/env ruby
# This script matches only capital letters
#


puts ARGV[0].scan(/\b[A-Z]\b/).join
