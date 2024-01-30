#!/usr/bin/env ruby

regex = /hbt*n/

ARGV.each do |arg|
  match = arg.scan(regex).join
  puts match
end    
