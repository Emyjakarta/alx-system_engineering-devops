#!/usr/bin/env ruby

regex = /h[bt]*n/

ARGV.each do |arg|
  match = arg.scan(regex).join("\n")
  puts match
end    
