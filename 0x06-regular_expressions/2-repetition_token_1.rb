#!/usr/bin/env ruby
# A script that matches the lines with 1 or 2
# alphabets inside the string "hn"

regex = /h[bt]*n/
ARGV.each do |arg|
  match = arg.scan(regex).join
  puts match
end    
