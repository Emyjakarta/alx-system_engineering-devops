#!/usr/bin/env ruby
# A script to match lines having 2 to 5 't' in the string starting
# with 'hb' and ending with 'n'

regex = /hbt{2,5}n/
ARGV.each do |arg|
  match = arg.scan(regex).join("\n")
  puts match
end    
