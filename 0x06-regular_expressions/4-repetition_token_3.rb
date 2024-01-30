#!/usr/bin/env ruby

regex = /hbo?n|hbt+n/

ARGV.each do |arg|
  match = arg.scan(regex).join("\n")
  puts match
end    
