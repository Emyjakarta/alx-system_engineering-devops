#!/usr/bin/env ruby

regex = /h[bt]*n/

ARGV.each do |arg|
  match = arg.scan(regex).join
  puts match
end    
