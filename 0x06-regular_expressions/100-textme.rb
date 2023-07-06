#!/usr/bin/env ruby
format_string = ARGV[0].scan(/from:(\w+)|to:(\w+)|flags:([\d:-]+)/)
list = format_string.flatten.compact.join(',')
puts list
