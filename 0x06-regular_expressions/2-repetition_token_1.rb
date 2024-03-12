#!/usr/bin/env ruby
# A script that matches the lines with 1 or 2
# alphabets inside the string "hn"

regex = /h[a-z]{1,2}n/
ARGV.each do |arg|
  match = arg.scan(regex).join("\n")
  puts match
end    
