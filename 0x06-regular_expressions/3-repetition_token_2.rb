#!/usr/bin/env ruby

regex = /hbt*n/

ARGV.each do |arg|
  match = arg.scan(regex).join("\n")
  puts match
end    
