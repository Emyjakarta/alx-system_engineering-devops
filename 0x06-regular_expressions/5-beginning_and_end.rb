#!/usr/bin/env ruby

regex = /^h.n$/

ARGV.each do |arg|
  match = arg.scan(regex).join
  puts match
end    
